from django import forms
from .models import Proyectos, Ingresos
from django.utils import timezone
from django.core.exceptions import ValidationError

class ProyectosForm(forms.ModelForm):
    class Meta:
        model = Proyectos
        fields = ['proyecto','empresa']

        # widgets = {
        #     'proyecto':forms.TextInput(attrs={
        #         'class': '',
        #         'placeholder':'Nombre del proyecto'
        #     }),
        #     'empresa':forms.TextInput(attrs={
        #         'class': '',
        #         'placeholder':'Nombre de la empresa'
        #     }),
        #     'estatus': forms.Select(attrs={
        #         'class': ''
        #     }),
        #     'total':forms.NumberInput(attrs={
        #         'class': '',
        #         'placeholder': 'Total'
        #     }),
        # }

class IngresosForm(forms.ModelForm):
    class Meta:
        model = Ingresos
        fields = ['concepto','ingreso','referencia','fecha']

        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),  # Calendar widget for 'fecha'
        }

    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha')

        # Check if the date is in the future
        if fecha > timezone.now():
            raise ValidationError('No puedes registrar un gasto con una fecha futura.')

        return fecha