# Generated by Django 5.0 on 2023-12-18 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_lancer_projects'),
    ]

    operations = [
        migrations.CreateModel(
            name='TempFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/')),
                ('unique_id', models.CharField(max_length=100, unique=True)),
            ],
        ),
    ]