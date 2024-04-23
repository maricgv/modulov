# Importar Streamlit
import streamlit as st

# Importar librerías necesarias
import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.io as pio

# Título de la aplicación
st.title('LGBTQ+ EN EL MUNDO')
st.markdown("#### Prof. Jésica Edith Tapia Reyes")
st.markdown('##### Alumna: *María del Carmen González Videgaray*')

# Barra lateral

with st.sidebar:
    st.image("Bandera.png")
    st.write("En este dashboard se muestran los resultados de una búsqueda en la base de datos Scopus realizada el 17 de abril 2024, con el tópico LGBTQ+.")
    st.markdown("#### Insights:")


# Lectura de datos
data = pd.read_csv("Scopus-10-Analyze-Year.csv")
x_values = data["Año"]
y_values = data["Documentos"]

# Se crea la línea de serie de tiempo
line_trace = go.Scatter(
    x=x_values,
    y=y_values,
    mode='lines',
    name='Tendencia'
)

# Se crea la línea de serie de tiempo
scatter_trace = go.Scatter(
    x=x_values,
    y=y_values,
    mode='markers',
    name='Valor'
)

# Creación de la salida
layout = go.Layout(
    title='Documentos académicos LGBTQ+ por año. <br>Fuente: Scopus (240416).',
    xaxis=dict(title='Año'),
    yaxis=dict(title='Documentos'),
    annotations=[
        dict(
            x=2023,  # Coordenada x
            y=1773,  # Coordenada y
            text='Crecimiento',  # Texto
            showarrow=True,  # Mostrar flecha
            arrowhead=7,  # Estilo punta flecha
            ax=0,  # Coordenada x para la flecha
            ay=-40  # Coordenada y para la flecha
        )
    ]
)

# Se crea la figura
fig = go.Figure(data=[line_trace,scatter_trace], layout=layout)

# Se muestra en el cuaderno
st.plotly_chart(fig)


# Simulated data
data = pd.read_csv("Scopus-10-Analyze-Country2.csv")
categories = data["País"]
values = data["Documentos"]

# Create a bar trace
trace = go.Bar(
    x=categories,
    y=values,
    marker=dict(color='purple')  # Customizing bar color
)

# Create layout
layout = go.Layout(
    title='Los diez países con mayor número de documentos académicos LGBTQ+.<br>Fuente: Scopus (240417).',
    xaxis=dict(title='Países'),
    yaxis=dict(title='Documentos')
)

# Create figure
fig = go.Figure(data=[trace], layout=layout)

# Show the plot in Jupyter Notebook
st.plotly_chart(fig)

# Sample data
data = pd.read_csv("Scopus-10-Analyze-Subject2.csv")
labels = data["Área"]
values = data["Documentos"]

# Creating the pie chart
fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.3)])

# Customizing layout
fig.update_layout(
    title_text="Documentos LGBTQ+ por área de conocimiento. <br>Fuente: Scopus (240417)",
    annotations=[dict(text='Total', x=0.5, y=0.5, font_size=20, showarrow=False)]
)

st.plotly_chart(fig)

# Lectura de datos
data = pd.read_csv("Scopus-10-Analyze-SourceRev.csv")
x_values = data["Anio"]
y1_values = data["Journal of Gay and Lesbian Social Services"]
y2_values = data["Journal of LGBT Youth"]
y3_values = data["Journal of Homosexuality"]
y4_values = data["Psychology of Sexual Orientation and Gender Diversity"]
y5_values = data["Journal of Gay and Lesbian Mental Health"]

# Se crea la línea de serie de tiempo 1
line_trace1 = go.Scatter(
    x=x_values,
    y=y1_values,
    mode='lines',
    name='Journal of Gay and Lesbian Social Services'
)

# Se crean los marcadores 1
scatter_trace1 = go.Scatter(
    x=x_values,
    y=y2_values,
    mode='markers',
    name='Valor JGLSS'
)

# Se crea la línea de serie de tiempo 2
line_trace2 = go.Scatter(
    x=x_values,
    y=y2_values,
    mode='lines',
    name='Journal of LGBT Youth'
)

# Se crean los marcadores 2
scatter_trace2 = go.Scatter(
    x=x_values,
    y=y1_values,
    mode='markers',
    name='Valor JLY'
)

# Se crea la línea de serie de tiempo 3
line_trace3 = go.Scatter(
    x=x_values,
    y=y3_values,
    mode='lines',
    name='Journal of Homosexuality'
)

# Se crean los marcadores 3
scatter_trace3 = go.Scatter(
    x=x_values,
    y=y3_values,
    mode='markers',
    name='Valor JH'
)

# Se crea la línea de serie de tiempo 4
line_trace4 = go.Scatter(
    x=x_values,
    y=y4_values,
    mode='lines',
    name='Psychology of Sexual Orientation and Gender Diversity'
)

# Se crean los marcadores 4
scatter_trace4 = go.Scatter(
    x=x_values,
    y=y4_values,
    mode='markers',
    name='Valor PSOGD'
)

# Se crea la línea de serie de tiempo 5
line_trace5 = go.Scatter(
    x=x_values,
    y=y5_values,
    mode='lines',
    name='Journal of Gay and Lesbian Mental Health'
)

# Se crean los marcadores 5
scatter_trace5 = go.Scatter(
    x=x_values,
    y=y5_values,
    mode='markers',
    name='Valor JGLMH'
)

# Creación de la salida
layout = go.Layout(
    title='Documentos académicos LGBTQ+ por fuente (journal). <br>Fuente: Scopus (240416).',
    xaxis=dict(title='Año'),
    yaxis=dict(title='Documentos'),
)

# Se crea la figura final
fig = go.Figure(data=[line_trace1,scatter_trace1,
                      line_trace2,scatter_trace2,
                      line_trace3,scatter_trace3,
                      line_trace4,scatter_trace4,
                      line_trace5,scatter_trace5], layout=layout)


# Se muestra en el cuaderno
st.plotly_chart(fig)
    
