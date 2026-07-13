import streamlit as st
import pandas as pd
import numpy as np

#Importo CSV limpio
df = pd.read_csv("nuevo_pib.csv")

#Imagen y titulo
st.image("https://www.biobiochile.cl/assets/logos-notas-patrocinadas/6302219_logo_img_patrocinada.png")
st.subheader("Introduccion a la programacion con R y Python")

#Agrego sidebar.header (Header en la zona izquierda) con el titulo de filtros de busqueda
st.sidebar.header("Filtros de Búsqueda")

#hago que el df "paises" solo tome los datos de las columnas dentro de "Country name"(Son los paises)
paises = df['Country Name']

#Agrego una barra lateral
#Coloco un titulo
#Coloco una selectbox para que puedan elegir el pais que desean ver
#Y procuro meter esto dentro de "pais" para despues utilizarlo
#Una linea para separar
#Y escribo mi nombre WOW
with st.sidebar:
    st.markdown("Dashboard Interactivo: Crecimiento del PIB (% anual)")
    pais = st.selectbox('escoger pais', paises)
    st.markdown("---")
    st.write("- Génesis Trincado")

#Hago que se muestre el pais anteriormente seleccionado (Texto)
st.write (pais)
#Coloco un slider para elegir de que año hasta que año quieren visualizar los datos mostrados
#Dentro del grafico que se muestra más abajo
anios = st.slider('Elige Año', 1961, 2025, value=(1961, 2025)) 

#Muesto el grafico tomando en cuenta el pais seleccionado y los años desde hasta.
df= pd.DataFrame(np.random.randn(10, 2),columns=['x', 'y'])
st.line_chart(df)

#Agrego cajas de información como el "Promedio PIB (pais)", "Promedio PIB" y "Diferencia"
#Con sus respectivos datos 


#Y fin :)

st.link_button("Made by @Sa3hyun", "https://github.com/sa3hyun")