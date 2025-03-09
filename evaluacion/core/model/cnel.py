from django.db import models

            
class Cnel(models.Model):
    id = models.IntegerField(primary_key=True)
    codigoCuentaAnterior = models.CharField(max_length=255)
    codigoCuentaNuevo = models.CharField(max_length=255)
    cuenAnterior = models.CharField(max_length=255)
    cuenNuevo = models.CharField(max_length=255)
    cuentaContrato = models.CharField(max_length=255)
    cedulaRuc = models.CharField(max_length=255)
    idUnAnterior = models.CharField(max_length=255)
    idUnNueva = models.CharField(max_length=255)
    fechaRegistro = models.DateTimeField()
    unidadNegocio = models.CharField(max_length=255)
    codUnidadNegocio = models.CharField(max_length=255)
    siglasUnidadNegocio = models.CharField(max_length=255)
    interesCondonadoJson = models.CharField(max_length=255)
    mensajeCondonacion = models.CharField(max_length=255)
    correoRegistrado = models.CharField(max_length=255)
    deuda = models.FloatField()
    fechaVencimiento = models.DateTimeField()
    planillasVencidas = models.IntegerField()
    
    def __str__(self):
        return self.cedulaRuc
