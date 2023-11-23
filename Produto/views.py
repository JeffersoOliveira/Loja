from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
import os

from PIL import Image

from Produto.forms import ProdutoForms, ProdutoEditForms
from Produto.uteis import resize_img
from Produto.models import Produto



@login_required
def cadastroProduto(request):    
    if request.method == 'POST':
        form = ProdutoForms(request.POST, request.FILES)

        img = request.FILES.get('img')
        codBarras = request.POST.get('codBarras', None)

        if form.is_valid():

            form.save()
            caminho_imag = os.path.join('media','images', codBarras+'.'+img.name.split('.')[1])
            resize_img(caminho_imag, 600)

            messages.success(request, 'Produto cadastrado com sucesso.')
            return redirect('cadastroProduto')
        else:
            context = {
                'form': form
            }
            return render(request, 'produto/produto.html', context=context)
    else:
        form = ProdutoForms()

    context = {
        'form': form
    }
    return render(request, 'produto/produto.html', context=context)

@login_required
def listarProduto(request):

    if request.method == 'GET':
        produtos  = Produto.objects.all()


        context = {
            'produtos': produtos
        }
        return render(request, 'produto/produto_lista.html', context=context)

@login_required
def editarProduto(request, codBarras):
    if request.method == 'GET':
        produto = get_object_or_404(Produto, codBarras=codBarras)
        form = ProdutoEditForms(instance=produto)
        context = {
            'form': form
        }

        return render(request, 'produto/produto_detalhes.html', context=context)
    
    elif request.method == 'POST':
        produto = get_object_or_404(Produto, codBarras=codBarras)
        form = ProdutoEditForms(request.POST,  instance=produto)
        print(form)
        form.save()
        return HttpResponse('teste')