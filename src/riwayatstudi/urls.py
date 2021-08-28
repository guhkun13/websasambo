from django.urls import path

from . import views

app_name = 'riwayatstudi'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('edit/', views.edit, name='edit'),
    path('save/', views.save, name='save'),
    path('delete/<int:id>', views.save, name='delete'),

]
