from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from inventario_app.serializers import ProductoSerializer
from inventario_app.models import Producto

from django.http import Http404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect



class ProductoList(APIView):
    """
    Genera una lista de los productos, tambien recibe get requests para filtrar por nombre o codigo.
    """
    def get(self, request, format=None):
        
        data = request.GET
        print(data)
        if 'codigo' in data:
            try:
                producto = Producto.objects.get(codigo=request.GET['codigo'])
            except Producto.DoesNotExist:
                raise Http404
            serializer = ProductoSerializer(producto)
        elif 'nombre' in data:
            productos = Producto.objects.filter(nombre__startswith=request.GET['nombre'])
            serializer = ProductoSerializer(productos, many=True)
        else:
            productos = Producto.objects.all()
            serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductoDetail(APIView):

    def get_object(self, pk):
        try:
            return Producto.objects.get(pk=pk)
        except Producto.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        producto = self.get_object(pk)
        serializer = ProductoSerializer(producto)
        return Response(serialzier.data)

    def put(self, request, pk, format=None):
        producto = self.get_object(pk)
        serializer = ProductoSerializer(producto, data=request.data)
        if serializer.is_valid():
            serialzier.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        producto = self.get_object(pk)
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
