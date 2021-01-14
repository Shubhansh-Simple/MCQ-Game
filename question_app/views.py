from django.views.generic           import TemplateView 
from django.contrib.auth.decorators import login_required
from django.contrib.auth            import get_user_model
from django.contrib.auth.mixins     import LoginRequiredMixin

from django.http                    import HttpResponse

from django.contrib                 import messages
from django.http                    import Http404
from django.shortcuts               import get_object_or_404,render,redirect
from .models                        import Question,Numbering


#@login_required()
class TermsConditionView( TemplateView ):
    '''Terms and conditions page.'''

    template_name = 'terms_condition.html'

    def get_context_data( self,**kwargs ):
        context                     = super().get_context_data( **kwargs )
        context['last_question']   = Question.objects.last().question_number.question_number
        return context


@login_required()
def QuestionPage( request, question_id=None ):
    '''Show Detail Page with messages.'''

    if question_id:
        obj_numbering = get_object_or_404( Numbering, question_number=question_id )
        obj           = get_object_or_404( Question,  question_number=obj_numbering )

        #request.user.is_complete_quiz = True 
        
        context       = { 'question' : obj }

        return render( request , 'question.html' ,context=context)
    else:
        raise Http404('Page Not Found.')


@login_required()
def FormProcessing( request, question_id=None ):
    '''Take form inputs,compare with answer then redirect with message.'''

    if request.method == 'POST':
        answer     = request.POST.get('image_selected') 

        obj_numbering = get_object_or_404( Numbering, question_number=question_id )
        obj           = get_object_or_404( Question, question_number=obj_numbering )
        user_login    = get_object_or_404( get_user_model(), pk=request.user.id  )

        '''Comparision with answer'''
        if answer in ['A','B','C','D']:

            #When the answer is wrong
            if not obj.answer == answer:
                messages.error( request,
                                'Gand Maraliye, Ans was %s' %(obj.answer) 
                              )
            
            #When the answer is correct
            else:
                user_login.increase_winning_prize
                user_login.increase_correct_answers
                messages.success( request,
                                  'Sahi Jawab!'
                                )

        #When the question is skipped
        else:
            messages.info( request,'Aapki phat k chaar!')
            
            # skip question many2many
            user_login.skip_quesiton.add( obj ) 

        user_login.save()
        
        # result page if it's last question.
        if question_id == 1:
            '''is_complete_quiz have to true'''
            # try-except for 0 question number
            return redirect( 'ResultView' ) 

        return redirect( '/question/{}/'.format(question_id-1) )

    else:
        raise Http404('Invalid Data.')


class ResultView( LoginRequiredMixin,TemplateView ):
    '''Showing the logged-in user's result page.'''

    template_name = 'user_result.html'


    def get_context_data( self,**kwargs ):
        context                     = super().get_context_data( **kwargs )
        context['total_questions']   = Question.objects.all().count()
        return context
 
