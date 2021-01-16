from django.urls import path
from .views      import DataAnalysis,UserListView,UserDetailView

urlpatterns = [
    path('data_analysis/', DataAnalysis,            name='analysis'),
    path('',               UserListView.as_view(),  name='user_list'),
    path('<int:pk>/',      UserDetailView.as_view(),name='user_detail'),
]
