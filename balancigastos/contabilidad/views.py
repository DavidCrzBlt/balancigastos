from django.shortcuts import render, redirect, get_object_or_404
from .forms import GastosVehiculosForm, GastosGeneralesForm, GastosMaterialesForm, GastosManoObraForm, GastosSeguridadForm, GastosEquiposForm, IngresosForm
from django.views.generic import ListView
from .models import GastosVehiculos, GastosGenerales, GastosMateriales, GastosManoObra, GastosEquipos, GastosSeguridad, Ingresos
from proyectos.models import Proyectos
from empleados.models import Salario
from django.db.models import Sum, F
from django.db.models.functions import Coalesce
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from decimal import Decimal
from django.contrib import messages

import pandas as pd

# Create your views here.

### Vistas de detalle de proyecto ------------------------------------------- ###
### Funciones genéricas para registro, edición y eliminación de instancias--- ###
### Funciones de registro y edición de instancias por tipo de gasto o ingreso ###
### Funciones de eliminación de instancias ---------------------------------- ###

### ------------------------------------------------------------------------- ###
### ------------------------------------------------------------------------- ###
# Se muestran todas las vistas de los detalles del proyecto
### ------------------------------------------------------------------------- ###
### ------------------------------------------------------------------------- ###

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

        # Calculate total iva using aggregate
        total_iva = Ingresos.objects.filter(proyecto=proyecto).aggregate(total=Sum('iva'))['total'] or 0

        # Add the total to the context
        context['total_monto'] = total_monto
        context['total_iva'] = total_iva
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

        # Calculate total iva using aggregate
        total_iva = GastosVehiculos.objects.filter(proyecto=proyecto).aggregate(total=Sum('iva'))['total'] or 0

        # Add the total to the context
        context['total_monto'] = total_monto
        context['total_iva'] = total_iva
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

        # Calculate total iva using aggregate
        total_iva = GastosGenerales.objects.filter(proyecto=proyecto).aggregate(total=Sum('iva'))['total'] or 0

        # Add the total to the context
        context['total_monto'] = total_monto
        context['total_iva'] = total_iva
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

        # Calculate total iva using aggregate
        total_iva = GastosMateriales.objects.filter(proyecto=proyecto).aggregate(total=Sum('iva'))['total'] or 0
        
        # Add the total to the context
        context['total_monto'] = total_monto
        context['total_iva'] = total_iva
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

        # Calculate total iva using aggregate
        total_iva = GastosEquipos.objects.filter(proyecto=proyecto).aggregate(total=Sum('iva'))['total'] or 0

        # Add the total to the context
        context['total_monto'] = total_monto
        context['total_iva'] = total_iva
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

        # Calculate total iva using aggregate
        total_iva = GastosSeguridad.objects.filter(proyecto=proyecto).aggregate(total=Sum('iva'))['total'] or 0

        # Add the total to the context
        context['total_monto'] = total_monto
        context['total_iva'] = total_iva
        context['proyecto'] = proyecto
        return context 
    
### ------------------------------------------------------------------------- ###
### ------------------------------------------------------------------------- ###
# Escribimos dos funciones que vamos a reutilizar después
### ------------------------------------------------------------------------- ###
### ------------------------------------------------------------------------- ###

