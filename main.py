import streamlit as st
import pywhatkit as pwk
import folium
from streamlit_folium import st_folium

# Función para enviar el mensaje de WhatsApp
def send_whatsapp_message(message, phone_number, location=None):
    if location:
        lat, lon = location
        # Crear un enlace de Google Maps
        location_link = f'https://www.google.com/maps?q={lat},{lon}'
        message += f' Puedes ver la ubicación aquí: {location_link}'
        
    # Enviar mensaje usando pywhatkit
    # Establece la hora de envío (en formato de 24 horas, por ejemplo, 14:30 para las 2:30 PM)
    # La función sendwhatmsg_envía el mensaje automáticamente a la hora indicada.
    # Se debe proporcionar un número de teléfono, con el código de país.
    pwk.sendwhatmsg_instantly(f'whatsapp://{phone_number}', message)

# Función para mostrar el mapa
def show_map(lat, lon):
    # Crear el mapa
    map = folium.Map(location=[lat, lon], zoom_start=12)
    folium.Marker([lat, lon], popup="Ubicación enviada").add_to(map)
    # Mostrar el mapa en Streamlit
    st_folium(map, width=700, height=500)

# Interfaz de Streamlit
st.title('Enviar mensaje de WhatsApp con ubicación')

# Entrada del mensaje
message = st.text_area('Escribe tu mensaje')

# Entrada de la ubicación
lat = st.number_input('Latitud', value=0.0)
lon = st.number_input('Longitud', value=0.0)

# Número de teléfono (debe ser en formato internacional)
phone_number = st.text_input('Número de teléfono (incluye el código de país)', '+1234567890')

# Enviar el mensaje
if st.button('Enviar mensaje'):
    if message and phone_number:
        if lat != 0.0 and lon != 0.0:
            # Mostrar el mapa con la ubicación
            show_map(lat, lon)
            # Enviar el mensaje con la ubicación
            send_whatsapp_message(message, phone_number, location=(lat, lon))
            st.success('¡Mensaje enviado con éxito!')
        else:
            # Enviar mensaje sin ubicación
            send_whatsapp_message(message, phone_number)
            st.success('¡Mensaje enviado sin ubicación!')
    else:
        st.error('Por favor, ingresa un mensaje y un número de teléfono.')
