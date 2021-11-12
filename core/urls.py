
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('loginApp.urls')),
    path('student_frameset/', include('studentApp.urls')),
]
