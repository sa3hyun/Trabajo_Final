import streamlit as st
import pandas as pd
import numpy as np


df = pd.read_csv("nuevo_pib.csv")

st.image("https://www.biobiochile.cl/assets/logos-notas-patrocinadas/6302219_logo_img_patrocinada.png")
st.subheader("Introduccion a la programacion con R y Python")


st.sidebar.header("Filtros de Búsqueda")

paises = df['Country Name']
año = df[['1961', '1962', '1963', '1964', '1965', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025']]
st.write(paises)

with st.sidebar:
    st.markdown("Dashboard Interactivo: Crecimiento del PIB (% anual)")
    st.selectbox('escoger pais', paises)
    st.markdown("---")
    st.write("- Génesis Trincado")

df= pd.DataFrame(np.random.randn(10, 2),columns=['x', 'y'])
st.line_chart(df)

#st.slider('Elige Año', año) 



st.link_button("Made by @Sa3hyun", "https://github.com/sa3hyun")