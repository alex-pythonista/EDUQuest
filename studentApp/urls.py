from os import name
from django.urls import path

from . import views

app_name = 'studentApp'

urlpatterns = [
    path('developers/', views.dev_page, name='dev-page'), # has issues

    path('profile/', views.profile_view, name = 'profile'),
    path('routine/', views.routine_view, name = 'routine'),
    path('schedule_checker/', views.schedule_checker_view, name = 'schedule_checker'),
    path('progress/', views.progress_view, name = 'progress'),
    path('instructor/', views.instructor_view, name = 'instructor'),
    path('finances/', views.finances_view, name = 'finances'),
    path('forum/', views.forum_view, name = 'forum'),
    path('bus_schedule/', views.bus_schedule_view, name = 'bus_schedule'),
    path('catalog/', views.catalog_view, name = 'catalog'),
    
]