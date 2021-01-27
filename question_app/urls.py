from django.urls import path
from .views      import QuestionPage,\
                        FormProcessing,\
                        TermsConditionView,\
                        Quit,\
                        ResultView,\
                        FullResult

urlpatterns = [
    path('',     TermsConditionView.as_view(), name='terms_condition'),
     
    path('question/<int:question_id>/',   QuestionPage,   name='question'),

    # do the backend stuff.
    path('processing/<int:question_id>/', FormProcessing, name='form_processing'),

    path('quit/',         Quit ,                name='quit'),
    path('results/',      ResultView.as_view(), name='result' ),
    path('full_results/', FullResult,           name='full_result' ),
]
