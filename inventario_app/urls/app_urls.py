from django.conf.urls import url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from inventario_app.views.app_views import *

urlpatterns = [
    url(r'^login/$', User_login.as_view(), name='login'),
    url(
        r'^$', 
        index_view, 
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
        RegistrarCliente.as_view(), 
        name='registrar_cliente'),
    url(r'^logout/$', log_out , name="logout"),
    url(
        r'^factura/generar/$', 
        login_required(TemplateView.as_view(template_name="generar_factura.html")), 
        name='generar_factura'),
    url(
        r'^factura/consultar/$', 
        login_required(TemplateView.as_view(template_name="consultar_factura.html")), 
        name='consultar_factura'),
    url(
        r'^cliente/consultar$', 
        login_required(TemplateView.as_view(template_name="consultar_cliente.html")), 
        name='consultar_cliente'),
    url(
        r'^cliente/registrar/$', 
        login_required(TemplateView.as_view(template_name="registrar_cliente.html")), 
        name='registrar_usuario'),
    url(
        r'^reporte/generar/$', 
        login_required(TemplateView.as_view(template_name="generar_reporte.html")), 
        name='generar_reporte'),
    url(
        r'^empleado/registrar/$', Registrar_Empleado.as_view(), name='registrar_empleado'),
]
