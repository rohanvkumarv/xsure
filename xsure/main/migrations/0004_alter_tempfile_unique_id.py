# Generated by Django 5.0 on 2023-12-18 13:26

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_tempfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tempfile',
            name='unique_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
