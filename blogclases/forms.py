from django import forms
from .models import Catedratico, Curso, Alumno, Asignacion
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class ingresarCatedratico(forms.ModelForm):
    class  Meta:
        model = Catedratico
        fields = ('cat_nombre', 'cat_apellido', 'cat_edad', 'cat_genero', 'cat_telefono', 'cat_imagen')

class ingresarCurso(forms.ModelForm):
    class  Meta:
        model = Curso
        fields = ('cur_nombre', 'cur_creditos')

class ingresarAlumno(forms.ModelForm):
    class  Meta:
        model = Alumno
        fields = ('al_nombre', 'al_apellido', 'al_edad')

class ingresarAsignacion(forms.ModelForm):
    class Meta:
        model = Asignacion
        fields = ('as_aula', 'as_catedratico', 'as_curso', 'as_alumno')

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
                'username',
                'first_name',
                'last_name',
                'email',
            ]
        labels = {
                'username': 'Nombre de usuario',
                'first_name': 'Nombre',
                'last_name': 'Apellidos',
                'email': 'Correo',
        }
