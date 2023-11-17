from django.contrib import admin
from django.urls import path, include
from Cliente import views
from Cliente import tests

urlpatterns = [
    
    # path('', views.teste, name='teste'),

    path('', views.cadastroCliente, name='cadastroCliente'),
    path('listar', views.listarCliente, name='listarCliente'),
    path('listar/<id>', views.detalhesCliente, name='detalhesCliente'),
    path('delete/<id>', views.deleteCliente, name='deleteCliente'),
    path('atualizar', views.atualizarCliente, name='atualizarCliente'),
]