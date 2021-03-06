from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from inventario_app.views.api_views import ProductoList, ProductoDetail

urlpatterns = [
    url(r'^productos/$' , ProductoList.as_view()),
    url(r'^producto/(?P<pk>[0-9]+)/$', ProductoDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
