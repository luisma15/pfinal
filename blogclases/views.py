from django.shortcuts import render
from django.shortcuts import redirect
from .models import Alumno, Catedratico, Curso, Asignacion
from .forms import ingresarCatedratico
from django.shortcuts import render, get_object_or_404

# Create your views here.
def listar_asignaciones(request):
    #posts = Asignacion.objects.filter(published_date__lte=timezone.now()).order_by('fecha')
    posts = Asignacion.objects.order_by('as_fecha')
    return render(request, 'blogclases/listar_asignaciones.html', {'posts': posts})

def IngresarCatedratico(request):
    if request.method == "POST":
        form = ingresarCatedratico(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.save()
            return render(request, 'blogclases/ingresarCatedratico.html', {'form': form})

    else:
        form = ingresarCatedratico()
    return render(request, 'blogclases/ingresarCatedratico.html', {'form': form})

def ListarCatedratico(request):
    posts = Catedratico.objects.order_by('cat_nombre')
    return render(request, 'blogclases/listar_catedratico.html', {'posts': posts})

def EditarCatedratico(request, pk):
    posts = Catedratico.objects.order_by('cat_nombre')
    post = get_object_or_404(Catedratico, pk = pk)
    if request.method == "POST":
        form = ingresarCatedratico(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.save()
            return redirect ('blogclases.views.ListarCatedratico')
    else:
        form = ingresarCatedratico(instance = post)
    return render(request, 'blogclases/editar_catedratico.html',{'form': form})

#def asignaciones_detalle (request, pk):
    #Post.objects.get(pk=pk)
