from django.contrib import admin
from .models import Alumno, Catedratico, Curso, Asignacion, CursoAdmin, CatedraticoAdmin, AlumnoAdmin

admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Catedratico, CatedraticoAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Asignacion)
# Register your models here.
