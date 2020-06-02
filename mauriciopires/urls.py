from django.conf.urls import url
from django.urls import include, path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from .views import (
    index,
    paneladmin,
    register,
    account_activation_sent,
    new_register,
    images,
    register_images,
    alluser,
    search,
    payment,
    register_payment,
    search2,
    ImagesUpdate
    
)


urlpatterns = [
    url(r'^index/$', index, name='mauriciopires_index'),
    url(r'^paneladmin/$', paneladmin, name='paneladmin_index'),
    url(r'^register/$', register, name='paneladmin_register'),
    url(r'^newregister/$', new_register, name='paneladmin_new_register'),
    url(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    url(r'^images/$', images, name='paneladmin_images'),
    url(r'^registerimages/$', register_images, name='paneladmin_register_images'),
    url(r'^alluser/$', alluser, name='paneladmin_alluser'),
    url(r'^sales_list/$', search, name='paneladmin_sales'),
    url(r'^accounting/$', search2, name='paneladmin_accounting'),
    url(r'^payment/$', payment, name='paneladmin_payment'),
    url(r'^register_payment/$', register_payment, name='paneladmin_register_payment'),
    url(r'^imagens_update/(?P<id>\\d+)/$', views.ImagesUpdate, 
     name='paneladmin_imagens_update'),
    url(r'^payments_list/$', search2, name='paneladmin_payments_list'),
   
     
    
]