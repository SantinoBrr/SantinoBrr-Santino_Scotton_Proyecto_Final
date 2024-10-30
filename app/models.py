from django.db import models
from django.core.validators import MinValueValidator

class Celular(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    tiempo_de_uso = models.IntegerField(validators=[MinValueValidator(0)])
    def __str__(self):
        return f'{self.marca} {self.modelo} '
