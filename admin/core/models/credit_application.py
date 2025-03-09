from django.db import models
from core.models.prospect import Prospect

class CreditApplication(models.Model):
    prospect = models.ForeignKey(Prospect, on_delete=models.CASCADE, related_name="credit_applications")
    monto_solicitado = models.DecimalField(max_digits=10, decimal_places=2)
    plazo = models.IntegerField()
    fecha = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=255, default="En revisión")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.prospect.nombres} - {self.monto_solicitado} USD - {self.plazo} meses"
