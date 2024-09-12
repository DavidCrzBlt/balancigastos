from django.shortcuts import render,redirect, get_object_or_404
from .forms import ProyectosForm, IngresosForm
from django.views.generic import ListView, DetailView
from .models import Proyectos, Ingresos
from gastos.models import GastosGenerales, GastosVehiculos
from django.db.models import Sum, F

import io
from django.http import HttpResponse
from openpyxl import Workbook

# Create your views here.

class IngresosListView(ListView):
    model = Ingresos
    template_name = "proyectos/ingresos.html"

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        proyecto = Proyectos.objects.get(slug=slug)
        return Ingresos.objects.filter(proyecto=proyecto)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        proyecto = Proyectos.objects.get(slug=slug)

        # Calculate total monto using aggregate
        total_monto = Ingresos.objects.filter(proyecto=proyecto).aggregate(total=Sum('ingreso'))['total'] or 0

        # Add the total to the context
        context['total_monto'] = total_monto
        context['proyecto'] = proyecto
        return context 

class ProyectosListView(ListView):
    model = Proyectos
    template_name = "proyectos/proyectos.html"
    context_object_name = "projects"

    def get_queryset(self):
        # Obtener la queryset inicial
        queryset = Proyectos.objects.all()

        # Obtener los parámetros de filtro de la URL o de un formulario GET
        estatus = self.request.GET.get('estatus')
        empresa = self.request.GET.get('empresa')
        proyecto = self.request.GET.get('proyecto')
        total_min = self.request.GET.get('total_min')
        total_max = self.request.GET.get('total_max')

        # Aplicar los filtros si los valores no son nulos
        if estatus:
            queryset = queryset.filter(estatus=estatus)
        
        if empresa:
            queryset = queryset.filter(empresa__icontains=empresa)
        
        if proyecto:
            queryset = queryset.filter(proyecto__icontains=proyecto)
        
        if total_min:
            queryset = queryset.filter(total__gte=total_min)
        
        if total_max:
            queryset = queryset.filter(total__lte=total_max)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Calcular la suma del campo 'total' de todos los proyectos filtrados
        total_monto_neto = self.get_queryset().aggregate(total=Sum('total'))['total'] or 0
        
        # Pasar la suma total al contexto
        context['total_monto_neto'] = total_monto_neto
        
        # Pasar los filtros actuales para mantener el estado del formulario
        context['estatus'] = self.request.GET.get('estatus', '')
        context['empresa'] = self.request.GET.get('empresa', '')
        context['proyecto'] = self.request.GET.get('proyecto', '')
        context['total_min'] = self.request.GET.get('total_min', '')
        context['total_max'] = self.request.GET.get('total_max', '')

        return context

    
class ProyectosDetailView(DetailView):
    model = Proyectos
    template_name = "proyectos/proyectos_detalles.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        proyecto = self.get_object()

        # Perform aggregations and ensure you extract the numerical values using ['key'] and default to 0 if None
        ingresos_result = Ingresos.objects.filter(proyecto=proyecto).aggregate(total_ingresos=Sum('ingreso'))
        ingresos = ingresos_result['total_ingresos'] if ingresos_result['total_ingresos'] is not None else 0

        gastos_vehiculos_result = GastosVehiculos.objects.filter(proyecto=proyecto).aggregate(total_gastos_vehiculos=Sum('monto'))
        gastos_vehiculos = gastos_vehiculos_result['total_gastos_vehiculos'] if gastos_vehiculos_result['total_gastos_vehiculos'] is not None else 0

        gastos_generales_result = GastosGenerales.objects.filter(proyecto=proyecto).aggregate(total_gastos_generales=Sum('monto_concepto'))
        gastos_generales = gastos_generales_result['total_gastos_generales'] if gastos_generales_result['total_gastos_generales'] is not None else 0

        # Add the numerical results
        total_gastos = gastos_vehiculos + gastos_generales
        neto = ingresos - total_gastos

        # Add values to the context
        context['ingresos'] = ingresos
        context['gastos_vehiculos'] = gastos_vehiculos
        context['gastos_generales'] = gastos_generales
        context['total_gastos'] = total_gastos
        context['neto'] = neto
        return context

def registrar_proyecto(request):
    registrar_proyectos_form = ProyectosForm()
    if request.method == "POST":
        registrar_proyectos_form = ProyectosForm(request.POST)
        
        if registrar_proyectos_form.is_valid():
            registrar_proyectos_form.save()
            return redirect('proyectos:proyectos')
        else:
            registrar_proyectos_form = ProyectosForm()

    return render(request,"proyectos/registrar_proyecto.html",{'proyectos_form':registrar_proyectos_form})

