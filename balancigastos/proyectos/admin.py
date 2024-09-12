from django.contrib import admin
from .models import Proyectos
# Register your models here.

class ProyectosAdmin(admin.ModelAdmin):
    list_display = ['proyecto','empresa','estatus','total']

admin.site.register(Proyectos,ProyectosAdmin)

