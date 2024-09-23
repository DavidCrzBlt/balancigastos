from django.urls import path
from . import views
from contabilidad.views import GastosVehiculosListView, GastosGeneralesListView, GastosMaterialesListView, GastosManoObraListView, GastosEquiposListView, IngresosListView, GastosSeguridadListView

app_name = 'contabilidad'

urlpatterns = [
    path("<slug:slug>/gastos-generales",GastosGeneralesListView.as_view(),name="gastos_generales"),
    path("registrar-gastos-generales/<slug:slug>",views.registro_gastos_generales, name="registro_gastos_generales"),
    path("<slug:slug>/gastos-vehiculos",GastosVehiculosListView.as_view(),name="gastos_vehiculos"),
    path("registrar-gastos-vehiculos/<slug:slug>",views.registro_gastos_vehiculos, name="registro_gastos_vehiculos"),
    path("registrar-gastos-materiales/<slug:slug>",views.registro_gastos_materiales,name="registro_gastos_materiales"),
    path("<slug:slug>/gastos-materiales",GastosMaterialesListView.as_view(),name="gastos_materiales"),
    path("registrar-gastos-mano-obra/<slug:slug>",views.registro_gastos_mano_obra,name="registro_gastos_mano_obra"),
    path("<slug:slug>/gastos-mano-obra",GastosManoObraListView.as_view(),name="gastos_mano_obra"),
    path("registrar-gastos-equipos/<slug:slug>",views.registro_gastos_equipos,name="registro_gastos_equipos"),
    path("<slug:slug>/gastos-equipos",GastosEquiposListView.as_view(),name="gastos_equipos"),
    path("registrar-gastos-seguridad/<slug:slug>",views.registro_gastos_seguridad,name="registro_gastos_seguridad"),
    path("<slug:slug>/gastos-seguridad",GastosSeguridadListView.as_view(),name="gastos_seguridad"),
    path("<slug:slug>/ingresos",IngresosListView.as_view(),name="ingresos"),
    path("registrar-ingreso/<slug:slug>",views.registro_ingresos,name="registro_ingresos"),
]