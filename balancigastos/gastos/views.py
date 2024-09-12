from typing import Any
from django.shortcuts import render, redirect
from .forms import VehiculosForm, GastosVehiculosForm, GastosGeneralesForm
from django.views.generic import ListView
from .models import Vehiculos, GastosVehiculos, GastosGenerales
from proyectos.models import Proyectos
from django.db.models import Sum, F
# Create your views here.

class GastosVehiculosListView(ListView):
    model = GastosVehiculos
    template_name = "gastos/gastos_vehiculos_list.html"

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        proyecto = Proyectos.objects.get(slug=slug)
        return GastosVehiculos.objects.filter(proyecto=proyecto)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        proyecto = Proyectos.objects.get(slug=slug)

        # Calculate total monto using aggregate
        total_monto = GastosVehiculos.objects.filter(proyecto=proyecto).aggregate(total=Sum('monto'))['total'] or 0

        # Add the total to the context
        context['total_monto'] = total_monto
        context['proyecto'] = proyecto
        return context

class GastosGeneralesListView(ListView):
    model = GastosGenerales
    template_name = "gastos/gastos_generales_list.html"

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        proyecto = Proyectos.objects.get(slug=slug)
        return GastosGenerales.objects.filter(proyecto=proyecto)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        proyecto = Proyectos.objects.get(slug=slug)

        # Calculate total monto using aggregate
        total_monto = GastosGenerales.objects.filter(proyecto=proyecto).aggregate(total=Sum('monto_concepto'))['total'] or 0

        # Add the total to the context
        context['total_monto'] = total_monto
        context['proyecto'] = proyecto
        return context 

def registro_vehiculos(request):

    vehiculos = Vehiculos.objects.all()

    if request.method == "POST":
        vehiculos_form = VehiculosForm(request.POST)

        if vehiculos_form.is_valid():
            vehiculos_form.save()
            return redirect('gastos:registro_vehiculos')
    else:
        vehiculos_form = VehiculosForm()

    return render(request,'gastos/registrar_vehiculo.html',{'vehiculos_form':vehiculos_form,'vehiculos':vehiculos})

def registro_gastos_vehiculos(request,slug):

    proyecto = Proyectos.objects.get(slug=slug)
    
    if request.method == "POST":
        gastos_vehiculos_form = GastosVehiculosForm(request.POST)

        if gastos_vehiculos_form.is_valid():
            gasto_vehiculo = gastos_vehiculos_form.save(commit=False)
            gasto_vehiculo.proyecto = proyecto
            gasto_vehiculo.save()

            # Actualizar el valor neto del proyecto restando el monto del gasto
            Proyectos.objects.filter(id=proyecto.id).update(total=F('total') - gasto_vehiculo.monto)

            return redirect('gastos:gastos_vehiculos', slug=slug)
    else:
        gastos_vehiculos_form = GastosVehiculosForm()

    return render(request,'gastos/registro_gastos_vehiculos.html',{'gastos_vehiculos_form':gastos_vehiculos_form,'proyecto':proyecto})

def registro_gastos_generales(request, slug):

    proyecto = Proyectos.objects.get(slug=slug)
    
    if request.method == "POST":
        gastos_generales_form = GastosGeneralesForm(request.POST)

        if gastos_generales_form.is_valid():
            gasto_general = gastos_generales_form.save(commit=False)
            gasto_general.proyecto = proyecto
            gasto_general.save()

            # Actualizar el valor neto del proyecto restando el monto del gasto
            Proyectos.objects.filter(id=proyecto.id).update(total=F('total') - gasto_general.monto_concepto)

            return redirect('gastos:gastos_generales',slug=slug)
    else:
        gastos_generales_form = GastosGeneralesForm()

    return render(request,'gastos/registrar_gastos_generales.html',{'gastos_generales_form':gastos_generales_form,'proyecto':proyecto})
