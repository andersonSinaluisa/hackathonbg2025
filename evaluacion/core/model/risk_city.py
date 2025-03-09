from django.db import models

class RiskCity(models.Model):
    city = models.CharField(max_length=50)
    risk = models.DecimalField(max_digits=3, decimal_places=2)
    
    def __str__(self):
        return self.city