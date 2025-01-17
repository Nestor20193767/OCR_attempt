import streamlit as st
from datetime import datetime
import pytz

# Configurar la zona horaria de Perú
peru_timezone = pytz.timezone("America/Lima")

# Contenedor para el cuadro con la hora
st.markdown("""
<div style="
    border: 1px solid #d6d6d6; 
    border-radius: 8px; 
    padding: 20px; 
    background-color: #ffffff;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
    <h2 style="text-align: center; color: #19348f;">Hora Actual</h2>
    <div id="hora" style="font-size: 24px; text-align: center; color: #000;">
        Aquí se mostrará la hora.
    </div>
</div>
""", unsafe_allow_html=True)

# Mostrar y actualizar la hora periódicamente
hora_placeholder = st.empty()

# Streamlit ya controla el refresco de la página
while True:
    hora_actual = datetime.now(peru_timezone).strftime("%H:%M:%S")
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
    st.experimental_rerun()  # Refresca la app















