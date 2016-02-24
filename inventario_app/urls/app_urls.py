from django.conf.urls import url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from inventario_app.views.app_views import *

urlpatterns = [
    url(r'^login/$', User_login.as_view(), name='login'),
    url(
        r'^$', 
        login_required(TemplateView.as_view(template_name="index.html")), 
        name='index'),
    url(
        r'^producto/consultar/$', 
        login_required(TemplateView.as_view(template_name="consultar_producto.html")), 
        name='consultar_producto'),
    url(
        r'^producto/registrar/$', 
        Registrar_producto.as_view(), 
        name='registrar_producto'),
    url(
        r'^cliente/registrar/$', 
        login_required(TemplateView.as_view(template_name="registrar_cliente.html")), 
        name='registrar_cliente'),
    url(r'^logout/$', log_out , name="logout"),
    url(
        r'^factura/generar/$', 
        login_required(TemplateView.as_view(template_name="generar_factura.html")), 
        name='generar_factura'),
]
