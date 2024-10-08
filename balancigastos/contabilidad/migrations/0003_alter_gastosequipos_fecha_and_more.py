# Generated by Django 5.1 on 2024-09-22 19:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0002_alter_gastosequipos_fecha_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gastosequipos',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2024, 9, 22, 19, 49, 51, 407709, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='gastosgenerales',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2024, 9, 22, 19, 49, 51, 407709, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='gastosmanoobra',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2024, 9, 22, 19, 49, 51, 407709, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='gastosmateriales',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2024, 9, 22, 19, 49, 51, 407709, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='gastosseguridad',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2024, 9, 22, 19, 49, 51, 407709, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='gastosvehiculos',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2024, 9, 22, 19, 49, 51, 407709, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='ingresos',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2024, 9, 22, 19, 49, 51, 407709, tzinfo=datetime.timezone.utc)),
        ),
    ]
