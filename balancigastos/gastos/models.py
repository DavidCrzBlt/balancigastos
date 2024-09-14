from django.db import models
from proyectos.models import Proyectos
from django.utils import timezone

# Create your models here.

class Vehiculos(models.Model):

    TIPO_COMBUSTIBLE = [
        ('GASOLINE','Gasolina'),
        ('DIESEL','Diesel'),
        ('ELECTRIC','Eléctrico')
    ]

    vehiculo = models.CharField(max_length=255)
    marca = models.CharField(max_length=80,default='')
    color = models.CharField(max_length=80,default='')
    placas = models.CharField(max_length=60)
    combustible = models.CharField(max_length=30,choices=TIPO_COMBUSTIBLE,default='GASOLINE')
    valor_original = models.FloatField()

    def __str__(self):
        return self.vehiculo

class GastosVehiculos(models.Model):
    
    proyecto = models.ForeignKey(Proyectos, related_name= 'gastos_vehiculos',on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculos, related_name='vehiculos',on_delete=models.CASCADE)
    cantidad_combustible = models.FloatField()
    monto = models.FloatField()
    ubicacion = models.CharField(max_length=255)
    conductor = models.CharField(max_length=255)
    fecha = models.DateTimeField()
    
class GastosGenerales(models.Model):
    proyecto = models.ForeignKey(Proyectos, related_name= 'gastos_generales',on_delete=models.CASCADE)
    concepto = models.CharField(max_length=255)
    comprador = models.CharField(max_length=255,default='')
    monto_concepto = models.FloatField()
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=80)
    fecha = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f"{self.proyecto.proyecto} - {self.concepto}"
    
class GastosMateriales(models.Model):
    proyecto = models.ForeignKey(Proyectos, related_name= 'gastos_materiales',on_delete=models.CASCADE)
    concepto_material = models.CharField(max_length=255)
    comprador = models.CharField(max_length=255,default='')
    monto = models.FloatField()
    descripcion = models.TextField()
    proveedor = models.CharField(max_length=80)
    fecha = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f"{self.proyecto.proyecto} - {self.concepto_material}"
    
class GastosManoObra(models.Model):
    proyecto = models.ForeignKey(Proyectos, related_name= 'gastos_mano_obra',on_delete=models.CASCADE)
    nomina = models.FloatField()
    imss = models.FloatField()
    infonavit = models.FloatField()
    isn = models.FloatField()
    isr = models.FloatField()
    monto = models.FloatField(default=0)
    fecha = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f"{self.proyecto.proyecto}"
    
class GastosEquipos(models.Model):

    TIEMPO_RENTA = [
        ('RENTA_MENSUAL','renta mensual'),
        ('RENTA_SEMANAL','renta semanal'),
        ('RENTA_DIARIA','renta diaria'),
        ('PROPIEDAD','Propiedad')
    ]

    proyecto = models.ForeignKey(Proyectos, related_name= 'gastos_equipos',on_delete=models.CASCADE)
    concepto = models.CharField(max_length=255)
    comprador = models.CharField(max_length=255,default='')
    tiempo_renta = models.CharField(max_length=100,choices=TIEMPO_RENTA,default='RENTA_MENSUAL')
    monto_concepto = models.FloatField()
    descripcion = models.TextField()
    proveedor = models.CharField(max_length=80)
    fecha = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f"{self.proyecto.proyecto} - {self.concepto}"