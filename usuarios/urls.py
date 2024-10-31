from django.urls import path
from usuarios import views
from django.contrib.auth.views import LogoutView


app_name = 'usuarios'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('perfil/editar/password/', views.CambiarPassword.as_view(), name='cambiar_password'),
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
    path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
]
