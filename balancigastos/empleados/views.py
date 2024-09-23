from django.shortcuts import render, redirect
from .models import Empleados
from proyectos.models import Proyectos
from .forms import EmpleadosForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
# Create your views here.

class EmpleadosListView(LoginRequiredMixin,ListView):
    model = Empleados
    template_name = "empleados/empleados.html"
    context_object_name = "empleados"

    def get_queryset(self):
        # Obtener la queryset inicial
        queryset = Empleados.objects.all()

        # Obtener los parámetros de filtro de la URL o de un formulario GET
        empleado = self.request.GET.get('empleado')
        rfc = self.request.GET.get('rfc')
        imss = self.request.GET.get('imss')
        infonavit = self.request.GET.get('infonavit')

        # Aplicar los filtros si los valores no son nulos
        if empleado:
            queryset = queryset.filter(empleado=empleado)
        
        if rfc:
            queryset = queryset.filter(rfc__icontains=rfc)
        
        if imss:
            queryset = queryset.filter(imss__icontains=imss)

        if infonavit:
            queryset = queryset.filter(infonavit__icontains=infonavit)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtener el slug del proyecto desde la URL
        # slug = self.kwargs.get('slug')
        # Si necesitas obtener el proyecto con base en el slug:
        # proyecto = Proyectos.objects.get(slug=slug)

        # Pasar los filtros actuales para mantener el estado del formulario
        context['empleado'] = self.request.GET.get('empleado', '')
        context['rfc'] = self.request.GET.get('rfc', '')
        context['imss'] = self.request.GET.get('imss', '')
        context['infonavit'] = self.request.GET.get('infonavit', '')
        # context['project'] = proyecto

        return context


@login_required
def registro_empleados(request):

    empleados = Empleados.objects.all()

    if request.method == "POST":
        empleados_form = EmpleadosForm(request.POST)

        if empleados_form.is_valid():
            empleados_form.save()
            return redirect('empleados:empleados')
    else:
        empleados_form = EmpleadosForm()

    return render(request,'empleados/registrar_empleados.html',{'empleados_form':empleados_form,'empleados':empleados})