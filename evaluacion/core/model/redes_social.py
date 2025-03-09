from django.db import models



class RedesSocial(models.Model):
    cedula = models.CharField(max_length=10)
    reputacion_en_redes = models.DecimalField(max_digits=3, decimal_places=2)
    referencias_compras_largo_plazo = models.BooleanField()
    interaccion_con_contenido_financiero = models.BooleanField()
    categoria_gasto = models.CharField(max_length=50)
    presencia_articulos_lujo = models.BooleanField()
    frecuencia_publicaciones_ambientes_falsos = models.BooleanField()
    nivel_edicion_fotos = models.CharField(max_length=50)
    aparicion_situaciones_riesgo = models.BooleanField()

    def __str__(self):
        return self.cedula