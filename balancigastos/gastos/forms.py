from django import forms
from .models import Vehiculos, GastosVehiculos, GastosGenerales, GastosEquipos, GastosManoObra, GastosMateriales
from django.utils import timezone
from django.core.exceptions import ValidationError

class VehiculosForm(forms.ModelForm):
    class Meta:
        model = Vehiculos
        fields = ['vehiculo','marca','color','placas','combustible','valor_original']

class GastosVehiculosForm(forms.ModelForm):
    class Meta:
        model = GastosVehiculos
        fields = ['vehiculo','cantidad_combustible','monto','ubicacion','conductor','fecha']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),  # Calendar widget for 'fecha'
        }

    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha')

        # Check if the date is in the future
        if fecha > timezone.now():
            raise ValidationError('No puedes registrar un gasto con una fecha futura.')

        return fecha 

class GastosGeneralesForm(forms.ModelForm):
    class Meta:
        model = GastosGenerales
        fields = ['concepto','comprador','monto_concepto','descripcion','ubicacion','fecha']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),  # Calendar widget for 'fecha'
        }
    
    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha')

        # Check if the date is in the future
        if fecha > timezone.now():
            raise ValidationError('No puedes registrar un gasto con una fecha futura.')

        return fecha
    
class GastosMaterialesForm(forms.ModelForm):
    class Meta:
        model = GastosMateriales
        fields = ['concepto_material','comprador','monto','descripcion','proveedor','fecha']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),  # Calendar widget for 'fecha'
        }

    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha')

        # Check if the date is in the future
        if fecha > timezone.now():
            raise ValidationError('No puedes registrar un gasto con una fecha futura.')

        return fecha 
    
class GastosManoObraForm(forms.ModelForm):
    class Meta:
        model = GastosManoObra
        fields = ['nomina','imss','infonavit','isn','isr','fecha']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),  # Calendar widget for 'fecha'
        }

    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha')

        # Check if the date is in the future
        if fecha > timezone.now():
            raise ValidationError('No puedes registrar un gasto con una fecha futura.')

        return fecha 
    
class GastosEquiposForm(forms.ModelForm):
    class Meta:
        model = GastosEquipos
        fields = ['concepto','comprador','tiempo_renta','monto_concepto','descripcion', 'proveedor','fecha']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),  # Calendar widget for 'fecha'
        }

    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha')

        # Check if the date is in the future
        if fecha > timezone.now():
            raise ValidationError('No puedes registrar un gasto con una fecha futura.')

        return fecha 