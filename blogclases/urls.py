from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.listar_asignaciones),
        url(r'^ingresarCatedratico/$', views.IngresarCatedratico, name = 'ingresar'),
        url(r'^listarCatedratico/$', views.ListarCatedratico, name = 'listar'),
        url(r'^EditarCatedratico/(?P<pk>[0-9]+)/editar/$', views.EditarCatedratico, name = 'EditarCatedratico'),
        #(r'^post/(?P<pk>[0-9]+)/$', views.asignaciones_detalle)
    ]
