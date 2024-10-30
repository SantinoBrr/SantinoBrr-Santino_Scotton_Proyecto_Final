from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login as django_login
from usuarios.form import FormularioDeCreacionDeUsuario, FormularioEdicionPerfil
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from usuarios.models import DatosExtra

def login(request):
    
    formulario = AuthenticationForm()
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            
            django_login(request, usuario)
            
            DatosExtra.objects.get_or_create(user=usuario)
            
            return redirect('app:home')
    
    return render(request, 'usuarios/login.html', {'form': formulario})


def register(request):
    formulario = FormularioDeCreacionDeUsuario()
    if request.method == 'POST':
        formulario = FormularioDeCreacionDeUsuario(request.POST)
        if formulario.is_valid():
            user = formulario.save()
            # Crear el objeto DatosExtra para el nuevo usuario
            DatosExtra.objects.create(user=user)  # Se crea una instancia vacía de DatosExtra
            return redirect('usuarios:login')
    
    return render(request, 'usuarios/register.html', {'form': formulario})


@login_required
def editar_perfil(request):
    datos_extra = request.user.datosextra
    formulario = FormularioEdicionPerfil(instance=request.user)

    if request.method == "POST":
        formulario = FormularioEdicionPerfil(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            # Guardar los cambios del usuario
            formulario.save()
            # Manejar el avatar
            new_avatar = request.FILES.get('avatar')
            if new_avatar:
                datos_extra.avatar = new_avatar
            datos_extra.save()
            
            return redirect('app:home')

    return render(request, 'usuarios/editar_perfil.html', {'form': formulario})

class CambiarPassword(LoginRequiredMixin, PasswordChangeView):
    template_name = 'usuarios/cambiar_password.html'
    success_url = reverse_lazy('usuarios:editar_perfil')