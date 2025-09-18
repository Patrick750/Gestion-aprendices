from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin_sign/', views.admin_sign, name='admin_sign'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('list_aprendises/', views.gention_aprendices, name='list_aprendises'),
    path('list_aprendises/eliminar/<str:documento>/', views.eliminar, name='eliminar_aprendiz'),
    
]