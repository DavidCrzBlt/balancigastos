# Generated by Django 5.1 on 2024-09-22 20:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0003_alter_asistencias_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asistencias',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2024, 9, 22, 20, 0, 3, 999298)),
        ),
        migrations.AlterField(
            model_name='salario',
            name='imss',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='salario',
            name='infonavit',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='salario',
            name='isn',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='salario',
            name='salario',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
