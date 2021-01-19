from django.urls import path
from .views      import QuestionPage,\
                        FormProcessing,\
                        TermsConditionView,\
                        ResultView

# it's imported from different source
from django.views.generic.base import TemplateView

urlpatterns = [
    path('terms/',     TermsConditionView.as_view(), name='terms_condition'),
    path('question/<int:question_id>/',  QuestionPage, name='question'),
    
    # if user try to replay the game ( redirect here ).
    path('no_replay/', TemplateView.as_view( template_name='no_replay.html'), name='no_replay' ),
    
    # do the backend stuff.
    path('processing/<int:question_id>/', FormProcessing , name='form_processing'),

    path('results/', ResultView.as_view(),  name='result' ),
]
