from django.urls import path
from .views      import DataAnalysis,UserListView,ContributorsListView

urlpatterns = [
    path('analyse_data/',  DataAnalysis,            name='analyse_data'),
    path('',               UserListView.as_view(),  name='user_list'),
    path('contributors/',  ContributorsListView.as_view(),  name='contributors_list'),
]
