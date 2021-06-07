from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('estadios/', views.estadios, name='estadios'),
    path('estadio/<int:estadio_id>/', views.estadio, name='estadio'),
    path('log_in/', views.log_in, name='log_in'),
    path('eventos/', views.eventos, name='eventos'),
]
