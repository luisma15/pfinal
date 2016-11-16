from django.shortcuts import render
from django.utils import timezone
from .models import Alumno, Catedratico, Curso, Asignacion

# Create your views here.
def listar_asignaciones(request):
    #posts = Asignacion.objects.filter(published_date__lte=timezone.now()).order_by('fecha')
    posts = Asignacion.objects.order_by('as_fecha')
    return render(request, 'blogclases/listar_asignaciones.html', {'posts': posts})
