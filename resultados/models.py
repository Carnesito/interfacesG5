from django.db import models
from citas.models import Cita
from medicinas.models import Medicina

class Resultado(models.Model):
    cita = models.OneToOneField(Cita, on_delete=models.CASCADE)
    diagnostico = models.TextField()
    indicaciones = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Resultado de la Cita #{self.cita.id} - {self.cita.paciente}"

class DetalleResultadoMedicina(models.Model):
    resultado = models.ForeignKey(Resultado, on_delete=models.CASCADE, related_name='detalles_medicamentos')
    medicina = models.ForeignKey(Medicina, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    dosis = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.cantidad}x {self.medicina.nombre_medicina} para Resultado #{self.resultado.id}"
