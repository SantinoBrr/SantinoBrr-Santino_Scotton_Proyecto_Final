from django.urls import path
from app.views import home, crear_celular, buscar_celular, aboutme, ver_celular,eliminar_celular, editar_celular

app_name = 'app'

urlpatterns = [
    path('', home, name='home'),
    path('crear-celular/', crear_celular, name='crear_celular'),
    path('buscar-celular/', buscar_celular, name='buscar_celular'),
    path('about-me/', aboutme, name='about_me'),
    path('ver-celular/<int:id>/', ver_celular, name= 'ver_celular'),
    path('eliminar-celular/<int:id>/', eliminar_celular, name= 'eliminar_celular'),
    path('editar-celular/<int:id>/', editar_celular, name= 'editar_celular'),
]
