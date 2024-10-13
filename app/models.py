from django.db import models

class Celular(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    tiempo_de_uso = models.IntegerField(help_text="Tiempo de uso en meses")
    def __str__(self):
        return f'{self.marca} {self.modelo} {self.tiempo_de_uso}'
