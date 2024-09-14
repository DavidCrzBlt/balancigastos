from django.contrib import admin
from .models import Vehiculos, GastosVehiculos, GastosGenerales, GastosManoObra, GastosEquipos, GastosMateriales
# Register your models here.

class VehiculosAdmin(admin.ModelAdmin):
    list_display = ['vehiculo','marca','color']

class GastosVehiculosAdmin(admin.ModelAdmin):
    list_display = ['vehiculo','proyecto','monto']

class GastosGeneralesAdmin(admin.ModelAdmin):
    list_display = ['concepto','proyecto','monto_concepto']

class GastosMaterialesAdmin(admin.ModelAdmin):
    list_display = ['concepto_material','proyecto','monto']

class GastosEquiposAdmin(admin.ModelAdmin):
    list_display = ['concepto','proyecto','monto_concepto']

class GastosManoObraAdmin(admin.ModelAdmin):
    list_display = ['proyecto','imss','infonavit','isn','isr','fecha']

admin.site.register(GastosVehiculos,GastosVehiculosAdmin)
admin.site.register(Vehiculos,VehiculosAdmin)
admin.site.register(GastosMateriales,GastosMaterialesAdmin)
admin.site.register(GastosEquipos,GastosEquiposAdmin)
admin.site.register(GastosManoObra,GastosManoObraAdmin)
admin.site.register(GastosGenerales,GastosGeneralesAdmin)
