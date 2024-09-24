from django.urls import path
from . import views
from .views import EmpleadosListView, AsistenciasListView
app_name = 'empleados'

urlpatterns = [
    path("empleados/",EmpleadosListView.as_view(),name="empleados"),
    path("registro-empleado/",views.registro_empleados,name="registro_empleados"),
    path("asistencias/<slug:slug>",AsistenciasListView.as_view(),name="asistencias"),
    path("registro_asistencias/",views.registro_asistencias,name="registro_asistencias"),
]