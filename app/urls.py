from django.urls import path
from app.views import home, crear_celular

urlpatterns = [
    path('', home),
    path('crear-celular/', crear_celular)
    
    
]
