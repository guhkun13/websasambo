from django.urls import path

from . import views

app_name = 'riwayatkerja'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('save/', views.save, name='save'),
    path('delete/<int:id>', views.delete, name='delete'),

]
