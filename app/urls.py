from django.urls import path
from app.views import home, crear_celular, buscar_celular, aboutme

app_name = 'app'

urlpatterns = [
    path('', home, name='home'),
    path('crear-celular/', crear_celular, name='crear_celular'),
    path('buscar-celular/', buscar_celular, name='buscar_celular'),
     path('about-me/', aboutme, name='about_me'), 
]
