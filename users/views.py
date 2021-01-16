from django.shortcuts     import render
from django.views.generic import ListView,DetailView
from .models              import CustomUser


class UserListView( ListView ):
    model               = CustomUser
    template_name       = 'user_list.html' 
    context_object_name = 'user_list'

class UserDetailView( DetailView ):
    model               = CustomUser
    template_name       = 'user_detail.html' 
    context_object_name = 'user_obj'

def DataAnalysis( request ):
    '''Send required data to template to show the graph'''

    username_list        = []
    correct_answers_list = []
    skiped_question_list = []

    for x in CustomUser.objects.all():
        username_list.append( x.username )
        correct_answers_list.append( x.correct_answers )
        skiped_question_list.append( x.total_skip_question )

    context = {
            'username_list'        : username_list,
            'correct_answers_list' : correct_answers_list,
            'skiped_question_list' : skiped_question_list
        }

    return render( request , 'data_analysis.html', context )
        



