from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.listar_asignaciones),
        url(r'^ingresarCatedratico/$', views.IngresarCatedratico, name = 'ingresar'),
        url(r'^ingresarCurso/$', views.IngresarCurso, name = 'ingresar'),
        url(r'^ingresarAlumno/$', views.IngresarAlumno, name = 'ingresar'),
        url(r'^ingresarAsignacion/$', views.IngresarAsignacion, name = 'ingresar'),

        url(r'^listarCatedratico/$', views.ListarCatedratico, name = 'listar'),
        url(r'^listarCurso/$', views.ListarCurso, name = 'listar'),
        url(r'^listarAlumno/$', views.ListarAlumno , name = 'listar'),

        url(r'^EditarCatedratico/(?P<pk>[0-9]+)/editar/$', views.EditarCatedratico, name = 'EditarCatedratico'),
        url(r'^EditarCurso/(?P<pk>[0-9]+)/editar/$', views.EditarCurso, name = 'EditarCurso'),
        url(r'^EditarAlumno/(?P<pk>[0-9]+)/editar/$', views.EditarAlumno, name = 'EditarAlumno'),
        url(r'^EditarAsignacion/(?P<pk>[0-9]+)/editar/$', views.EditarAsignacion, name = 'EditarAsignacion'),
        #(r'^post/(?P<pk>[0-9]+)/$', views.asignaciones_detalle)
    ]
