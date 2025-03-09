from django.db import models
from core.models.prospect import Prospect

class FinancialInformation(models.Model):
    prospect = models.OneToOneField(Prospect, on_delete=models.CASCADE, related_name="informacion_financiera")
    ingresos_mensuales = models.DecimalField(max_digits=10, decimal_places=2)
    cargas_familiares = models.IntegerField()
    gastos_mensuales = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_trabajo = models.CharField(max_length=255)
    actividad_economica = models.CharField(max_length=255)
    anos_en_puesto = models.IntegerField()

    def __str__(self):
        return f"{self.prospect.nombres} - {self.ingresos_mensuales} USD"