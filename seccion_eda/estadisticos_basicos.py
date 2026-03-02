import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.markdown("Texto de prueba")

st.markdown("## Datos Crudos del dataset")

# Cargamos datos en pandas
df = pd.read_csv("bike_dataset_day.csv")
# Mostramos los datos
st.dataframe(df.head(500))

st.markdown("## Datos sobre el dataset")
# Puedo mostrar informacion general de forma un poco fea
st.markdown(df.describe().T)
# O puedo mostrarlo de forma más bonita, como un dataframe
st.dataframe(df.describe().T)

st.markdown("## Estadísticos de las variables")
# Saco los dtos que me interesa del dataframe y lo muestro bonito
st.dataframe(df[['dteday', 'temp',  'windspeed', 'hum', 'cnt']].describe())
# Ahora hago la traspuesta y me quedo solo con algunas
st.dataframe(df[['dteday', 'temp',  'windspeed', 'hum', 'cnt']].describe().T[['count', 'std', 'mean']])


st.markdown("## Distribución de las variables")
# Lo creamos en columnas primero
col1 = st.columns(3)
with col1[0]:
    # Generamos la figura y ejes y luego añadimos el plot
    fig, ax = plt.subplots()
    sns.histplot(df['temp'], kde=True)
    plt.title('Distribucion Temp.')
    st.pyplot(fig)
with col1[1]:
    # Generamos la figura y ejes y luego añadimos el plot
    fig, ax = plt.subplots()
    sns.histplot(df['hum'], kde=True)
    plt.title('Distribucion Humedad.')
    st.pyplot(fig)
with col1[2]:
    # Generamos la figura y ejes y luego añadimos el plot
    fig, ax = plt.subplots()
    sns.histplot(df['windspeed'], kde=True)
    plt.title('Distribucion windspeed.')
    st.pyplot(fig)

# Añadimos una linea para separar el plot que nos interesa
st.markdown("---")
# Generamos la figura y ejes y luego añadimos el plot de lo que nos interesa
cols_target, = st.columns(1)
with cols_target:
    fig, ax = plt.subplots()
    sns.histplot(df['cnt'], kde=True)
    plt.title('Distribucion de ventas.')
    st.pyplot(fig)


st.markdown("## Matriz de correlación")
# Usamos una función de pandas en vez de a mano:
# st.markdown(df.corr()) # Pero esto va a dar errror poque hay columnas como la fecha que no tienen ni sentido apra esto
# Seleccionamos las columnas:
cols_interes = ['temp', 'hum', 'windspeed', 'casual', 'cnt']
st.markdown(df[cols_interes].corr())
# Y lo mostramos bonito, como un dataframe:
st.dataframe(df[cols_interes].corr())
# Igual pero con un mapa de calor:
matriz_correlacion = df[cols_interes].corr()
sns.heatmap(matriz_correlacion)
col, = st.columns(1)
with col:
    fig, ax = plt.subplots()
    sns.heatmap(matriz_correlacion, annot=True)
    plt.title("Matriz correlacion con cnt")
    st.pyplot(fig)

