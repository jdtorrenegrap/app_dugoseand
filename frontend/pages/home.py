import streamlit as st
from config import set_up_credentials
from question import render_faq


def render_home():

    # Descripción general
    st.subheader("Automatización inteligente de correos electrónicos")
    st.write("""
    En DugoSeand, estamos comprometidos a hacer que el envío de correos masivos sea rápido, seguro y eficiente. 
    Con nuestra herramienta, puedes:
    - Subir un archivo Excel con tus contactos.
    - Personalizar un mensaje adaptado a tus necesidades.
    - Enviar correos a múltiples destinatarios con tan solo unos clics.
    """)

    # Sección "¿Cómo funciona?"
    st.markdown("### ¿Cómo funciona?")
    st.markdown("""
    1. **Sube tu archivo Excel**: Incluye las direcciones de correo y otra información relevante que necesites.
    2. **Configura tus credenciales**: Proporciona tus datos de correo de forma segura para realizar los envíos.
    3. **Escribe tu mensaje**: Personaliza el asunto y el cuerpo del correo según tus necesidades.
    4. **Envía los correos**: Nosotros nos encargamos del proceso y te mostramos los resultados de manera detallada.
    """)

    # Sección de contacto
    st.markdown("### ¿Necesitas ayuda?")
    st.write("""
    Si tienes preguntas o necesitas soporte, no dudes en contactarnos:
    - **Correo electrónico**: email@autotesthub.8shield.net
    """)

if __name__ == "__main__":
    # Configuración inicial de la app
    st.set_page_config(
        page_title="A Coffee and seend",
        page_icon="",
        layout="centered",
    )

    # Crear un menú en la barra lateral
    

    # Crear pestañas
    tab1, tab2, tab3 = st.tabs(
        ["Inicio", "Configuración y Envío de Correos", "FQA"]
    )

    with tab1:
        render_home()
    
    with tab2:
        set_up_credentials()

    with tab3:
        render_faq()