from django.shortcuts     import render
from django.views.generic import ListView,DetailView
from .models              import CustomUser
from .utils               import get_plot


class UserListView( ListView ):
    '''All the user in database'''

    model               = CustomUser
    template_name       = 'user_list.html' 
    context_object_name = 'user_list'

    def get_queryset( self ):
        return CustomUser.objects.hide_special_user

class UserDetailView( DetailView ):
    '''Users skipped question'''

    model               = CustomUser
    template_name       = 'user_detail.html' 
    context_object_name = 'user_obj'

def DataAnalysis( request ):
    '''Send required data to template to show the graph'''

    username_list        = []
    correct_answers_list = []
    skiped_question_list = []

    for x in CustomUser.objects.hide_special_user:
        username_list.append( x.username )
        correct_answers_list.append( x.correct_answers )
        skiped_question_list.append( x.total_skip_question )
        
    chart = get_plot( correct_answers_list,skiped_question_list,username_list )


    return render( request , 'data_analysis.html', { 'chart':chart } )
        



