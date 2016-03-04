from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    codigo = models.PositiveIntegerField()
    proveedor = models.CharField(max_length=100)
    precio_compra = models.FloatField()
    precio_venta = models.FloatField(blank=True, null=True)
    stock = models.PositiveIntegerField()
    stock_minimo = models.PositiveIntegerField(blank=True, null=True)
    stock_maximo = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return '[' + str(self.codigo) + '] - ' + self.nombre + ': ' + str(self.precio_venta) + ' Bs'

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cedula = models.PositiveIntegerField(primary_key=True, unique=True)
    telefono = models.CharField(max_length=15)
    telefono_alternativo = models.CharField(max_length=15, blank=True, null=True)
    sexo = models.CharField(default="M",choices=(('M','Masculino'),('F', 'Femenino')), max_length=1)
    
    def __str__(self):
        return self.user.first_name + ': ' + str(self.cedula) 

class Empleado(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cedula = models.PositiveIntegerField(primary_key=True, unique=True)
    sexo = models.CharField(default="M",choices=(('M','Masculino'),('F', 'Femenino')), max_length=1)
    telefono = models.CharField(max_length=15)
    cargo = models.CharField(max_length=25,
        default="Empleado", 
        choices=(
            ('Departamento de Recepcion', 'Departamento de Recepcion'),
            ('Empleado', 'Empleado'),
            ('Administrador', 'Administrador'),
            ))
    def __str__(self):
        return self.user.first_name + ': ' + str(self.cedula) 

class Factura(models.Model):
    productos = models.ManyToManyField('Producto')
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    creada = models.DateTimeField(auto_now_add=True)
