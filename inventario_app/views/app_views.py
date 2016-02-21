from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login 
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

@csrf_protect
def user_login(request):

    if request.method == 'GET':
        print('Method: get')
        return render(request, 'login.html')

    elif request.method == 'POST':
        print('Method Post')
        username = request.POST['username']
        password = request.POST['password']
        print(request.POST)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'index.html')
            else:
                return render(request, 'login.html', {'error_message': 'El usuario no esta activo'})
        else:
            return render(request, 'login.html', {'error_message': 'Usuario o contraseña inválidos'})

    return render(request, 'login.html')

@login_required
def index(request):
    return render(request, 'index.html')
