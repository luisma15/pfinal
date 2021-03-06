
from django.db import models
from django.contrib import admin
from django.utils import timezone
# Create your models here.

class Catedratico(models.Model):
    cat_nombre = models.CharField(max_length = 20)
    cat_apellido = models.CharField(max_length = 20)
    cat_genero = models.CharField(max_length = 9)
    cat_edad = models.CharField(max_length = 2)
    cat_telefono = models.CharField(max_length = 8)
    #campo de imagen
    cat_imagen = models.ImageField(upload_to='media/Fotos/', null = True, blank = True)

    def __str__(self):
        return self.cat_nombre

#@receiver (post_delete, sender = Catedratico)
#def

class Curso(models.Model):
    cur_nombre = models.CharField(max_length = 15)
    cur_creditos = models.CharField(max_length = 2)

    def __str__(self):
        return self.cur_nombre

class Alumno(models.Model):
    al_nombre = models.CharField(max_length = 20)
    al_apellido = models.CharField(max_length = 20)
    al_edad = models.CharField(max_length = 2)
    al_cursos = models.ManyToManyField(Curso, through = 'Asignacion')

    def __str__(self):
        return self.al_nombre

class Asignacion(models.Model):
    as_fecha = models.DateField(default = timezone.now)
    as_aula = models.CharField(max_length = 5)
    as_catedratico = models.ForeignKey(Catedratico,on_delete=models.CASCADE)
    as_alumno = models.ForeignKey(Alumno,on_delete=models.CASCADE)
    as_curso = models.ForeignKey(Curso,on_delete=models.CASCADE)

#class AsignacionInLine(admin.TabularInline):
    #model=Asignacion
#    extra=1

#class CursoAdmin(admin.ModelAdmin):
#    inlines = (AsignacionInLine,)

#class AlumnoAdmin(admin.ModelAdmin):
#    inlines = (AsignacionInLine,)

#class CatedraticoAdmin(admin.ModelAdmin):
#    inlines = (AsignacionInLine,)
