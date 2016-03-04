from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from inventario_app.forms import ProductoForm
from inventario_app.models import Cliente, Empleado, Factura
from django.contrib.auth.models import User, Group



@login_required
def log_out(request):
    logout(request)
    return redirect('/')

@login_required
def index_view(request):
    groups = request.user.groups.all()
    print(groups)
    return render(request, 'index.html')

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


@method_decorator(login_required, name='dispatch')
class Registrar_Empleado(View):

    def get(self, request):
        return render(request, 'registrar_empleado.html')

    @method_decorator(csrf_protect)
    def post(self, request):
        print(request.POST)
        if User.objects.filter(username=request.POST['username']).exists():
            return render(
                request, 
                'registrar_empleado.html', 
                {'error_message': 'No pudo ser registrado porque el usuario ya existe'})
        try:
            user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            group = Group.objects.get(name=request.POST['cargo'])
            user.groups.add(group)
            user.is_staff = True
            user.save()
            empleado = Empleado.objects.create(
                user=user, 
                cedula=request.POST['cedula'],
                telefono=request.POST['telefono'],
                sexo=request.POST['sexo'],
                cargo=request.POST['cargo']
                )
        except Exception as e:
            print(e)
            try: 
                user.remove()
            except Exception as e2:
                print(e2)
            return render(
                request, 
                'registrar_empleado.html', 
                {'error_message': 'Error en los datos ingresados'})
        return render(request, 
            'registrar_empleado.html', 
            {'message': 'Usuario Registrado Satisfactoriamete'})

class RegistrarCliente(View):

    def get(self, request):
        return render(request, 'registrar_cliente.html')

    def post(self, request):
        print(request.POST)
        try:
            user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            group = Group.objects.get(name='Cliente')
            user.groups.add(group)
            user.save()
            cliente = Cliente.objects.create(
                user=user, 
                cedula=request.POST['cedula'],
                telefono=request.POST['telefono'],
                telefono_alternativo=request.POST['telefono_alternativo'],
                sexo=request.POST['sexo'],
                )
            if cliente:
                context = {
                'message': 'Cliente registrado Satisfactoriamete'
                }
        except Exception as e:
            print (e)
            try:
                user.remove()
            except:
                pass
            context = {'message':'cliente no registrado', 'error_message' : 'Datos de usuraio invalidos'}
        return render(request, 'registrar_cliente.html', context)

@method_decorator(login_required, name='dispatch')
class GenerarFactura(View):

    def get(self, request):
        return render(request, 'generar_factura.html')

    def post(self, request):
        context = {}
        data = request.POST
        cedula = data['cedula']
        try:
            cliente = Cliente.objects.get(cedula=cedula)
        except Exception as e:
            print(e)
            context.error_message = 'cedula de cliente invalida'
            return render(request, 'generar_factura.html', context)
        productos = data['productos']
        prodarray = []
        if len(productos) == 0:
            context.error_message = 'No se encontraron productos para registrar'
            return render(request, 'generar_factura.html', context)
        else:
            for codigo in productos:
                try:
                    producto = Producto.objects.get(codigo=codigo)
                    prod_array.append(producto)
                except Exception as e:
                    print(e)
                    context.error_message = 'No se encontraron productos para registrar'
                    return render(request, 'generar_factura.html', context)

        factura = Factura.objects.create(cliente = cliente)
        factura.save()

        for producto in prod_array:
            factura.productos.add(producto)

        factura.save()
        return render(request, 'generar_factura.html', {'message', 'Factura generada staisfactoriamente'})

                