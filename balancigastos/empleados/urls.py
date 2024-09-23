from django.urls import path
from . import views
from .views import EmpleadosListView
app_name = 'empleados'

urlpatterns = [
    path("empleados/",EmpleadosListView.as_view(),name="empleados"),
    path("registro-empleado/",views.registro_empleados,name="registro_empleados"),
]