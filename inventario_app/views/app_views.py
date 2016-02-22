from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from inventario_app.forms import ProductoForm


@login_required
def log_out(request):
    logout(request)
    return redirect('/')

class User_login(View):

    def get(self, request):
        return render(request, 'login.html')

    @method_decorator(csrf_protect)
    def post(self, request):
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


@method_decorator(login_required, name='dispatch')
class Registrar_producto(View):

    def get(self, request):
        return render(request, 'registrar_producto.html')

    @method_decorator(csrf_protect)
    def post(self, request):
        print(request.POST)
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print('error registering the product')
            print('form errors')
            print(form.errors)
        return render(request, 'registrar_producto.html', {'form': form})


