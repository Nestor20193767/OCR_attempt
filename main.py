import streamlit as st
from datetime import datetime
import pytz
import time

# Configurar la zona horaria de Perú
peru_timezone = pytz.timezone("America/Lima")

# Contenedor para el cuadro
with st.container():
    st.markdown("""
    <div style="
        border: 1px solid #d6d6d6; 
        border-radius: 8px; 
        padding: 20px; 
        background-color: #ffffff;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
        <h2 style="text-align: center; color: #19348f;">Hora Actual</h2>
        <div id="hora" style="font-size: 24px; text-align: center; color: #000;">
            Cargando...
        </div>
    </div>
    """, unsafe_allow_html=True)

# Elemento vacío para actualizar la hora
hora_placeholder = st.empty()

# Actualizar la hora en tiempo real
while True:
    # Obtener la hora actual
    hora_actual = datetime.now(peru_timezone).strftime("%H:%M:%S")
    # Actualizar el cuadro con la hora actual
    hora_placeholder.markdown(f"""
    <div style="
        border: 1px solid #d6d6d6; 
        border-radius: 8px; 
        padding: 20px; 
        background-color: #ffffff;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
        <h2 style="text-align: center; color: #19348f;">Hora Actual</h2>
        <div style="font-size: 24px; text-align: center; color: #000;">
            {hora_actual}
        </div>
    </div>
    """, unsafe_allow_html=True)
    time.sleep(1)  # Actualizar cada segundo














