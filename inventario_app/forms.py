from django.forms import ModelForm
from inventario_app.models import Producto

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        #exclude = ['']
        fields = ['nombre', 
        'descripcion', 
        'codigo', 
        'proveedor', 
        'precio_compra', 
        'precio_venta', 
        'stock',
        'stock_minimo',
        'stock_maximo',
        ]
