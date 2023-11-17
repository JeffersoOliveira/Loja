from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


from .models import Cliente
from .forms import ClientePfForm, ClientePjForm

# Create your views here.
def teste(request):
    return HttpResponse('teste')


@login_required
def cadastroCliente(request):
    if request.method == 'GET':

        return render(request, 'cliente/cliente.html', {
            'form': ClientePfForm
        })
    elif request.method == 'POST':
        if request.POST.get('tipo') == "1":
            form = ClientePfForm(request.POST)

            if form.is_valid():
                cliente = Cliente.objects.filter(cpf = request.POST.get('cpf'))               
                if cliente:
                    messages.warning(request, 'Cpf já cadastrado no sistema')
                    return redirect('cadastroCliente')
                
                form.save()

                messages.info(request, 'Cliente cadastrado com sucesso.')
                return redirect('cadastroCliente') 

            else:
                messages.info(request, 'Algo deu errado, por favor contate o administrador.')
                return redirect('cadastroCliente') 

        elif request.POST.get('tipo') == "2":
            form = ClientePjForm(request.POST)

            if form.is_valid():
                cliente = Cliente.objects.filter(cnpj = request.POST.get('cnpj'))               
                if cliente:
                    messages.warning(request, 'Cnpj já cadastrado no sistema')
                    return redirect('cadastroCliente')
                
                print(form.cleaned_data['razaosocial'])
                form.save()

                messages.info(request, 'Cliente cadastrado com sucesso.')
                return redirect('cadastroCliente') 

            else:
                messages.info(request, 'Algo deu errado, por favor contate o administrador.')
                return redirect('cadastroCliente') 
   
        return render(request, 'cliente/cliente.html')

@login_required
def listarCliente(request):
    list = Cliente.objects.all()
    # lista = [x*x for x in list[x].id];
    return render(request, "cliente/listar.html", {'List': list})

@login_required
def detalhesCliente(request, id):
    if request.method == 'GET':
        cliente = get_object_or_404(Cliente, pk=id)     
        return render(request, "cliente/cliente_detalhes.html", {'cliente': cliente})

@login_required
def deleteCliente(request, id):
    if request.method == 'GET':
        cliente = get_object_or_404(Cliente, pk=id)
        return render(request, "cliente/cliente_delete.html", {'cliente': cliente})
    if request.method == 'POST':
        cliente = get_object_or_404(Cliente, pk=id)
        cliente.delete()
        return redirect('listarCliente')

@login_required
def atualizarCliente(request):
    if request.method == 'GET':
        return redirect('listarCliente')
    
    elif request.method == 'POST':
        tipo = request.POST.get('tipo')
        id = request.POST.get('id')

        cliente = get_object_or_404(Cliente, pk=id)

        if tipo == '1' :
            form = ClientePfForm(request.POST, instance=cliente)
        else:
            form = ClientePjForm(request.POST , instance=cliente)

        if form.is_valid():

            form.save()

        messages.success(request, 'Cliente editado com sucesso.')
        return redirect('listarCliente')
    
