from django.urls import path
from .views      import DataAnalysis,UserListView,UserDetailView

urlpatterns = [
    path('analyse_data/',  DataAnalysis,            name='analyse_data'),
    path('',               UserListView.as_view(),  name='user_list'),
    path('<int:pk>/',      UserDetailView.as_view(),name='user_detail'),
]
