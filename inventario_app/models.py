from django.db import models

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
