from django.db import models
from proyectos.models import Proyectos
from django.utils import timezone
from decimal import Decimal

# Create your models here.

class Empleados(models.Model):
    nombres = models.CharField(max_length=255,null=False)
    apellido_paterno = models.CharField(max_length=255,null=False)
    apellido_materno = models.CharField(max_length=255,null=False)
    rfc = models.CharField(max_length=100,null=False)
    infonavit = models.BooleanField(default=False)
    imss = models.BooleanField(default=False)
    status = models.BooleanField(default=True)

class Asistencias(models.Model):
    empleado = models.ForeignKey(Empleados,related_name="asistencias",on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyectos,related_name="asistencias",on_delete=models.CASCADE)
    asistencias = models.BooleanField(default=True,null=False)
    horas_extras = models.DecimalField(max_digits=4, decimal_places=2,null=False,default=Decimal('0.00'))
    fecha = models.DateField(default=timezone.now,null=False)

    def __str__(self):
        return self.empleado

class Salario(models.Model):
    empleado = models.ForeignKey(Empleados,related_name="salario",on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyectos,related_name="salario",on_delete=models.CASCADE)
    asistencias = models.ForeignKey(Asistencias,related_name="salario",on_delete=models.CASCADE)
    salario_base = models.DecimalField(max_digits=10, decimal_places=2,null=False,default=Decimal('0.00'))
    salario = models.DecimalField(max_digits=10, decimal_places=2,null=False,default=Decimal('0.00'))
    infonavit = models.DecimalField(max_digits=10, decimal_places=2,null=False,default=Decimal('0.00'))
    imss = models.DecimalField(max_digits=10, decimal_places=2,null=False,default=Decimal('0.00'))
    isn = models.DecimalField(max_digits=10, decimal_places=2,null=False,default=Decimal('0.00'))
    horas_extras = models.DecimalField(max_digits=10, decimal_places=2,null=False,default=Decimal('0.00'))
    