from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

def teste(request):
    return render(request, 'base1.html')

def home(request):
    return render(request, 'home.html')

def logar(request):
    if request.method == 'GET':
        return render(request, 'login/login.html')
    else:
        username = request.POST['username'] # email
        password = request.POST['password']
        print(username, password)

        user = authenticate(
            request, username=username, password= password
        )
        if user is None:
            messages.warning(request, 'Usuário ou senha está incorreto.')
            return redirect('login')

        else:
            login(request, user)
            return redirect('home')

def desLogar(request):
    if request.method == 'GET':
        print('DESLOGAR')
        logout(request)
        return redirect('login')




@login_required
def cadastroUsuario(request):
    if request.method == 'GET':
        return render(request, 'usuario/usuario.html')
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username'] # email
        password = request.POST['password']
        password1 = request.POST['password1']

        if first_name == '' or last_name == '' or username == '' or password =='' or password1 == '':
            messages.warning(request, 'Todos os campos são obrigatórios!')
            return redirect('cadastroUsuario')
        
        if password != password1:
            messages.warning(request, 'Senhas não conferem.')
            return redirect('cadastroUsuario')
        
        try:
            user  = User.objects.create_user(username=username, email=username, password=password, first_name=first_name, last_name=last_name, is_staff=True)
            user.save()

            # login(request, user)
            messages.success(request, 'Cadastro realizado com sucesso.')
            return redirect('cadastroUsuario')

        except:
            messages.info(request, 'Usuário ja cadastrado.')
            return redirect('cadastroUsuario')

        # print(first_name, last_name, username, password, password1)      
        # return render(request, 'usuario/usuario.html')