from django.conf.urls import url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from inventario_app.views.app_views import *

urlpatterns = [
    url(r'^login/$', user_login, name='login'),
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
        login_required(TemplateView.as_view(template_name="registrar_producto.html")), 
        name='registrar_producto'),
    url(
        r'^cliente/registrar/$', 
        login_required(TemplateView.as_view(template_name="registrar_cliente.html")), 
        name='registrar_cliente'),
]
