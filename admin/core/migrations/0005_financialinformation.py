# Generated by Django 5.1.7 on 2025-03-09 13:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20250309_0800'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinancialInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingresos_mensuales', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cargas_familiares', models.IntegerField()),
                ('gastos_mensuales', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tipo_trabajo', models.CharField(max_length=255)),
                ('actividad_economica', models.CharField(max_length=255)),
                ('anos_en_puesto', models.IntegerField()),
                ('prospect', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='informacion_financiera', to='core.prospect')),
            ],
        ),
    ]
