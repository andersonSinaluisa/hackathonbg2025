# Generated by Django 5.1.7 on 2025-03-09 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="RedesSocial",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cedula", models.CharField(max_length=10)),
                (
                    "reputacion_en_redes",
                    models.DecimalField(decimal_places=2, max_digits=3),
                ),
                ("referencias_compras_largo_plazo", models.BooleanField()),
                ("interaccion_con_contenido_financiero", models.BooleanField()),
                ("categoria_gasto", models.CharField(max_length=50)),
                ("presencia_articulos_lujo", models.BooleanField()),
                ("frecuencia_publicaciones_ambientes_falsos", models.BooleanField()),
                ("nivel_edicion_fotos", models.CharField(max_length=50)),
                ("aparicion_situaciones_riesgo", models.BooleanField()),
            ],
        ),
    ]
