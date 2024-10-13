from django import forms
from app.models import Celular

class CelularForm(forms.ModelForm):
    marca = forms.CharField(max_length=20)
    modelo = forms.CharField(max_length=20)
    tiempo_de_uso = forms.IntegerField(help_text="Tiempo de uso en meses")
        
class BuscarCelularForm(forms.Form):
    marca = forms.CharField(max_length=20, required=False)
    modelo = forms.CharField(max_length=20, required=False)