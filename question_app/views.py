from django.views.generic           import TemplateView 
from django.contrib.auth.decorators import login_required
from django.contrib.auth            import get_user_model
from django.contrib                 import messages
from django.http                    import Http404
from django.shortcuts               import get_object_or_404,render,redirect
from .models                        import Question,Numbering


#@login_required()
class TermsConditionView( TemplateView ):
    template_name = 'terms_condition.html'


@login_required()
def QuestionPage( request, question_id=None ):
    '''Show Detail Page and conditional context data.'''

    if question_id:
        obj_numbering = get_object_or_404( Numbering, question_number=question_id )
        obj           = get_object_or_404( Question,  question_number=obj_numbering )
        
        context       = { 'question' : obj }

        return render( request , 'question.html' ,context=context)
    else:
        raise Http404('Page Not Found.')


@login_required()
def FormProcessing( request, question_id=None ):
    '''Take form input and compare with answer redirect with message.'''

    if request.method == 'POST':
        answer     = request.POST.get('image_selected') 

        obj_numbering = get_object_or_404( Numbering, question_number=question_id )
        obj           = get_object_or_404( Question, question_number=obj_numbering )
        user_login    = get_object_or_404( get_user_model(), pk=request.user.id  )

        '''Comparision with answer'''
        if answer in ['A','B','C','D']:

            #When the answer is wrong
            if not obj.answer == answer:
                messages.error( request,'Gand Maraliye, Ans was %s' %(obj.answer) )
            
            #When the answer is correct
            else:
                user_login.increase_winning_prize
                user_login.increase_correct_answers
                messages.success( request,'Sahi Jawab!.Paytm Cash - {}rupeej.'.format(user_login.winning_prize) )

        #When the question is skipped
        else:
            messages.info( request,'Aapki phat k chaar!')
            user_login.skip_quesiton = obj

        user_login.save()
        return redirect('/question/{}/'.format(question_id+1) )

    else:
        raise Http404('Invalid Data.')



 
