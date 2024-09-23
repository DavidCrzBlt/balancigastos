from django.db import models
from django.utils.text import slugify
# Create your models here.

class Proyectos(models.Model):

    proyecto = models.CharField(max_length=255)
    clave_proyecto = models.CharField(max_length=100)
    empresa = models.CharField(max_length=255)
    estatus = models.BooleanField(default=True)
    total = models.FloatField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.proyecto)
        super(Proyectos, self).save(*args, **kwargs)

    def __str__(self):
        return self.proyecto