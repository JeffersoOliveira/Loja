from django.urls import path, include


from Produto import views


urlpatterns = [
    
    path('', views.cadastroProduto, name='cadastroProduto'),
    path('lista/', views.listarProduto, name='listarProduto'),
    path('lista/<codBarras>', views.editarProduto, name='editarProduto'),
    
    # path('', views.cadastroCliente, name='cadastroCliente'),
    # path('listar', views.listarCliente, name='listarCliente'),
    # path('listar/<id>', views.detalhesCliente, name='detalhesCliente'),
    # path('delete/<id>', views.deleteCliente, name='deleteCliente'),
    # path('atualizar', views.atualizarCliente, name='atualizarCliente'),
]

