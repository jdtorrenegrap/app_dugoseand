import streamlit as st

def render_faq():
    st.title("Preguntas Frecuentes (FAQ)")

    with st.expander("¿Cómo configurar mi correo para el envío de correos?"):
        st.write("""
        Para configurar tu correo, sigue estos pasos:
        1. Inicia sesión en tu cuenta de correo.
        2. Ve a la opción de "Gestionar cuenta".
        3. Dirígete a la sección de "Seguridad".
        4. Busca la opción de "Contraseña de aplicaciones".
        5. Genera una nueva contraseña de aplicación.
        6. Ingresa esta contraseña generada en la sección de "Contraseña" de nuestra aplicación.
        7. Usa tu correo electrónico habitual en la sección de "Correo electrónico".

        **Nota:** La contraseña generada no es la misma que usas para iniciar sesión en tu correo.
        """)

    with st.expander("¿Cómo sé cuáles son las columnas de mi Excel?"):
        st.write("""
        Para identificar las columnas de tu archivo Excel:
        1. Abre tu archivo Excel.
        2. Observa la primera fila, que generalmente contiene los nombres de las columnas.
        3. Usa estos nombres en la configuración de la aplicación.

        **Ejemplo:**
        - Nombre
        - Correo Electrónico
        """)
       
    with st.expander("¿Cómo sé cuáles son las hojas de mi Excel?"):
        st.write("""
        Para identificar las hojas de tu archivo Excel:
        1. Abre tu archivo Excel.
        2. Observa las pestañas en la parte inferior del archivo, cada pestaña representa una hoja.
        3. Usa el nombre de la hoja que contiene tus datos en la configuración de la aplicación.

        **Ejemplo:**
        - Hoja1
        - Contactos
        """)

    with st.expander("¿Guardan la información de los usuarios?"):
        st.write("""
        No, no guardamos la información de los usuarios. Todos los datos proporcionados se utilizan únicamente para el envío de correos y no se almacenan en nuestros servidores.
        """)