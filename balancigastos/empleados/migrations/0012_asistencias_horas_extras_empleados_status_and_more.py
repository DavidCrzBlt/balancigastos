# Generated by Django 5.1 on 2024-09-23 11:49

import datetime
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0011_alter_asistencias_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='asistencias',
            name='horas_extras',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=4),
        ),
        migrations.AddField(
            model_name='empleados',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='asistencias',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2024, 9, 23, 11, 49, 47, 259562)),
        ),
    ]
