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


#Coloco un slider para elegir de que año hasta que año quieren visualizar los datos mostrados
#Dentro del grafico que se muestra más abajo
anios = st.slider('Elige Año', 1961, 2025, value=(1961, 2025)) 


#Primero creo df_pais para poder seleccionar con mas facilidad el pais que se selecciono en la selectbox
df_pais = df[df['Country Name'] == pais]
df_pais.drop(columns=['Unnamed: 0','Country Code'], inplace=True)

#Hago lo mismo pero con los años seleccionados

#(El codigo de aca abajo estaba mal, lo arregle y lo deje comentado para que vean como estaba antes :p)
#anios_selec = [for a in range anios in df.columns] }

## 1. Creamos las listas de años correctamente
anios_txt = [str(a) for a in range(anios[0], anios[1] + 1)]
anios_int = [int(a) for a in range(anios[0], anios[1] + 1)]

# Filtro los datos correctamente usando df_pais
# Extraigo la serie de datos del país para los años seleccionados
s_pais = df_pais[anios_txt].iloc[0]

# Saco la media del PIB del país seleccionado
p_pais = s_pais.mean()

#df_pais[]

#Ahora saco el promedio de america
datos_america = df[df['Country Name'].isin(paises)]

promedio_america = (datos_america[anios_txt].mean(axis=1).mean())

#Ahora hago la diferencia
diferencia = p_pais - promedio_america

#Hago que se muestre el pais anteriormente seleccionado (Texto)
st.write (pais)

#Hago el grafico del crecimiento del PIB 
fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(anios_int, s_pais.values,
        label=pais)

prom_anual = datos_america[anios_txt].mean(axis=0)

ax.plot(anios_int, prom_anual.values,
        label='Promedio América')

ax.set_title(f'Crecimiento del PIB (% anual)')
ax.set_ylabel("%")

#Cuando hice el grafico note que algunos años los mostraba como "1999.0" y otros como
#"2000.0" y eso no me gustaba, asi que lo arregle con el siguiente codigo que encontre 
#en la pagina de streamlit
ax.set_xticks(anios_int[::5]) 

#Hago las KPIs
col1, col2, col3 = st.columns(3)
with col1:
     with st.container(border=True):
         st.metric("Promedio PIB país", f"{p_pais:.2f}%")
with col2:
     with st.container(border=True):
         st.metric("Promedio PIB (América)", f"{promedio_america:.2f}%")
with col3:
     with st.container(border=True):
         st.metric("Diferencia", f"{diferencia:.2f}%")

#Y muestro el gráfico en Streamlit

st.pyplot(fig)

#Y fin :)





st.link_button("Made by @Sa3hyun", "https://github.com/sa3hyun")