import streamlit as st

#st.title("Primera app")
#st.balloons()

# Crea una página a partir de un archivo de python (cada una en un fichero diferente):
pg_intro = st.Page("intro.py", title="Introducción")

#Páginas EDA
pg_eda_intro = st.Page("seccion_eda/intro_eda.py", title="Primeros pasos")
pg_eda_basica = st.Page("seccion_eda/estadisticos_basicos.py", title="Información básica")

#Necesitamos un atributo "items" (un diccionario) y además que sea iterable
navigation_env = st.navigation(
    {
        "": [pg_intro],
        "EDA": [pg_eda_intro, pg_eda_basica]
    }
)

navigation_env.run()