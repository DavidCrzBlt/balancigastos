from django.test import TestCase
from django.utils import timezone
from .forms import GastosGeneralesForm
from .models import Proyectos, GastosGenerales

# Create your tests here.

class GastosGeneralesFormTest(TestCase):

    def setUp(self):
        # Create a test project
        self.proyecto = Proyectos.objects.create(nombre="Proyecto de Prueba", slug="proyecto-de-prueba")

    def test_gastos_generales_fecha_futura(self):
        # Try to submit a form with a future date
        future_date = timezone.now() + timezone.timedelta(days=1)
        form_data = {
            'proyecto': self.proyecto.id,
            'concepto': 'Test Concepto',
            'comprador': 'Test Comprador',
            'monto_concepto': 1000,
            'descripcion': 'Test Descripción',
            'ubicacion': 'Test Ubicación',
            'fecha': future_date,
        }

        form = GastosGeneralesForm(data=form_data)
        self.assertFalse(form.is_valid())  # The form should not be valid
        self.assertIn('fecha', form.errors)  # 'fecha' should have an error
        self.assertEqual(form.errors['fecha'], ['No puedes registrar un gasto con una fecha futura.'])

    def test_gastos_generales_fecha_valida(self):
        # Try to submit a form with a valid (past or current) date
        valid_date = timezone.now()
        form_data = {
            'proyecto': self.proyecto.id,
            'concepto': 'Test Concepto',
            'comprador': 'Test Comprador',
            'monto_concepto': 1000,
            'descripcion': 'Test Descripción',
            'ubicacion': 'Test Ubicación',
            'fecha': valid_date,
        }

        form = GastosGeneralesForm(data=form_data)
        self.assertTrue(form.is_valid())  # The form should be valid
