import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv("pib.csv")

st.sidebar.header("Filtros de Búsqueda")
with st.sidebar:
    st.markdown("### Dashboard Interactivo: Crecimiento del PIB (% anual)")

st.subheader("made by sa3hyun", text_alignment="center")