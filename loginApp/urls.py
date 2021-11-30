from os import name
from django.urls import path

from . import views

app_name = 'loginApp'

urlpatterns = [
    path('', views.login_page),
    path('login/', views.login_page, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout'),
]