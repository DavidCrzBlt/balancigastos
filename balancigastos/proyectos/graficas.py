# graficas.py

from .models import Proyectos

from contabilidad.views import recalcular_totales_proyecto, recalcular_ingresos_gastos_por_fecha

import plotly.express as px
import pandas as pd


def grafica_ingresos_vs_gastos_semanales(proyecto_id):
    
    # Obtener los ingresos y gastos por semana
    df_semanal = recalcular_ingresos_gastos_por_fecha(proyecto_id)

    # Verifica si df_semanal tiene datos antes de graficar
    if df_semanal.empty:
        return None  # O devuelve un gráfico vacío o un mensaje adecuado

    # Convertir el índice a Datetime si es necesario (esto solo si el índice es de tipo DateField)
    # df_semanal.index = pd.to_datetime(df_semanal.index)  # Asegura que el índice sea reconocido como fechas

    # Agrupar por semana si es necesario, por ejemplo, usando resample:
    df_semanal = df_semanal.resample('W').sum()

    # Crear la gráfica de líneas
    fig = px.line(df_semanal.reset_index(), x='fecha', y=['total_ingresos', 'total_gastos'], markers=True)

    fig.update_layout(
    xaxis_title='Fecha (Semana)',
    yaxis_title='Monto',
    yaxis_tickformat='$,.4s MXN',  # Formato de moneda
    legend_title='Totales por semana',
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(255, 255, 255, 0.8)',
    font=dict(family="Arial, sans-serif", size=16),
    template="plotly_white"
    )

    # Cambiar los nombres de la leyenda
    fig.update_traces(name='Total Ingresos', selector=dict(name='total_ingresos'))
    fig.update_traces(name='Total Gastos', selector=dict(name='total_gastos'))
    
    return fig.to_json()

def grafica_ingresos_vs_gastos(proyecto_id):

    # Obtener los ingresos y gastos totales
    df_totales = recalcular_totales_proyecto(proyecto_id)

    # Generar datos de la gráfica
    data = {
        'Categoría': ['Ingresos', 'Gastos', 'IVA'],
        'Montos': [df_totales['total_ingresos'], df_totales['total_gastos'], df_totales['iva_neto']]
    }
    df_bar = pd.DataFrame(data)
    
    # Crear gráfica de líneas usando Plotly Express
    fig = px.bar(df_bar, x='Categoría', y='Montos',color='Categoría',
                 color_discrete_map={
                     'Ingresos': '#6671fa',  # Color para ingresos
                     'Gastos': '#ef5e45',     # Color para gastos
                     'IVA': '#6896f0'       # Color para IVA
                 })

    # Agregar anotaciones para los valores dentro de las barras
    # fig.update_traces(texttemplate='%{y:.3s} MXN', textposition='auto')

    fig.update_layout(
    xaxis_title='Tipo de movimiento',
    yaxis_title='Monto',
    yaxis_tickformat='$,.4s MXN',  # Formato de moneda
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(255, 255, 255, 0.8)',
    font=dict(family="Arial, sans-serif", size=16),
    template="plotly_white"
    )
    
    return fig.to_json()

def grafica_gastos_categoria(proyecto_id):

    # Obtener los gastos por categoria
    df_totales = recalcular_totales_proyecto(proyecto_id)

    total_gastos = df_totales['total_gastos']

    # Calcular los porcentajes
    porcentajes_gastos = [
        (df_totales['gastos_vehiculos'] / total_gastos),
        (df_totales['gastos_generales'] / total_gastos),
        (df_totales['gastos_materiales'] / total_gastos),
        (df_totales['gastos_seguridad'] / total_gastos),
        (df_totales['gastos_equipos'] / total_gastos),
        (df_totales['gastos_mano_obra'] / total_gastos)
    ]

    # Generar datos de la gráfica
    data = {
        'Categoría': ['GastosVehiculos', 'GastosGenerales', 'GastosMateriales', 'GastosSeguridad', 'GastosManoObra', 'GastosEquipos'],
        'Montos': porcentajes_gastos }
    df_bar = pd.DataFrame(data)
    
    # Crear gráfica de líneas usando Plotly Express
    fig = px.bar(df_bar, x='Categoría', y='Montos')

    fig.update_layout(
    xaxis_title='Categoría',
    yaxis_title='Porcentaje de gastos',
    yaxis_tickformat='.0%',
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(255, 255, 255, 0.8)',
    font=dict(family="Arial, sans-serif", size=16),
    template="plotly_white"
    )
    
    return fig.to_json()


