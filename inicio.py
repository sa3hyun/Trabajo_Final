import streamlit as st
import pandas as pd


df = pd.read_csv("nuevo_pib.csv")

st.image("https://www.biobiochile.cl/assets/logos-notas-patrocinadas/6302219_logo_img_patrocinada.png")
st.subheader("Introduccion a la programacion con R y Python")


st.sidebar.header("Filtros de Búsqueda")

with st.sidebar:
    st.markdown("### Dashboard Interactivo: Crecimiento del PIB (% anual)")

st.link_button("Made by @Sa3hyun", "https://github.com/sa3hyun")