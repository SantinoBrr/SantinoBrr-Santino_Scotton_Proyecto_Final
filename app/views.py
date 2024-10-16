from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render, redirect
from app.models import Celular
from app.form import CelularForm, BuscarCelularForm


def home(request):
    return render(request,'index.html')
    
def crear_celular(request):
    if request.method == "POST":
        form = CelularForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # Crear el objeto Celular con los datos del formulario
            celular = Celular(
                marca=data.get("marca"),
                modelo=data.get("modelo"),
                tiempo_de_uso=data.get("tiempo_de_uso")
            )
            celular.save()
            form = CelularForm()
    else:
        form = CelularForm()

    # Renderizar la plantilla con el formulario
    return render(request, 'crear_celular.html', {'form': form})


def buscar_celular(request):
    form = BuscarCelularForm(request.GET)
    celulares = Celular.objects.all()

    if form.is_valid():
        marca = form.cleaned_data['marca']
        modelo = form.cleaned_data['modelo']
        
        # Filtrado
        if marca or modelo:
            celulares = celulares.filter(marca__icontains=marca, modelo__icontains=modelo)

    return render(request, 'buscar_celular.html', {'celulares': celulares, 'form': form})

def aboutme(request):
    return render(request,'about_me.html')