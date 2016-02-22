from rest_framework import serializers

from inventario_app.models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
