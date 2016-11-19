from django import forms
from .models import Catedratico

class ingresarCatedratico(forms.ModelForm):
    class  Meta:
        model = Catedratico
        fields = ('cat_nombre', 'cat_apellido', 'cat_edad', 'cat_genero', 'cat_telefono')
