import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles.csv')

st.header('Carros para venda')

build_histogram = st.checkbox('Criar um histograma')
"""Criando uma caixa para o histograna"""

if build_histogram:

    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')          
    
    fig = px.histogram(car_data, x="odometer")
    
    st.plotly_chart(fig, use_container_width=True)

hist_button = st.button('Criar histograma')

"""Cria um histograna"""

if hist_button: 
  
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')          
    
    fig = px.histogram(car_data, x="odometer")
    
    st.plotly_chart(fig, use_container_width=True)


scat_button = st.button('Criar um gráfico de dispersão')

"""Cria um gráfico de dispersão"""

if scat_button:
    st.write('Criando um gráfico de dispersão')

    fig = px.scatter(df, x="odometer", y="price")
    st.plotly_chart(fig)
