from django.db import models
from django.utils.text import slugify
# Create your models here.

class Proyectos(models.Model):

    proyecto = models.CharField(max_length=255)
    empresa = models.CharField(max_length=255)
    estatus = models.BooleanField(default=True)
    total = models.FloatField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.proyecto)
        super(Proyectos, self).save(*args, **kwargs)

    def __str__(self):
        return self.proyecto
    
class Ingresos(models.Model):

    proyecto = models.ForeignKey(Proyectos,related_name='ingresos',on_delete=models.CASCADE)
    concepto = models.CharField(max_length=255,default='')
    ingreso = models.FloatField(default=0)
    referencia = models.CharField(max_length=255,blank=True, default='')
    fecha = models.DateTimeField()

    def __str__(self):
        return self.proyecto.proyecto