def registrar_ingreso(request, slug):
    # Fetch the project based on the slug
    proyecto = Proyectos.objects.get(slug=slug)

    # Form handling
    registrar_ingresos_form = IngresosForm()
    if request.method == "POST":
        registrar_ingresos_form = IngresosForm(request.POST)
        
        if registrar_ingresos_form.is_valid():
            ingreso = registrar_ingresos_form.save(commit=False)
            ingreso.proyecto = proyecto  # Associate the income with the project
            ingreso.save()

            # Actualizar el valor neto del proyecto sumando el monto del ingreso
            Proyectos.objects.filter(id=proyecto.id).update(total=F('total') + ingreso.ingreso)

            return redirect('proyectos:ingresos', slug=slug)
    
    return render(request, "proyectos/registrar_ingresos.html", {
        'ingresos_form': registrar_ingresos_form,
        'proyecto': proyecto  # Pass the project to the template
    })

def toggle_estatus_proyecto(request, slug):
    # Obtener el proyecto por su slug
    proyecto = get_object_or_404(Proyectos, slug=slug)

    # Alternar el estatus entre True (Activo) y False (Inactivo)
    proyecto.estatus = not proyecto.estatus
    proyecto.save()

    # Redirigir a la página de detalle del proyecto o a la lista de proyectos
    return redirect('proyectos:proyectos')

def export_proyectos_to_excel(request):
    # Crea un libro de trabajo y una hoja
    wb = Workbook()
    ws = wb.active
    ws.title = 'Proyectos'

    # Añade encabezados
    headers = ['ID', 'Nombre', 'Empresa', 'Estatus', 'Monto']  # Ajusta según tus campos
    ws.append(headers)

    # Añade datos de los proyectos
    proyectos = Proyectos.objects.all()  # Obtén todos los proyectos
    for proyecto in proyectos:
        ws.append([proyecto.id, proyecto.proyecto, proyecto.empresa, proyecto.estatus, proyecto.total])  # Ajusta según tus campos

    # Guarda el libro de trabajo en un buffer
    buffer = io.BytesIO()
    wb.save(buffer)
    buffer.seek(0)

    # Prepara la respuesta HTTP
    response = HttpResponse(buffer, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=proyectos.xlsx'
    return response

def export_project_details_to_excel(request, proyecto_slug):
    # Obtén el proyecto
    proyecto = Proyectos.objects.get(slug=proyecto_slug)
    
    # Crea un libro de trabajo y varias hojas
    wb = Workbook()

    # Hoja de Proyectos
    ws1 = wb.active
    ws1.title = 'Proyectos'
    headers1 = ['ID', 'Proyecto', 'Empresa', 'Estatus', 'Total']
    ws1.append(headers1)
    ws1.append([proyecto.id, proyecto.proyecto, proyecto.empresa, proyecto.estatus, proyecto.total])

    # Hoja de Ingresos
    ws2 = wb.create_sheet(title='Ingresos')
    headers2 = ['ID', 'Concepto', 'Ingreso', 'Referencia', 'Fecha']
    ws2.append(headers2)
    ingresos = Ingresos.objects.filter(proyecto=proyecto)
    for ingreso in ingresos:
        fecha_ingreso = ingreso.fecha.replace(tzinfo=None)
        ws2.append([ingreso.id, ingreso.concepto, ingreso.ingreso, ingreso.referencia, fecha_ingreso])

    # Hoja de Gastos Vehículos
    ws3 = wb.create_sheet(title='Gastos Vehículos')
    headers3 = ['ID', 'Vehículo', 'Cantidad Combustible', 'Monto', 'Ubicación', 'Conductor', 'Fecha']
    ws3.append(headers3)
    gastos_vehiculos = GastosVehiculos.objects.filter(proyecto=proyecto)
    for gasto in gastos_vehiculos:
        fecha_gasto = gasto.fecha.replace(tzinfo=None)
        ws3.append([
            gasto.id,
            gasto.vehiculo.vehiculo,  # Extrae el nombre del vehículo
            gasto.cantidad_combustible,
            gasto.monto,
            gasto.ubicacion,
            gasto.conductor,
            fecha_gasto
        ])

    # Hoja de Gastos Generales
    ws4 = wb.create_sheet(title='Gastos Generales')
    headers4 = ['ID', 'Concepto', 'Comprador', 'Monto Concepto', 'Descripción', 'Ubicación', 'Fecha']
    ws4.append(headers4)
    gastos_generales = GastosGenerales.objects.filter(proyecto=proyecto)
    for gasto in gastos_generales:
        fecha_gasto_general = gasto.fecha.replace(tzinfo=None)
        ws4.append([gasto.id, gasto.concepto, gasto.comprador, gasto.monto_concepto, gasto.descripcion, gasto.ubicacion, fecha_gasto])

    # Guarda el libro de trabajo en un buffer
    buffer = io.BytesIO()
    wb.save(buffer)
    buffer.seek(0)

    # Prepara la respuesta HTTP
    response = HttpResponse(buffer, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename={proyecto_slug}_detalles.xlsx'
    return response