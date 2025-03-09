from django.db import models

from .base_model import BaseModel



from django.db import models
class Prospect(models.Model):
    cedula = models.CharField(max_length=10, primary_key=True)
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    ciudadania = models.CharField(max_length=255)
    fechaNacimiento = models.DateField()
    estadoCivil = models.CharField(max_length=255)
    profesion = models.CharField(max_length=255)
    nivelEstudios = models.CharField(max_length=255)
    esCliente = models.BooleanField()
    tipoPersona = models.CharField(max_length=255)
    score = models.ForeignKey('ScoreHistory', null=True, blank=True, on_delete=models.CASCADE)