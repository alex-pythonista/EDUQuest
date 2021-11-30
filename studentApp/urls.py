from os import name
from django.urls import path

from . import views

app_name = 'studentApp'

urlpatterns = [
    path('developers/', views.dev_page, name='dev-page'), # uploaded
    path('profile/', views.profile_view, name = 'profile'), #done
    path('routine/', views.routine_view, name = 'routine'), #done
    path('schedule_checker/', views.schedule_checker_view, name = 'schedule_checker'),
    path('progress/', views.progress_view, name = 'progress'),
    path('instructor/', views.instructor_view, name = 'instructor'), #done
    path('finances/', views.finances_view, name = 'finances'),
    path('bus_schedule/', views.bus_schedule_view, name = 'bus_schedule'), #uploaded
    path('courses/', views.catalog_view, name = 'courses'),
]