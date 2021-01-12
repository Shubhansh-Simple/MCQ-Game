from django.urls import path
from .views      import QuestionPage,FormProcessing,TermsConditionView

urlpatterns = [
    path('terms/',     TermsConditionView.as_view(), name='terms_condition'),
    path('question/<int:question_id>/',  QuestionPage, name='question'),
    
    # do the backend stuff.
    path('processing/<int:question_id>/', FormProcessing , name='form_processing')
]