# Recalcular gastos e ingresos por fecha. Esto se usará para detalle de proyecto después.
def recalcular_ingresos_gastos_por_fecha(proyecto_id):
    # Obtener ingresos agrupados por fecha
    ingresos = Ingresos.objects.filter(proyecto_id=proyecto_id).values('fecha').annotate(total_ingresos=Sum('monto'))
    df_ingresos = pd.DataFrame(list(ingresos))
    df_ingresos['fecha'] = pd.to_datetime(df_ingresos['fecha'])
    df_ingresos.set_index('fecha', inplace=True)

    # Inicializar DataFrame para almacenar los totales de gastos
    df_gastos_totales = pd.DataFrame()

    # Definir todas las tablas de gastos a considerar
    tablas_gastos = [GastosVehiculos, GastosGenerales, GastosMateriales, GastosSeguridad, GastosManoObra, GastosEquipos]

    # Iterar sobre cada tabla de gastos, obtener los datos y agregarlos
    for tabla in tablas_gastos:
        gastos = tabla.objects.filter(proyecto_id=proyecto_id).values('fecha').annotate(total_gastos=Sum('monto'))
        df_gastos = pd.DataFrame(list(gastos))
        
        if not df_gastos.empty:  # Solo si hay datos en la tabla
            df_gastos['fecha'] = pd.to_datetime(df_gastos['fecha'])
            df_gastos.set_index('fecha', inplace=True)

            # Sumar los valores de esta tabla al DataFrame de totales
            if df_gastos_totales.empty:
                df_gastos_totales = df_gastos
            else:
                df_gastos_totales = df_gastos_totales.add(df_gastos, fill_value=0)

    # Agrupar ingresos y gastos por semana
    ingresos_semanales = df_ingresos.resample('W').sum()
    gastos_semanales = df_gastos_totales.resample('W').sum()

    # Unir los DataFrames de ingresos y gastos en uno solo
    df_semanal = pd.merge(ingresos_semanales, gastos_semanales, left_index=True, right_index=True, how='outer').fillna(0)

    # Renombrar columnas para que tengan sentido en la gráfica
    df_semanal.columns = ['total_ingresos', 'total_gastos']

    return df_semanal


# Recalcular los totales de ingresos y gastos para el proyecto
def recalcular_totales_proyecto(proyecto_id):
    proyecto = Proyectos.objects.get(id=proyecto_id)

    ingresos_result = Ingresos.objects.filter(proyecto=proyecto).aggregate(
        total_ingresos=Coalesce(Sum('monto'),Decimal('0.00')),
        total_iva = Coalesce(Sum('iva'),Decimal('0.00'))
        )
    total_ingresos = ingresos_result['total_ingresos'] 
    total_iva_ingresos = ingresos_result['total_iva']

    gastos_vehiculos_result = GastosVehiculos.objects.filter(proyecto=proyecto).aggregate(
        total_gastos_vehiculos=Coalesce(Sum('monto'),Decimal('0.00')),
        total_iva_vehiculos = Coalesce(Sum('iva'),Decimal('0.00'))
        )
    gastos_vehiculos = gastos_vehiculos_result['total_gastos_vehiculos']
    iva_vehiculos = gastos_vehiculos_result['total_iva_vehiculos']

    gastos_generales_result = GastosGenerales.objects.filter(proyecto=proyecto).aggregate(
        total_gastos_generales=Coalesce(Sum('monto'),Decimal('0.00')),
        total_iva_generales=Coalesce(Sum('iva'),Decimal('0.00'))
        )
    gastos_generales = gastos_generales_result['total_gastos_generales'] 
    iva_generales = gastos_generales_result['total_iva_generales'] 

    gastos_materiales_result = GastosMateriales.objects.filter(proyecto=proyecto).aggregate(
        total_gastos_materiales=Coalesce(Sum('monto'),Decimal('0.00')),
        total_iva_materiales=Coalesce(Sum('iva'),Decimal('0.00'))
        )
    gastos_materiales = gastos_materiales_result['total_gastos_materiales'] 
    iva_materiales = gastos_materiales_result['total_iva_materiales'] 

    gastos_seguridad_result = GastosSeguridad.objects.filter(proyecto=proyecto).aggregate(
        total_gastos_seguridad=Coalesce(Sum('monto'),Decimal('0.00')),
        total_iva_seguridad=Coalesce(Sum('iva'),Decimal('0.00'))
        )
    gastos_seguridad = gastos_seguridad_result['total_gastos_seguridad']
    iva_seguridad = gastos_seguridad_result['total_iva_seguridad']

    gastos_mano_obra_result = GastosManoObra.objects.filter(proyecto=proyecto).aggregate(total_gastos_mano_obra=Coalesce(Sum('monto'),Decimal('0.00')))
    gastos_mano_obra = gastos_mano_obra_result['total_gastos_mano_obra'] 

    gastos_equipos_result = GastosEquipos.objects.filter(proyecto=proyecto).aggregate(
        total_gastos_equipos=Coalesce(Sum('monto'),Decimal('0.00')),
        total_iva_equipos=Coalesce(Sum('iva'),Decimal('0.00'))
        )
    gastos_equipos = gastos_equipos_result['total_gastos_equipos'] 
    iva_equipos = gastos_equipos_result['total_iva_equipos'] 

    # Add the numerical results
    total_gastos = gastos_vehiculos + gastos_generales + gastos_materiales + gastos_mano_obra + gastos_equipos + gastos_seguridad

    total_iva_gastos = iva_vehiculos + iva_generales + iva_materiales + iva_equipos + iva_seguridad

    # Actualizar el proyecto con los nuevos valores
    total_neto = total_ingresos - total_gastos
    iva_neto = total_iva_ingresos - total_iva_gastos

    # Actualizar el proyecto con los nuevos valores
    proyecto.total = total_neto
    proyecto.iva = iva_neto
    proyecto.save()

    # Retornar un diccionario con los valores calculados
    return {
        'total_ingresos': total_ingresos,
        'total_iva_ingresos': total_iva_ingresos,
        'total_gastos': total_gastos,
        'total_iva_gastos': total_iva_gastos,
        'gastos_vehiculos':gastos_vehiculos,
        'iva_vehiculos':iva_vehiculos,
        'gastos_generales':gastos_generales,
        'iva_generales':iva_generales,
        'gastos_materiales':gastos_materiales,
        'iva_materiales':iva_materiales,
        'gastos_seguridad':gastos_seguridad,
        'iva_seguridad':iva_seguridad,
        'gastos_equipos':gastos_equipos,
        'iva_equipos':iva_equipos,
        'gastos_mano_obra':gastos_mano_obra,
        'total_neto': total_neto,
        'iva_neto': iva_neto
    }


