from django.urls import path

from . import views
from gastos.views import GastosVehiculosListView, GastosGeneralesListView

app_name = 'gastos'
urlpatterns = [
    path("<slug:slug>/gastos-generales",GastosGeneralesListView.as_view(),name="gastos_generales"),
    path("registrar-gastos-generales/<slug:slug>",views.registro_gastos_generales, name="registro_gastos_generales"),
    path("<slug:slug>/gastos-vehiculos",GastosVehiculosListView.as_view(),name="gastos_vehiculos"),
    path("registrar-gastos-vehiculos/<slug:slug>",views.registro_gastos_vehiculos, name="registro_gastos_vehiculos"),
    path("registrar-vehiculo",views.registro_vehiculos, name="registro_vehiculos"),
]