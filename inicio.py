import streamlit as st
import pandas as pd


df = pd.read_csv("nuevo_pib.csv")


st.sidebar.header("Filtros de Búsqueda")

with st.sidebar:
    st.markdown("### Dashboard Interactivo: Crecimiento del PIB (% anual)")

st.subheader("made by sa3hyun", text_alignment="center")