@login_required
def registro_operaciones_generico(request, slug, form_class, redirect_url,op_category,active_tab):

    # Obtén el proyecto usando el slug
    proyecto = Proyectos.objects.get(slug=slug)

    if not proyecto.estatus:
        messages.error(request, "No se pueden registrar operaciones para un proyecto inactivo.")
        return redirect(redirect_url,slug=slug)

    if request.method == "POST":

        if form_class.is_valid():
            gasto = form_class.save(commit=False)
            gasto.proyecto = proyecto
            gasto.iva = gasto.monto * Decimal('0.16')
            gasto.save()

            # Actualizar el valor neto del proyecto (suma o resta según la categoría)
            recalcular_totales_proyecto(proyecto.id)

            # Redirige a la URL que se pasa como argumento
            return redirect(redirect_url, slug=slug)

    # Renderiza el template correspondiente
    return render(request, 'contabilidad/registrar_operaciones.html', {'operaciones_form': form_class,
     'proyecto': proyecto,
     'categoria_operacion':op_category,
     'active_tab':active_tab})

@login_required
def eliminar_operaciones_generico(request,slug,modelo,instancia_id,redirect_url):
    # Obtener el proyecto
    proyecto = get_object_or_404(Proyectos, slug=slug)

    if proyecto.estatus == True:

        # Buscar el movimiento por ID
        movimiento = get_object_or_404(modelo, id=instancia_id, proyecto=proyecto)

        # Eliminar el movimiento
        movimiento.delete()

        # Actualizar el valor neto del proyecto (suma o resta según la categoría)
        recalcular_totales_proyecto(proyecto.id)

        # Mostrar un mensaje de éxito
        messages.success(request, 'El gasto ha sido eliminado exitosamente.')

        # Redirigir a la lista de gastos o a la página que prefieras
        return redirect(redirect_url, slug=slug)
    else:
        # Mostrar un mensaje de advertencia
        messages.error(request, 'No se pueden hacer cambios a un proyecto inactivo.')
        # Redirigir a página de error
        return redirect(redirect_url,slug=slug)

### ------------------------------------------------------------------------- ###
### ------------------------------------------------------------------------- ###
# A partir de aquí se registran los gastos e ingresos
### ------------------------------------------------------------------------- ###
### ------------------------------------------------------------------------- ###
@login_required
def registro_gastos_vehiculos(request,slug,gasto_id=None):

    if gasto_id:
        # Si se pasa un gasto_id, es una edición, se obtiene el gasto
        gasto = get_object_or_404(GastosVehiculos, id=gasto_id)
        form_class = GastosVehiculosForm(request.POST or None, instance=gasto)  # Precargar datos
    else:
        # Si no hay gasto_id, es un registro nuevo
        form_class = GastosVehiculosForm(request.POST or None)

    return registro_operaciones_generico(
        request=request,
        slug=slug,
        form_class=form_class,    # Formulario de gastos de vehículos
        redirect_url='contabilidad:gastos_vehiculos',  # URL a la que redirigir
        op_category='gastos de vehículos',  # Categoría de operación
        active_tab='vehiculos'
    )

