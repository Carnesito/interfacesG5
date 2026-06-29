from django.db import models

# Create your models here.

class Medicina(models.Model):
    nombre_medicina = models.CharField(max_length=100)
    precio_medicina = models.DecimalField(max_digits=10, decimal_places=2)
    stock_medicina = models.IntegerField()
    estado_medicina = models.CharField(max_length=20, default='Disponible')

    def __str__(self):
        return self.nombre_medicina
    