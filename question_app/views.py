from django.views.generic           import TemplateView 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins     import LoginRequiredMixin
from django.contrib                 import messages
from django.http                    import Http404
from django.shortcuts               import get_object_or_404,render,redirect
from .models                        import Question,Numbering,Attempt


class TermsConditionView( LoginRequiredMixin,TemplateView ):
    '''Terms and conditions page.'''

    template_name = 'terms_condition.html'

    def get_context_data( self,**kwargs ):
        context                     = super().get_context_data( **kwargs )
        context[ 'question' ]       = Question.objects
        return context


@login_required()
def QuestionPage( request, question_id=None ):
    '''Show Detail Page with messages.'''

    if not request.user.is_complete_quiz:
        if type(question_id):
            try:
                obj_numbering = Numbering.objects.get( question_number=question_id )

            except Numbering.DoesNotExist:
                '''Extra work for result page.'''

                if question_id == 0:
                    '''is_complete_quiz have to true'''

                    request.user.is_complete_quiz = True 
                    request.user.save()
                    return redirect( 'result' ) 

                raise Http404('Question Not Found')

            question_obj  = get_object_or_404( Question,  question_number=obj_numbering )
            context       = { 'question' : question_obj,
                              'passing_pushes' : Question.objects.passing_pushes 
                            }
            return render( request , 'question.html' ,context=context)

        raise Http404('Question Not Found')
    return redirect( 'no_replay' )


@login_required()
def FormProcessing( request, question_id=None ):
    '''Take form inputs,then redirect with message after comparision.'''

    if request.method == 'POST':

        obj_numbering = get_object_or_404( Numbering, question_number=question_id )
        question_obj  = get_object_or_404( Question, question_number=obj_numbering )

        if not Attempt.objects.filter( contestent=request.user,
                                       contestent_question=question_obj 
                                     ).exists():

            answer      = request.POST.get('image_selected') 
            attempt_obj = Attempt( contestent=request.user, contestent_question=question_obj )


            '''Comparision with answer'''
            if answer in ['A','B','C','D']:

                #When the answer is wrong
                if not question_obj.answer == answer:
                    messages.error( request,
                                    'Gand Maraliye, Ans was %s' %(question_obj.answer) 
                                  )
                    attempt_obj.contestent_answer='W'
                
                #When the answer is correct
                else:
                    request.user.increase_winning_prize
                    request.user.increase_correct_answers
                    messages.success( request,
                                      'Sahi Jawab!, 10rs paytm cash'
                                    )
                    attempt_obj.contestent_answer='R'

            #When the question is skipped
            else:
                messages.warning( request,'Aapki gand phat gyi lgta')
                
                # skip question many2many
                request.user.skip_question.add( question_obj ) 
                attempt_obj.contestent_answer='S'

            # save
            request.user.save()
            attempt_obj.save()
            
            # Next question
            return redirect( 'question', question_id=question_id-1 )

        # add msg already answered
        else:
            messages.warning( request,
                              'Already answered this question'  
                            )

    # redirect to same page
    return redirect( 'question', question_id=question_id )


class ResultView( LoginRequiredMixin,TemplateView ):
    '''Showing the logged-in user's result page.'''

    template_name = 'user_result.html'

    def get_context_data( self,**kwargs ):
        context                     = super().get_context_data( **kwargs )
        context['total_questions']  = Question.objects.total_questions
        return context
 