@login_required
def registro_gastos_generales(request,slug,gasto_id=None):

    if gasto_id:
        # Si se pasa un gasto_id, es una edición, se obtiene el gasto
        gasto = get_object_or_404(GastosGenerales, id=gasto_id)
        form_class = GastosGeneralesForm(request.POST or None, instance=gasto)  # Precargar datos
    else:
        # Si no hay gasto_id, es un registro nuevo
        form_class = GastosGeneralesForm(request.POST or None)

    return registro_operaciones_generico(
        request=request,
        slug=slug,
        form_class=form_class,    # Formulario de gastos generales
        redirect_url='contabilidad:gastos_generales',  # URL a la que redirigir
        op_category='gastos generales',  # Categoría de operación
        active_tab='generales'
    )

@login_required
def registro_gastos_materiales(request,slug,gasto_id=None):

    if gasto_id:
        # Si se pasa un gasto_id, es una edición, se obtiene el gasto
        gasto = get_object_or_404(GastosMateriales, id=gasto_id)
        form_class = GastosMaterialesForm(request.POST or None, instance=gasto)  # Precargar datos
    else:
        # Si no hay gasto_id, es un registro nuevo
        form_class = GastosMaterialesForm(request.POST or None)

    return registro_operaciones_generico(
        request=request,
        slug=slug,
        form_class=form_class,    # Formulario de gastos de materiales
        redirect_url='contabilidad:gastos_materiales',  # URL a la que redirigir
        op_category='gastos de materiales',  # Categoría de operación
        active_tab='materiales'
    )

@login_required
def registro_gastos_seguridad(request,slug,gasto_id=None):

    if gasto_id:
        # Si se pasa un gasto_id, es una edición, se obtiene el gasto
        gasto = get_object_or_404(GastosSeguridad, id=gasto_id)
        form_class = GastosSeguridadForm(request.POST or None, instance=gasto)  # Precargar datos
    else:
        # Si no hay gasto_id, es un registro nuevo
        form_class = GastosSeguridadForm(request.POST or None)

    return registro_operaciones_generico(
        request=request,
        slug=slug,
        form_class=form_class,    # Formulario de gastos de seguridad
        redirect_url='contabilidad:gastos_seguridad',  # URL a la que redirigir
        op_category='gastos de seguridad',  # Categoría de operación
        active_tab='seguridad'
    )

@login_required
def registro_gastos_equipos(request,slug,gasto_id=None):

    if gasto_id:
        # Si se pasa un gasto_id, es una edición, se obtiene el gasto
        gasto = get_object_or_404(GastosEquipos, id=gasto_id)
        form_class = GastosEquiposForm(request.POST or None, instance=gasto)  # Precargar datos
    else:
        # Si no hay gasto_id, es un registro nuevo
        form_class = GastosEquiposForm(request.POST or None)

    return registro_operaciones_generico(
        request=request,
        slug=slug,
        form_class=form_class,    # Formulario de gastos de equipos
        redirect_url='contabilidad:gastos_equipos',  # URL a la que redirigir
        op_category='gastos equipos',  # Categoría de operación
        active_tab='equipos'
    )

@login_required
def registro_gastos_mano_obra(request,slug):
    return registro_operaciones_generico(
        request=request,
        slug=slug,
        form_class=GastosManoObraForm,    # Formulario de gastos de mano de obra
        redirect_url='contabilidad:gastos_mano_obra',  # URL a la que redirigir
        op_category='gastos mano de obra',  # Categoría de operación
        active_tab='mano_obra'
    )

