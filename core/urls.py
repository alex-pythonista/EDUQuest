
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from studentApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('loginApp.urls')),
    path('student_frameset/', include('studentApp.urls')),
    path('profile/', profile_view, name = 'profile'),
    path('routine/', routine_view, name = 'routine'),
    path('schedule_checker/', schedule_checker_view, name = 'schedule_checker'),
    path('progress/', progress_view, name = 'progress'),
    path('instructor/', instructor_view, name = 'instructor'),
    path('finances/', finances_view, name = 'finances'),
    path('forum/', forum_view, name = 'forum'),
    path('bus_schedule/', bus_schedule_view, name = 'bus_schedule'),
    path('catalog/', catalog_view, name = 'catalog'),
]
