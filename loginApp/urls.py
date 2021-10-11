from django.urls import path

from . import views

app_name = 'loginApp'

urlpatterns = [
    path('', views.login_page, name='login'),
]