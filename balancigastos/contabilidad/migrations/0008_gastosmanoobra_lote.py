# Generated by Django 5.1 on 2024-09-29 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0007_gastosmanoobra_horas_extras'),
    ]

    operations = [
        migrations.AddField(
            model_name='gastosmanoobra',
            name='lote',
            field=models.IntegerField(default=1, editable=False),
        ),
    ]
