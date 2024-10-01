from django.contrib import admin
from .models import Empleados, Salario, Asistencias
# Register your models here.

class EmpleadosAdmin(admin.ModelAdmin):
    list_display = [
        'nombres',
        'apellido_paterno',
        'apellido_materno',
        'rfc',
        'infonavit',
        'imss',
        'status'
    ]

class SalarioAdmin(admin.ModelAdmin):
    list_display = [
        'empleado',
        'proyecto',
        'salario',
        'infonavit',
        'imss',
        'isr',
        'horas_extras',
        'lote'
    ]

class AsistenciasAdmin(admin.ModelAdmin):
    list_display = [
        'get_empleado_rfc',
        'proyecto',
        'asistencias',
        'horas_extras',
        'fecha'
    ]
    def get_empleado_rfc(self, obj):
        return obj.empleado.rfc  # Devuelve el RFC del empleado
    get_empleado_rfc.short_description = 'RFC Empleado'  # Nombre de la columna en el admin

admin.site.register(Empleados,EmpleadosAdmin)
admin.site.register(Asistencias,AsistenciasAdmin)
admin.site.register(Salario,SalarioAdmin)