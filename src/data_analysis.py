import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.io as pio
import statsmodels.api as sm

pio.renderers.default = "browser"

# Configuración inicial
pd.set_option("display.max_columns", None)
plt.style.use("ggplot")

# Cargar los datos
try:
    df = pd.read_csv("data/arboles_bogota.csv")
except FileNotFoundError:
    raise FileNotFoundError("El archivo 'data/arboles_bogota.csv' no se encontró.")

# Validar que el DataFrame no esté vacío
if df.empty:
    raise ValueError("El archivo CSV está vacío.")

## 1. Análisis General
print(f"Total de registros: {len(df)}")
print(f"Columnas disponibles: {list(df.columns)}")
print("\nResumen estadístico:")
print(df.describe(include="all").T)

## 2. Visualizaciones

# 2.1 Distribución por Localidad
if "Localidad" in df.columns:
    localidad_counts = df["Localidad"].value_counts().reset_index()
    localidad_counts.columns = ["Localidad", "Cantidad"]

    fig1 = px.bar(
        localidad_counts,
        x="Localidad",
        y="Cantidad",
        title="Distribución de Árboles por Localidad",
        labels={"Localidad": "Localidad", "Cantidad": "Cantidad"},
        color="Localidad",
    )
    fig1.update_layout(xaxis_tickangle=-45)
    fig1.show()

# 2.2 Top 20 Especies
if "Especie" in df.columns:
    top_especies = df["Especie"].value_counts().nlargest(20).reset_index()
    top_especies.columns = ["Especie", "Cantidad"]

    fig2 = px.bar(top_especies, x="Especie", y="Cantidad", title="Top 20 Especies Más Comunes", color="Especie")
    fig2.update_layout(xaxis_tickangle=-45)
    fig2.show()

# 2.3 Estado de los Árboles
estado_campos = ["Estado fuste", "Estado Copa", "Estado Raiz", "Estado FitoSanitario"]
estado_validos = [col for col in estado_campos if col in df.columns]

fig3 = make_subplots(rows=2, cols=2, subplot_titles=estado_validos)

for i, estado in enumerate(estado_validos, 1):
    counts = df[estado].value_counts().reset_index()
    counts.columns = [estado, "Cantidad"]

    fig3.add_trace(
        go.Bar(x=counts[estado], y=counts["Cantidad"], name=estado), row=(i - 1) // 2 + 1, col=(i - 1) % 2 + 1
    )

fig3.update_layout(height=800, width=1000, title_text="Distribución de Estados de los Árboles")
fig3.show()

# 2.4 Medidas Físicas
medidas = ["PAP", "DAP", "Altura Total", "Altura Comercial", "Diam. Copa Polar", "Diam. Copa Ecuatorial"]
medidas_validas = [col for col in medidas if col in df.columns]

fig4 = make_subplots(rows=2, cols=3, subplot_titles=medidas_validas)

for i, medida in enumerate(medidas_validas, 1):
    fig4.add_trace(go.Box(y=df[medida].dropna(), name=medida), row=(i - 1) // 3 + 1, col=(i - 1) % 3 + 1)

fig4.update_layout(height=600, width=1000, title_text="Distribución de Medidas Físicas")
fig4.show()

# 2.5 Mapa
if {"Latitud", "Longitud"}.issubset(df.columns):
    df_mapa = df.dropna(subset=["Latitud", "Longitud"])
    fig5 = px.scatter_map(
        df_mapa,
        lat="Latitud",
        lon="Longitud",
        color="Localidad",
        hover_name="Especie",
        hover_data=["Estado General", "Riesgo"],
        zoom=10,
        height=600,
        title="Distribución Geográfica de los Árboles",
    )
fig5.update_layout(mapbox_style="open-street-map")
fig5.show()

# 2.6 Correlación
numeric_cols = df.select_dtypes(include=np.number).columns
if len(numeric_cols) >= 2:
    corr_matrix = df[numeric_cols].corr()
    fig6 = go.Figure(
        data=go.Heatmap(z=corr_matrix, x=corr_matrix.columns, y=corr_matrix.columns, colorscale="RdBu", zmin=-1, zmax=1)
    )
    fig6.update_layout(title="Matriz de Correlación entre Variables Numéricas")
    fig6.show()

# 2.7 Distribución por Estrato
if "Estrato" in df.columns:
    fig7 = px.pie(df, names="Estrato", title="Distribución de Árboles por Estrato")
    fig7.show()

# 2.8 Riesgo por Especie
if {"Especie", "Riesgo"}.issubset(df.columns):
    riesgo_especie = pd.crosstab(df["Especie"], df["Riesgo"])
    if "Alto" in riesgo_especie.columns:
        riesgo_top10 = riesgo_especie.nlargest(10, "Alto").reset_index()
        fig8 = px.bar(
            riesgo_top10,
            x="Especie",
            y=["Bajo", "Medio", "Alto"],
            barmode="group",
            title="Top 10 Especies con Mayor Riesgo Alto",
            labels={"value": "Cantidad", "variable": "Nivel de Riesgo"},
        )
        fig8.show()

## 3. Análisis Adicionales

# Interés patrimonial
if "Interes patrimonial" in df.columns:
    patrimonial = df["Interes patrimonial"].value_counts(normalize=True) * 100
    print("\nPorcentaje de árboles con interés patrimonial:")
    print(patrimonial)

# Especies con mayor altura
if {"Especie", "Altura Total"}.issubset(df.columns):
    print("\nEspecies con mayor altura promedio:")
    print(df.groupby("Especie")["Altura Total"].mean().nlargest(10).reset_index())

# Tratamientos aplicados
if "Tratamiento" in df.columns:
    print("\nDistribución de tratamientos aplicados:")
    print(df["Tratamiento"].value_counts().reset_index())
