from django.conf.urls import include, url
from . import views
from django.contrib.auth.views import login,logout


urlpatterns = [
        #url(r'^$', views.listar_asignaciones),
        url(r'^$', login),
        url(r'^ingresarCatedratico/$', views.IngresarCatedratico, name = 'ingresarCatedratico'),
        url(r'^ingresarCurso/$', views.IngresarCurso, name = 'ingresarCurso'),
        url(r'^ingresarAlumno/$', views.IngresarAlumno, name = 'ingresarAlumno'),
        url(r'^ingresarAsignacion/$', views.IngresarAsignacion, name = 'ingresarAsignacion'),

        url(r'^listarAsignaciones/$', views.listar_asignaciones, name = 'listarAsignaciones'),
        url(r'^listarCatedratico/$', views.ListarCatedratico, name = 'listarCatedratico'),
        url(r'^listarCurso/$', views.ListarCurso, name = 'listarCurso'),
        url(r'^listarAlumno/$', views.ListarAlumno , name = 'listarAlumno'),

        url(r'^EditarCatedratico/(?P<pk>[0-9]+)/editar/$', views.EditarCatedratico, name = 'EditarCatedratico'),
        url(r'^EditarCurso/(?P<pk>[0-9]+)/editar/$', views.EditarCurso, name = 'EditarCurso'),
        url(r'^EditarAlumno/(?P<pk>[0-9]+)/editar/$', views.EditarAlumno, name = 'EditarAlumno'),
        url(r'^EditarAsignacion/(?P<pk>[0-9]+)/editar/$', views.EditarAsignacion, name = 'EditarAsignacion'),

        url(r'^eliminarCurso/(?P<pk>[0-9]+)/editar/$', views.EliminarCurso, name = 'EliminarCurso'),
        url(r'^eliminarAlumno/(?P<pk>[0-9]+)/editar/$', views.EliminarAlumno, name = 'EliminarAlumno'),
        url(r'^eliminarCatedratico/(?P<pk>[0-9]+)/editar/$', views.EliminarCatedratico, name = 'EliminarCatedratico'),

        url(r'^accounts/login/$',  login),
        url(r'^accounts/logout/$', logout, name = 'logout' ),

        url(r'^usuario/nuevo/$', views.RegistroUsuario.as_view(), name='nuevo_user'),

        #(r'^post/(?P<pk>[0-9]+)/$', views.asignaciones_detalle)
    ]
