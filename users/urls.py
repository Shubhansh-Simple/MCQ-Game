from django.urls import path
from .views      import DataAnalysis

urlpatterns = [
    path('',    DataAnalysis  , name='analysis'),
]
