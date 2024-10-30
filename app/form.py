from django import forms
from app.models import Celular
from django.core.validators import MinValueValidator

class CelularForm(forms.Form):
    marca = forms.CharField(max_length=20)
    modelo = forms.CharField(max_length=20)
    tiempo_de_uso = forms.IntegerField(validators=[MinValueValidator(0)])
    
class EditarCelularFormulario(CelularForm):
    ...
        
class BuscarCelularForm(forms.Form):
    marca = forms.CharField(max_length=20, required=False)
    modelo = forms.CharField(max_length=20, required=False)