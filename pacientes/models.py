from django.db import models

class Paciente(models.Model):
    nombre_completo = models.CharField(max_length=200)
    cedula = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    correo = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nombre_completo
