import pandas as pd
import plotly.graph_objects as go  # Importación de plotly.graph_objects como go
import plotly.express as px
import streamlit as st

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

st.header('Proyecto Sprint 7')

# Crear un botón en la aplicación Streamlit
hist_button = st.button('Construir Gráfico')
disp_check = st.checkbox('Construir gráfico de dispersión')

# Lógica a ejecutar cuando se hace clic en el botón
if hist_button:
    if disp_check:
        st.write('Creación de gráfico de dispersión para el conjunto de datos deanuncios de venta de coches')

        fig = go.Figure(data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])

        fig.update_layout(title_text='Relación entre Odómetro y Precio')

        st.plotly_chart(fig, use_container_width=True)
        
    else:
        st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')    
        fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    
        fig.update_layout(title_text='Distribución del Odómetro')
 
        st.plotly_chart(fig, use_container_width=True) 


