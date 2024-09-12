from django.contrib import admin
from .models import Vehiculos, GastosVehiculos
# Register your models here.

class VehiculosAdmin(admin.ModelAdmin):
    list_display = ['vehiculo','marca','color']

class GastosVehiculosAdmin(admin.ModelAdmin):
    list_display = ['vehiculo','proyecto','monto']

admin.site.register(GastosVehiculos,GastosVehiculosAdmin)
admin.site.register(Vehiculos,VehiculosAdmin)