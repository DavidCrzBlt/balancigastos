from django.db import models
from proyectos.models import Proyectos
from django.utils import timezone

# Create your models here.

class Empleados(models.Model):
    nombres = models.CharField(max_length=255,null=False)
    apellido_paterno = models.CharField(max_length=255,null=False)
    apellido_materno = models.CharField(max_length=255,null=False)
    rfc = models.CharField(max_length=100,null=False)
    infonavit = models.BooleanField(default=False)
    imss = models.BooleanField(default=False)

class Asistencias(models.Model):
    empleado = models.ForeignKey(Empleados,related_name="asistencias",on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyectos,related_name="asistencias",on_delete=models.CASCADE)
    asistencias = models.BooleanField(default=True,null=False)
    fecha = models.DateField(default=timezone.now(),null=False)

    def __str__(self):
        return self.empleado

class Salario(models.Model):
    empleado = models.ForeignKey(Empleados,related_name="salario",on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyectos,related_name="salario",on_delete=models.CASCADE)
    asistencias = models.ForeignKey(Asistencias,related_name="salario",on_delete=models.CASCADE)
    salario = models.DecimalField(max_digits=10, decimal_places=2,null=False)
    infonavit = models.DecimalField(max_digits=10, decimal_places=2,null=False)
    imss = models.DecimalField(max_digits=10, decimal_places=2,null=False)
    isn = models.DecimalField(max_digits=10, decimal_places=2,null=False)
    