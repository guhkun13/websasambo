# from django.conf.urls import *
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views
# from . import ajax_class
app_name = 'survey'

urlpatterns = [
    path('', views.index, name="index"),    
    path('riwayat_studi/add', views.riwayat_studi_add, name="riwayat_studi_add"),    
    path('riwayat_studi/create_or_update', views.riwayat_studi_create_or_update, name="riwayat_studi_create_or_update"),    
]
