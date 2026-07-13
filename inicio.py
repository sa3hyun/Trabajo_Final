import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


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
#st.write (pais)
#Coloco un slider para elegir de que año hasta que año quieren visualizar los datos mostrados
#Dentro del grafico que se muestra más abajo
anios = st.slider('Elige Año', 1961, 2025, value=(1961, 2025)) 


#Primero creo df_pais para poder seleccionar con mas facilidad el pais que se selecciono en la selectbox
df_pais = df[df['Country Name'] == pais]
df_pais.drop(columns=['Unnamed: 0','Country Code'], inplace=True)
st.write (df_pais)
#Hago lo mismo pero con los años seleccionados
#anios_selec = [for a in range anios in df.columns]

anios_txt = [str(a) for a in range(anios[0], anios[1])]
#st.write(anios_txt)

anios_int = [int(a) for a in range(anios[0], anios[1])]
#st.write(anios_int) 

df_pais[]

#Muesto el grafico tomando en cuenta el pais seleccionado y los años desde hasta.

x = anios_int
y = df_pais
plt.plot(x, y, color='blue', linestyle='dashed', linewidth=2.5, marked='o')
plt.title("Metricas Anuales")
plt.xlabel(Años)
plt.ylabel(PIB)
st.pyplot(fig)

#Agrego cajas de información como el "Promedio PIB (pais)", "Promedio PIB" y "Diferencia"
#Con sus respectivos datos 

st.metric 

#Y fin :)


st.link_button("Made by @Sa3hyun", "https://github.com/sa3hyun")