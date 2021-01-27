from django.shortcuts              import render
from django.contrib.auth.mixins    import LoginRequiredMixin
from django.views.generic          import ListView
from .models                       import CustomUser,Contributor
from .utils                        import get_plot


class UserListView( LoginRequiredMixin,ListView ):
    '''All the user in database'''

    model               = CustomUser
    template_name       = 'user_list.html' 
    context_object_name = 'user_list'

    def get_queryset( self ):
        return CustomUser.hide_special_user()


def DataAnalysis( request ):
    '''Send required data to template to show the graph'''

    username_list        = []
    correct_answers_list = []
    #skiped_question_list = []

    for x in CustomUser.whose_quiz_complete():
        username_list.append( x.username )
        correct_answers_list.append( x.correct_answers )
        #skiped_question_list.append( x.total_skip_question )
        
    chart = get_plot( correct_answers_list,username_list )

    return render( request , 'data_analysis.html', { 'chart':chart } )
        
class ContributorsListView( ListView ):
    model               = Contributor
    template_name       = 'contributors_template.html'
    context_object_name = 'contributor_list'


