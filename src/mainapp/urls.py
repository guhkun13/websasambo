# from django.conf.urls import *
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views
# from . import ajax_class

app_name = 'mainapp'
urlpatterns = [
    path('', views.index, name="index"),
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'),
    path('dashboard/', views.dashboard, name="dashboard"),
]
