from django.shortcuts import render
from django.shortcuts import redirect
from .models import Alumno, Catedratico, Curso, Asignacion
from .forms import ingresarCatedratico, ingresarCurso, ingresarAlumno, ingresarAsignacion, RegistroForm
from django.shortcuts import render, get_object_or_404
from django.contrib import auth

from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy


def EliminarCurso(reques, pk = None):
    instance = get_object_or_404(Curso, pk=pk)
    instance.delete()
    return redirect ('blogclases.views.ListarCurso')

def EliminarAlumno(reques, pk = None):
    instance = get_object_or_404(Alumno, pk=pk)
    instance.delete()
    return redirect ('blogclases.views.ListarAlumno')

def EliminarCatedratico(reques, pk = None):
    instance = get_object_or_404(Catedratico, pk=pk)
    instance.delete()
    return redirect ('blogclases.views.ListarCatedratico')

# Create your views here.
def listar_asignaciones(request):
    #posts = Asignacion.objects.filter(published_date__lte=timezone.now()).order_by('fecha')
    posts = Asignacion.objects.order_by('as_fecha')
    return render(request, 'blogclases/listar_asignaciones.html', {'posts': posts})



def IngresarCatedratico(request):
    if request.method == "POST":
        form = ingresarCatedratico(request.POST or None, request.FILES or None)
        if form.is_valid():
            post = form.save(commit = False)
            post.save()
            return redirect ('blogclases.views.ListarCatedratico')

    else:
        form = ingresarCatedratico()
    return render(request, 'blogclases/ingresarCatedratico.html', {'form': form})

def IngresarCurso(request):
    if request.method == "POST":
        form = ingresarCurso(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.save()
            return redirect ('blogclases.views.ListarCurso')

    else:
        form = ingresarCurso()
    return render(request, 'blogclases/ingresar_curso.html', {'form': form})

def IngresarAlumno(request):
    if request.method == "POST":
        form = ingresarAlumno(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.save()
            return redirect ('blogclases.views.ListarAlumno')

    else:
        form = ingresarAlumno()
    return render(request, 'blogclases/ingresar_alumno.html', {'form': form})

def IngresarAsignacion(request):
    if request.method == "POST":
        form = ingresarAsignacion(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.save()
            return redirect ('blogclases.views.listar_asignaciones')

    else:
        form = ingresarAsignacion()
    return render(request, 'blogclases/ingresarAsignacion.html', {'form': form})

def ListarCatedratico(request):
    posts = Catedratico.objects.order_by('cat_nombre')
    return render(request, 'blogclases/listar_catedratico.html', {'posts': posts})

def ListarCurso(request):
    posts = Curso.objects.order_by('cur_nombre')
    return render(request, 'blogclases/listar_curso.html', {'posts': posts})

def ListarAlumno(request):
    posts = Alumno.objects.order_by('al_nombre')
    return render(request, 'blogclases/listar_alumno.html', {'posts': posts})

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

def EditarCurso(request, pk):
    posts = Curso.objects.order_by('cur_nombre')
    post = get_object_or_404(Curso, pk = pk)
    if request.method == "POST":
        form = ingresarCurso(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.save()
            return redirect ('blogclases.views.ListarCurso')
    else:
        form = ingresarCurso(instance = post)
    return render(request, 'blogclases/editar_curso.html',{'form': form})

def EditarAlumno(request, pk):
    posts = Alumno.objects.order_by('al_nombre')
    post = get_object_or_404(Alumno, pk = pk)
    if request.method == "POST":
        form = ingresarAlumno(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.save()
            return redirect ('blogclases.views.ListarAlumno')
    else:
        form = ingresarAlumno(instance = post)
    return render(request, 'blogclases/editar_alumno.html',{'form': form})

def EditarAsignacion(request, pk):
    posts = Asignacion.objects.order_by('as_fecha')
    post = get_object_or_404(Asignacion, pk = pk)
    if request.method == "POST":
        form = ingresarAsignacion(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.save()
            return redirect ('blogclases.views.listar_asignaciones')
    else:
        form = ingresarAsignacion(instance = post)
    return render(request, 'blogclases/editar_asignacion.html',{'form': form})

def Login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect("/account/loggedin/")
    else:
        # Show an error page
        return redirect('blogclases.views.Login')

def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/account/loggedout/")

class RegistroUsuario(CreateView):
    model = User
    template_name = "blogclases/nuevousuario.html"
    form_class = RegistroForm
    success_url = reverse_lazy('blogclases.views.listar_asignaciones')
