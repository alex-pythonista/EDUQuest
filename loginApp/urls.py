from os import name
from django.urls import path

from . import views

app_name = 'loginApp'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register, name='register'),
]