@login_required
def registro_ingresos(request,slug,ingreso_id=None):

    if ingreso_id:
        # Si se pasa un ingreso_id, es una edición, se obtiene el gasto
        gasto = get_object_or_404(Ingresos, id=ingreso_id)
        form_class = IngresosForm(request.POST or None, instance=gasto)  # Precargar datos
    else:
        # Si no hay ingreso_id, es un registro nuevo
        form_class = IngresosForm(request.POST or None)

    return registro_operaciones_generico(
        request=request,
        slug=slug,
        form_class=form_class,    # Formulario de ingresos
        redirect_url='contabilidad:ingresos',  # URL a la que redirigir
        op_category='ingresos',  # Categoría de operación
        active_tab='ingresos'
    )

### ------------------------------------------------------------------------- ###
### ------------------------------------------------------------------------- ###
# A partir de aquí se eliminan instancias de gastos o ingresos
### ------------------------------------------------------------------------- ###
### ------------------------------------------------------------------------- ###

@login_required
def eliminar_gastos_mano_obra(request,slug,gasto_id):

    # Obtenemos el proyecto
    proyecto = Proyectos.objects.get(slug=slug)
    # No se pueden hacer cambios a proyectos inactivos
    if proyecto.estatus == True:
        # También tenemos que eliminar los salarios de la tabla Salario en empleados
        # Para eso necesitamos obtener el número de lote
        gasto = GastosManoObra.objects.get(id=gasto_id) 
        lote = gasto.lote
        # Con el número de lote buscamos los salarios que vamos a eliminar
        salarios_a_eliminar = Salario.objects.filter(lote=lote)

        if salarios_a_eliminar.exists():
            num_eliminados = salarios_a_eliminar.count()
            salarios_a_eliminar.delete()
            # Mostrar un mensaje de éxito con el número de instancias eliminadas
            messages.success(request, f'Se han eliminado {num_eliminados} salarios del lote {lote} exitosamente.')
        else:
            # Mostrar un mensaje si no hay salarios asociados a ese lote
            messages.error(request, f'No se encontraron salarios asociados al lote {lote}.')

        return eliminar_operaciones_generico(
            request=request,
            slug=slug,
            modelo=GastosManoObra,
            instancia_id=gasto_id,
            redirect_url='contabilidad:gastos_mano_obra',  # URL a la que redirigir
        )
    
    else:
        # Mostrar un mensaje de advertencia
        messages.error(request, 'No se pueden hacer cambios a un proyecto inactivo.')
        # Redirigir a página de error
        return redirect('contabilidad:gastos_mano_obra',slug=slug)
    
@login_required
def eliminar_gastos_generales(request, slug, gasto_id):
    return eliminar_operaciones_generico(
            request=request,
            slug=slug,
            modelo=GastosGenerales,
            instancia_id=gasto_id,
            redirect_url='contabilidad:gastos_generales',  # URL a la que redirigir
        )

@login_required
def eliminar_gastos_equipos(request, slug, gasto_id):
    return eliminar_operaciones_generico(
            request=request,
            slug=slug,
            modelo=GastosEquipos,
            instancia_id=gasto_id,
            redirect_url='contabilidad:gastos_equipos',  # URL a la que redirigir
        )

@login_required
def eliminar_gastos_materiales(request, slug, gasto_id):
    return eliminar_operaciones_generico(
            request=request,
            slug=slug,
            modelo=GastosMateriales,
            instancia_id=gasto_id, 
            redirect_url='contabilidad:gastos_materiales',  # URL a la que redirigir
        )

@login_required
def eliminar_gastos_seguridad(request, slug, gasto_id):
    return eliminar_operaciones_generico(
            request=request,
            slug=slug,
            modelo=GastosSeguridad,
            instancia_id=gasto_id, 
            redirect_url='contabilidad:gastos_seguridad',  # URL a la que redirigir
        )

@login_required
def eliminar_gastos_vehiculos(request, slug, gasto_id):
    return eliminar_operaciones_generico(
            request=request,
            slug=slug,
            modelo=GastosVehiculos,
            instancia_id=gasto_id,  
            redirect_url='contabilidad:gastos_vehiculos',  # URL a la que redirigir
        )

@login_required
def eliminar_ingresos(request, slug, gasto_id):
    return eliminar_operaciones_generico(
            request=request,
            slug=slug,
            modelo=Ingresos,
            instancia_id=gasto_id, 
            redirect_url='contabilidad:ingresos',  # URL a la que redirigir
        )