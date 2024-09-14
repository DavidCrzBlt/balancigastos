from django.shortcuts import render, redirect
from .forms import VehiculosForm, GastosVehiculosForm, GastosGeneralesForm, GastosMaterialesForm, GastosManoObraForm, GastosEquiposForm
from django.views.generic import ListView
from .models import Vehiculos, GastosVehiculos, GastosGenerales, GastosMateriales, GastosManoObra, GastosEquipos
from proyectos.models import Proyectos
from django.db.models import Sum, F
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class GastosVehiculosListView(LoginRequiredMixin,ListView):
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

class GastosGeneralesListView(LoginRequiredMixin,ListView):
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

class GastosMaterialesListView(LoginRequiredMixin,ListView):
    model = GastosMateriales
    template_name = "gastos/gastos_materiales_list.html"

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        proyecto = Proyectos.objects.get(slug=slug)
        return GastosMateriales.objects.filter(proyecto=proyecto)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        proyecto = Proyectos.objects.get(slug=slug)

        # Calculate total monto using aggregate
        total_monto = GastosMateriales.objects.filter(proyecto=proyecto).aggregate(total=Sum('monto'))['total'] or 0

        # Add the total to the context
        context['total_monto'] = total_monto
        context['proyecto'] = proyecto
        return context 

class GastosManoObraListView(LoginRequiredMixin,ListView):
    model = GastosManoObra
    template_name = "gastos/gastos_mano_obra_list.html"

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        proyecto = Proyectos.objects.get(slug=slug)
        return GastosManoObra.objects.filter(proyecto=proyecto)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        proyecto = Proyectos.objects.get(slug=slug)

        # Calculate total monto using aggregate
        total_monto = GastosManoObra.objects.filter(proyecto=proyecto).aggregate(total=Sum('monto'))['total'] or 0

        # Add the total to the context
        context['total_monto'] = total_monto
        context['proyecto'] = proyecto
        return context 

class GastosEquiposListView(LoginRequiredMixin,ListView):
    model = GastosEquipos
    template_name = "gastos/gastos_equipos_list.html"

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        proyecto = Proyectos.objects.get(slug=slug)
        return GastosEquipos.objects.filter(proyecto=proyecto)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        proyecto = Proyectos.objects.get(slug=slug)

        # Calculate total monto using aggregate
        total_monto = GastosEquipos.objects.filter(proyecto=proyecto).aggregate(total=Sum('monto_concepto'))['total'] or 0

        # Add the total to the context
        context['total_monto'] = total_monto
        context['proyecto'] = proyecto
        return context 

@login_required
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

@login_required
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


@login_required
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


@login_required
def registro_gastos_materiales(request, slug):

    proyecto = Proyectos.objects.get(slug=slug)
    
    if request.method == "POST":
        gastos_materiales_form = GastosMaterialesForm(request.POST)

        if gastos_materiales_form.is_valid():
            gasto_material = gastos_materiales_form.save(commit=False)
            gasto_material.proyecto = proyecto
            gasto_material.save()

            # Actualizar el valor neto del proyecto restando el monto del gasto
            Proyectos.objects.filter(id=proyecto.id).update(total=F('total') - gasto_material.monto)

            return redirect('gastos:gastos_materiales',slug=slug)
    else:
        gastos_materiales_form = GastosGeneralesForm()

    return render(request,'gastos/registrar_gastos_materiales.html',{'gastos_materiales_form':gastos_materiales_form,'proyecto':proyecto})


@login_required
def registro_gastos_mano_obra(request, slug):

    proyecto = Proyectos.objects.get(slug=slug)
    
    if request.method == "POST":
        gastos_mano_obra_form = GastosManoObraForm(request.POST)

        if gastos_mano_obra_form.is_valid():
            gasto_mano_obra = gastos_mano_obra_form.save(commit=False)
            gasto_mano_obra.proyecto = proyecto
            monto_total = gasto_mano_obra.nomina + gasto_mano_obra.imss + gasto_mano_obra.infonavit + gasto_mano_obra.isn + gasto_mano_obra.isr
            gasto_mano_obra.monto = monto_total
            gasto_mano_obra.save()

            # Actualizar el valor neto del proyecto restando el monto del gasto
            Proyectos.objects.filter(id=proyecto.id).update(total=F('total') - gasto_mano_obra.monto)

            return redirect('gastos:gastos_mano_obra',slug=slug)
    else:
        gastos_mano_obra_form = GastosManoObraForm()

    return render(request,'gastos/registrar_gastos_mano_obra.html',{'gastos_mano_obra_form':gastos_mano_obra_form,'proyecto':proyecto})


@login_required
def registro_gastos_equipos(request, slug):

    proyecto = Proyectos.objects.get(slug=slug)
    
    if request.method == "POST":
        gastos_equipos_form = GastosEquiposForm(request.POST)

        if gastos_equipos_form.is_valid():
            gasto_equipo = gastos_equipos_form.save(commit=False)
            gasto_equipo.proyecto = proyecto
            gasto_equipo.save()

            # Actualizar el valor neto del proyecto restando el monto del gasto
            Proyectos.objects.filter(id=proyecto.id).update(total=F('total') - gasto_equipo.monto_concepto)

            return redirect('gastos:gastos_equipos',slug=slug)
    else:
        gastos_equipos_form = GastosEquiposForm()

    return render(request,'gastos/registrar_gastos_equipos.html',{'gastos_equipos_form':gastos_equipos_form,'proyecto':proyecto})