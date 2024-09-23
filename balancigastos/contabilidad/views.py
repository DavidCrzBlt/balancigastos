from django.shortcuts import render, redirect
from .forms import GastosVehiculosForm, GastosGeneralesForm, GastosMaterialesForm, GastosManoObraForm, GastosSeguridadForm, GastosEquiposForm, IngresosForm
from django.views.generic import ListView
from .models import GastosVehiculos, GastosGenerales, GastosMateriales, GastosManoObra, GastosEquipos, GastosSeguridad, Ingresos
from proyectos.models import Proyectos
from django.db.models import Sum, F
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from decimal import Decimal

# Create your views here.

class IngresosListView(LoginRequiredMixin,ListView):
    model = Ingresos
    template_name = "contabilidad/ingresos.html"

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        proyecto = Proyectos.objects.get(slug=slug)
        return Ingresos.objects.filter(proyecto=proyecto)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        proyecto = Proyectos.objects.get(slug=slug)

        # Calculate total monto using aggregate
        total_monto = Ingresos.objects.filter(proyecto=proyecto).aggregate(total=Sum('monto'))['total'] or 0

        # Add the total to the context
        context['total_monto'] = total_monto
        context['proyecto'] = proyecto
        return context 

class GastosVehiculosListView(LoginRequiredMixin,ListView):
    model = GastosVehiculos
    template_name = "contabilidad/gastos_vehiculos_list.html"

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
    template_name = "contabilidad/gastos_generales_list.html"

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        proyecto = Proyectos.objects.get(slug=slug)
        return GastosGenerales.objects.filter(proyecto=proyecto)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        proyecto = Proyectos.objects.get(slug=slug)

        # Calculate total monto using aggregate
        total_monto = GastosGenerales.objects.filter(proyecto=proyecto).aggregate(total=Sum('monto'))['total'] or 0

        # Add the total to the context
        context['total_monto'] = total_monto
        context['proyecto'] = proyecto
        return context 

class GastosMaterialesListView(LoginRequiredMixin,ListView):
    model = GastosMateriales
    template_name = "contabilidad/gastos_materiales_list.html"

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
    template_name = "contabilidad/gastos_mano_obra_list.html"

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
    template_name = "contabilidad/gastos_equipos_list.html"

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        proyecto = Proyectos.objects.get(slug=slug)
        return GastosEquipos.objects.filter(proyecto=proyecto)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        proyecto = Proyectos.objects.get(slug=slug)

        # Calculate total monto using aggregate
        total_monto = GastosEquipos.objects.filter(proyecto=proyecto).aggregate(total=Sum('monto'))['total'] or 0

        # Add the total to the context
        context['total_monto'] = total_monto
        context['proyecto'] = proyecto
        return context 
    
class GastosSeguridadListView(LoginRequiredMixin,ListView):
    model = GastosEquipos
    template_name = "contabilidad/gastos_seguridad_list.html"

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        proyecto = Proyectos.objects.get(slug=slug)
        return GastosSeguridad.objects.filter(proyecto=proyecto)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        proyecto = Proyectos.objects.get(slug=slug)

        # Calculate total monto using aggregate
        total_monto = GastosSeguridad.objects.filter(proyecto=proyecto).aggregate(total=Sum('monto'))['total'] or 0

        # Add the total to the context
        context['total_monto'] = total_monto
        context['proyecto'] = proyecto
        return context 

@login_required
def registro_operaciones_generico(request, slug, form_class, category_update, redirect_url,op_category,active_tab):

    # Obtén el proyecto usando el slug
    proyecto = Proyectos.objects.get(slug=slug)
    
    if request.method == "POST":
        # Usa la clase de formulario que se pasa como argumento
        form = form_class(request.POST)

        if form.is_valid():
            gasto = form.save(commit=False)
            gasto.proyecto = proyecto
            gasto.iva = gasto.monto * Decimal('0.16')
            gasto.save()

            # Actualizar el valor neto del proyecto (suma o resta según la categoría)
            if category_update == 'gasto':
                Proyectos.objects.filter(id=proyecto.id).update(total=F('total') - gasto.monto)
            elif category_update == 'ingreso':
                Proyectos.objects.filter(id=proyecto.id).update(total=F('total') + gasto.monto)

            # Redirige a la URL que se pasa como argumento
            return redirect(redirect_url, slug=slug)
    
    else:
        form = form_class()

    # Renderiza el template correspondiente
    return render(request, 'contabilidad/registrar_operaciones.html', {'operaciones_form': form, 'proyecto': proyecto,'categoria_operacion':op_category,'active_tab':active_tab})

def registro_gastos_vehiculos(request,slug):
    return registro_operaciones_generico(
        request=request,
        slug=slug,
        form_class=GastosVehiculosForm,    # Formulario de gastos de vehículos
        category_update='gasto',  # Indica que es un gasto (se resta)
        redirect_url='contabilidad:gastos_vehiculos',  # URL a la que redirigir
        op_category='gastos de vehículos',  # Categoría de operación
        active_tab='vehiculos'
    )

def registro_gastos_generales(request,slug):
    return registro_operaciones_generico(
        request=request,
        slug=slug,
        form_class=GastosGeneralesForm,    # Formulario de gastos generales
        category_update='gasto',  # Indica que es un gasto (se resta)
        redirect_url='contabilidad:gastos_generales',  # URL a la que redirigir
        op_category='gastos generales',  # Categoría de operación
        active_tab='generales'
    )

def registro_gastos_materiales(request,slug):
    return registro_operaciones_generico(
        request=request,
        slug=slug,
        form_class=GastosMaterialesForm,    # Formulario de gastos de materiales
        category_update='gasto',  # Indica que es un gasto (se resta)
        redirect_url='contabilidad:gastos_materiales',  # URL a la que redirigir
        op_category='gastos de materiales',  # Categoría de operación
        active_tab='materiales'
    )

def registro_gastos_seguridad(request,slug):
    return registro_operaciones_generico(
        request=request,
        slug=slug,
        form_class=GastosSeguridadForm,    # Formulario de gastos de seguridad
        category_update='gasto',  # Indica que es un gasto (se resta)
        redirect_url='contabilidad:gastos_seguridad',  # URL a la que redirigir
        op_category='gastos de seguridad',  # Categoría de operación
        active_tab='seguridad'
    )

def registro_gastos_equipos(request,slug):
    return registro_operaciones_generico(
        request=request,
        slug=slug,
        form_class=GastosEquiposForm,    # Formulario de gastos de equipos
        category_update='gasto',  # Indica que es un gasto (se resta)
        redirect_url='contabilidad:gastos_equipos',  # URL a la que redirigir
        op_category='gastos equipos',  # Categoría de operación
        active_tab='equipos'
    )

def registro_gastos_mano_obra(request,slug):
    return registro_operaciones_generico(
        request=request,
        slug=slug,
        form_class=GastosManoObraForm,    # Formulario de gastos de mano de obra
        category_update='gasto',  # Indica que es un gasto (se resta)
        redirect_url='contabilidad:gastos_mano_obra',  # URL a la que redirigir
        op_category='gastos mano de obra',  # Categoría de operación
        active_tab='mano_obra'
    )

def registro_ingresos(request,slug):
    return registro_operaciones_generico(
        request=request,
        slug=slug,
        form_class= IngresosForm,    # Formulario de ingresos
        category_update='ingreso',  # Indica que es un ingreso (se suma)
        redirect_url='contabilidad:ingresos',  # URL a la que redirigir
        op_category='ingresos',  # Categoría de operación
        active_tab='ingresos'
    )