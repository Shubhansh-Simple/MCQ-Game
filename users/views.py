from django.shortcuts import render
from .models     import CustomUser
#import pandas    as     pd


def DataAnalysis( request ):

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
        



