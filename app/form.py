from django import forms
from app.models import Celular

class CelularForm(forms.Form):
    marca = forms.CharField(max_length=20)
    modelo = forms.CharField(max_length=20)
    tiempo_de_uso = forms.IntegerField()
        
class BuscarCelularForm(forms.Form):
    marca = forms.CharField(max_length=20, required=False)
    modelo = forms.CharField(max_length=20, required=False)