from rest_framework import serializers

from inventario_app.models import Producto, Cliente
from django.contrib.auth.models import User

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto

class ClienteSerializer(serializers.ModelSerializer):
	nombre = serializers.ReadOnlyField(source="user.first_name")
	apellido = serializers.ReadOnlyField(source="user.last_name")

	class Meta:
		model = Cliente
