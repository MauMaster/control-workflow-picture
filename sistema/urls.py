
from django.contrib import admin
from django.urls import path, include
from mauriciopires.views import index
from django.contrib.auth import logout
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', index),
    path(r'mauriciopires/', include('mauriciopires.urls')),
    path(r'', include('mauriciopires.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
