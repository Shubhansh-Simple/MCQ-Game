from django.urls import path
from .views      import QuestionPage,\
                        FormProcessing,\
                        TermsConditionView,\
                        Quit,\
                        ResultView,\
                        FullResult

# it's imported from different source
from django.views.generic.base import TemplateView

urlpatterns = [
    path('terms/',     TermsConditionView.as_view(), name='terms_condition'),
     
    # if user try to replay the game ( redirect here ).
    path('no_replay/', TemplateView.as_view( template_name='no_replay.html'), name='no_replay' ),

    path('question/<int:question_id>/',   QuestionPage,   name='question'),

    # do the backend stuff.
    path('processing/<int:question_id>/', FormProcessing, name='form_processing'),

    path('quit/',         Quit ,                       name='quit'),
    path('results/',      ResultView.as_view(), name='result' ),
    path('full_results/', FullResult,       name='full_result' ),
]
