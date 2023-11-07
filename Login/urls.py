from django.contrib import admin
from django.urls import path, include
from Login import views

urlpatterns = [
    
    path('', views.logar, name='login'),
    path('sair', views.desLogar, name='sair'),
]