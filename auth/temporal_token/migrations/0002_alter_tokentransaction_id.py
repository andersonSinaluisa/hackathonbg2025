# Generated by Django 5.1.2 on 2024-10-27 02:47

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("temporal_token", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tokentransaction",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
    ]
