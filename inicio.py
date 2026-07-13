import streamlit as st
import pandas as pd
import numpy as np


df = pd.read_csv("nuevo_pib.csv")

st.image("https://www.biobiochile.cl/assets/logos-notas-patrocinadas/6302219_logo_img_patrocinada.png")
st.subheader("Introduccion a la programacion con R y Python")


st.sidebar.header("Filtros de Búsqueda")

paises = df['Country Name']

with st.sidebar:
    st.markdown("Dashboard Interactivo: Crecimiento del PIB (% anual)")
    pais = st.selectbox('escoger pais', paises)
    st.markdown("---")
    st.write("- Génesis Trincado")

st.write (pais)
anios = st.slider('Elige Año', 1961, 2025, value=(1961, 2025)) 

df= pd.DataFrame(np.random.randn(10, 2),columns=['x', 'y'])
st.line_chart(df)





st.link_button("Made by @Sa3hyun", "https://github.com/sa3hyun")