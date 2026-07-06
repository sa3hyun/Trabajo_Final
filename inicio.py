import streamlit as st
import pandas as pd


df = pd.read_csv("pib.csv")
df.info()

nulos = df.isnull().sum().sort_values(ascending=False)
nulos[nulos > 0]


st.sidebar.header("Filtros de Búsqueda")

with st.sidebar:
    st.markdown("### Dashboard Interactivo: Crecimiento del PIB (% anual)")

st.subheader("made by sa3hyun", text_alignment="center")