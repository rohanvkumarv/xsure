# Generated by Django 5.0 on 2023-12-19 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_tempfile_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='allow_without_pay',
            field=models.BooleanField(default=False),
        ),
    ]
