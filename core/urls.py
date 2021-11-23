
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from studentApp.views import *

from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('loginApp.urls')),
    path('', include('studentApp.urls')),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)