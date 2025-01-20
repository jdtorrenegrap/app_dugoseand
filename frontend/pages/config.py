import streamlit as st
import re
import base64
import requests

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email)

def is_valid_smtp_server(server):
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, server)

def set_up_credentials():

    # Configuración del correo
    st.header("Configuración del Correo")
    email = st.text_input("Correo electrónico", placeholder="tucorreo@gmail.com")
    if not email:
        st.info("Por favor, ingresa tu correo electrónico.")
    if email and not is_valid_email(email):
        st.error("Por favor, ingresa un correo electrónico válido.")
    
    password = st.text_input("Contraseña", type="password")
    if not password:
        st.info("Por favor, ingresa tu contraseña.")
    
    st.subheader("Configuración de SMTP")
    port = st.text_input("Puerto", placeholder="587", disabled=True)
    
    smtp_server = st.selectbox("Servidor SMTP", ["smtp.gmail.com", "smtp-mail.outlook.com", "Otro proveedor"])
    if smtp_server == "Otro proveedor":
        smtp_server = st.text_input("Ingresa el servidor SMTP de tu proveedor")
        if smtp_server and not is_valid_smtp_server(smtp_server):
            st.error("Por favor, ingresa un servidor SMTP válido.")

    if email and password and smtp_server:
        st.success("Configuración del correo completada.")

        # Envío de correos
        st.header("Enviar correo")
        
        st.subheader("Sube tu archivo Excel")
        excel = st.file_uploader("Selecciona un archivo Excel con tus contactos", type=["xlsx"], key="excel_uploader")
        
        if excel:
            st.subheader("Configura tu archivo Excel")
            columna1 = st.text_input("Nombre de la columna para los nombres de los destinatarios")
            columna2 = st.text_input("Nombre de la columna para los correos electrónicos")
            sheet_name = st.text_input("Nombre de la hoja en el archivo Excel")
            
            if columna1 and columna2 and sheet_name:
                st.subheader("Personaliza tu correo")
                subject = st.text_input("Asunto del correo")
                message = st.text_area("Mensaje del correo (usa [destinatario] para personalizar con el nombre)", placeholder="Ejemplo: Estimado [destinatario]")
                
                if subject and message:
                    if st.button("Enviar"):
                        if email and password and smtp_server and columna1 and columna2 and sheet_name and subject and message:
                            if is_valid_email(email):
                                #diccionario
                                combined_data = {
                                    "config_data": {
                                        "email": email,
                                        "password": password,
                                        "port": "587",
                                        "smtp_server": smtp_server
                                    },
                                    "email_data": {
                                        "excel": base64.b64encode(excel.getvalue()).decode('utf-8'),
                                        "columna1": columna1,
                                        "columna2": columna2,
                                        "sheet_name": sheet_name,
                                        "subject": subject,
                                        "message": message,
                                    }
                                }
                                
                                st.success("Configuración guardada y correo preparado para enviar.")
                                print("Combined Data:", combined_data)
                                
                                # Mostrar ícono de carga mientras se envía el correo
                                with st.spinner('Enviando correo...'):
                                    response = requests.post("http://localhost:8000/send-email", json=combined_data)
                                    if response.status_code == 200:
                                        st.success("Correo enviado exitosamente.")
                                    else:
                                        st.error("Error al enviar el correo.")
                            else:
                                st.error("Por favor, verifica que todos los campos sean correctos.")
                        else:
                            st.error("Por favor, completa todos los campos antes de enviar.")
        else:
            st.info("Por favor, sube un archivo Excel para continuar.")