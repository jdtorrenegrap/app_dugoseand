import time
import pandas as pd
import streamlit as st
import re
import base64
import requests

# Función para validar el correo electrónico
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

def set_up_credentials():
    # Configuración del correo
    st.header("Configuración del Correo")
    
    # Ingreso del correo electrónico
    email = st.text_input("Correo electrónico", placeholder="youremail@gmail.com")
    if email and not is_valid_email(email):
        st.error("Por favor, ingresa un correo electrónico válido.")
    
    # Ingreso de la contraseña
    password = st.text_input("Contraseña", type="password")
    
    # Configuración SMTP
    st.subheader("Configuración de SMTP")
    smtp_server = st.selectbox("Servidor SMTP", ["smtp.gmail.com", "smtp-mail.outlook.com"])
    
    if email and password and smtp_server:
        st.success("Configuración del correo completada.")

        # Subida del archivo Excel
        st.header("Enviar correo")
        st.subheader("Sube tu archivo Excel")
        excel = st.file_uploader("Selecciona un archivo Excel con tus contactos", type=["xlsx"], key="excel_uploader")
        
        if excel:
            df = pd.read_excel(excel)
            df_preview = df.iloc[:5, :3]  # Vista previa de las primeras filas y columnas
            st.write("Vista previa del archivo")
            st.dataframe(df_preview)

            # Configuración del archivo Excel
            st.subheader("Configura tu archivo Excel")
            columna1 = st.text_input("Columna de los destinatarios", placeholder="Name")
            columna2 = st.text_input("Columna de los correos electrónicos", placeholder="Email")
            sheet_name = st.text_input("Nombre de la hoja en el archivo Excel", placeholder="Sheet1")
            
            if columna1 and columna2 and sheet_name:
                st.success("Configuración del archivo Excel completada")
                
                # Personalización del correo
                st.subheader("Personaliza tu correo")
                subject = st.text_input("Asunto del correo")
                message = st.text_area("Mensaje del correo (usa [destinatario] para personalizar con el nombre)", placeholder="Ejemplo: Estimado [destinatario]")
                
                if subject and message:
                    if st.button("Enviar"):
                        if email and password and smtp_server and columna1 and columna2 and sheet_name and subject and message:
                            if is_valid_email(email):
                                
                                # Preparación de los datos para enviar
                                combined_data = {
                                    "smtp_config": {
                                        "smtp_server": smtp_server,
                                        "port": 587,
                                        "email": email,
                                        "password": password
                                    },
                                    "email_data": {
                                        "subject": subject,
                                        "message": message,
                                        "excel_file": base64.b64encode(excel.getvalue()).decode('utf-8'),
                                        "sheet_name": sheet_name,
                                        "column_x": columna1,
                                        "column_y": columna2,
                                    }
                                }
                                
                                # Mostrar spinner mientras se procesa la solicitud
                                with st.spinner('Procesando solicitud, por favor espere...'):
                                    time.sleep(10)
                                   
                                with st.spinner('Enviando correo...'):
                                    try:
                                        response = requests.post("http://localhost:8000/send-email", json=combined_data)
                                        response_data = response.json()
                                        if response.status_code == 200:
                                            if "error" in response_data:
                                                st.error(f"{response_data['error']}")
                                            else:
                                                st.success("Correo enviado exitosamente.")
                                        else:
                                            st.error(f"{response_data['detail']}")
                                        return True
                                    except requests.exceptions.RequestException as e:
                                        st.error(f"Error al enviar el correo: {e}")
                                        return False
                            else:
                                st.error("Por favor, verifica que todos los campos sean correctos.")
                        else:
                            st.error("Por favor, completa todos los campos antes de enviar.")
        else:
            st.info("Por favor, sube un archivo Excel para continuar.")