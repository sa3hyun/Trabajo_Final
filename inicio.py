import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("pib.csv")

st.sidebar.header("Filtros de Búsqueda")
lista_paises = sorted(df['Country Name'].unique())
pais = st.sidebar.selectbox("Selecciona un País:", lista_paises)
with st.sidebar:
    st.markdown("### Dashboard Interactivo: Crecimiento del PIB (% anual)")

st.subheader("made by sa3hyun", text_alignment="center")