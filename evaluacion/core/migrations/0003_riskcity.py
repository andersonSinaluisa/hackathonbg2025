# Generated by Django 5.1.7 on 2025-03-09 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_redessocial"),
    ]

    operations = [
        migrations.CreateModel(
            name="RiskCity",
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
                ("city", models.CharField(max_length=50)),
                ("risk", models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
    ]
