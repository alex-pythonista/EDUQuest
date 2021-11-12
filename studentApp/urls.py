from os import name
from django.urls import path

from . import views

app_name = 'studentApp'

urlpatterns = [
    path('developers/', views.dev_page, name='dev-page'),
    
]