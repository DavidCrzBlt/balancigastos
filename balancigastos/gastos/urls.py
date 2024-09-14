from django.urls import path

from . import views
from gastos.views import GastosVehiculosListView, GastosGeneralesListView, GastosMaterialesListView, GastosManoObraListView, GastosEquiposListView

app_name = 'gastos'
urlpatterns = [
    path("<slug:slug>/gastos-generales",GastosGeneralesListView.as_view(),name="gastos_generales"),
    path("registrar-gastos-generales/<slug:slug>",views.registro_gastos_generales, name="registro_gastos_generales"),
    path("<slug:slug>/gastos-vehiculos",GastosVehiculosListView.as_view(),name="gastos_vehiculos"),
    path("registrar-gastos-vehiculos/<slug:slug>",views.registro_gastos_vehiculos, name="registro_gastos_vehiculos"),
    path("registrar-vehiculo",views.registro_vehiculos, name="registro_vehiculos"),
    path("registrar-gastos-materiales/<slug:slug>",views.registro_gastos_materiales,name="registro_gastos_materiales"),
    path("<slug:slug>/gastos-materiales",GastosMaterialesListView.as_view(),name="gastos_materiales"),
    path("registrar-gastos-mano-obra/<slug:slug>",views.registro_gastos_mano_obra,name="registro_gastos_mano_obra"),
    path("<slug:slug>/gastos-mano-obra",GastosManoObraListView.as_view(),name="gastos_mano_obra"),
    path("registrar-gastos-equipos/<slug:slug>",views.registro_gastos_equipos,name="registro_gastos_equipos"),
    path("<slug:slug>/gastos-equipos",GastosEquiposListView.as_view(),name="gastos_equipos"),
]