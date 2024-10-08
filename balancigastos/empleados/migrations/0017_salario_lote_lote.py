# Generated by Django 5.1 on 2024-09-26 14:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0016_remove_salario_asistencias_and_more'),
        ('proyectos', '0005_alter_proyectos_clave_proyecto'),
    ]

    operations = [
        migrations.AddField(
            model_name='salario',
            name='lote',
            field=models.IntegerField(default=1, editable=False),
        ),
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado_en', models.DateTimeField(auto_now_add=True)),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lotes', to='proyectos.proyectos')),
            ],
        ),
    ]
