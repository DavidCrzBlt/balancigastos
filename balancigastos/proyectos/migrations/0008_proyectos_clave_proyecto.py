# Generated by Django 5.1 on 2024-09-21 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0007_ingresos_concepto_ingresos_referencia'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyectos',
            name='clave_proyecto',
            field=models.CharField(blank=True, default='pro', max_length=80),
        ),
    ]
