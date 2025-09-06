from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('sign/', views.sign, name='sign'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('list_aprendises/', views.gention_aprendices, name='list_aprendises'),

]