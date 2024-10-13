from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render, redirect
from app.models import Celular
from app.form import CelularForm, BuscarCelularForm


def home(request):
    return render(request,'index.html')
    
def crear_celular(request):
    if request.method == 'POST':
        form = CelularForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CelularForm()
    return render(request, 'crear_celular.html', {'form': form})

def buscar_celular(request):
    if request.method == 'GET':
        form = BuscarCelularForm(request.GET)
        if form.is_valid():
            marca = form.cleaned_data['marca']
            modelo = form.cleaned_data['modelo']
            celulares = Celular.objects.filter(marca__icontains=marca, modelo__icontains=modelo)
            return render(request, 'resultado_busqueda.html', {'celulares': celulares, 'marca': marca, 'modelo': modelo})