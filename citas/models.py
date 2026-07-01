from django.db import models
from django.contrib.auth.models import User
from pacientes.models import Paciente
from especialidades.models import Especialidad

class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    motivo_consulta = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=20, default='Pendiente') # Pendiente, En curso, Finalizada, Cancelada

    def __str__(self):
        return f"Cita de {self.paciente} con Dr. {self.doctor.username} - {self.fecha} {self.hora}"
