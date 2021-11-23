from django.urls import path

from . import views

app_name = 'forumApp'

urlpatterns = [
    path('forum/', views.forum, name='forum'),
]