from django.urls import path

from . import views

app_name = 'forumApp'

urlpatterns = [
    path('forum/', views.forum, name='forum'),
    path('question/<str:pk>/', views.discussion_view, name='discussion'),
]