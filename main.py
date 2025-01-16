import streamlit as st
import pandas as pd
from datetime import datetime




# Crear el diálogo para mostrar el texto
@st.dialog("Mostrar tu texto")
def show_text_dialog():
    user_text = st.text_input("Escribe algo aquí...")
    
    # Botón para mostrar el texto ingresado en el diálogo
    if st.button("Mostrar en el diálogo"):
        if user_text:
            st.session_state.user_message = user_text
            st.rerun()  # Recargar la página para activar el diálogo
        else:
            st.write("Por favor, ingresa algo antes de presionar el botón.")

# Verificar si ya se ha guardado el texto en el estado de la sesión
if "user_message" in st.session_state:
    st.write(f"Tu mensaje es: {st.session_state.user_message}")
else:
    st.write("Ingresa un texto y presiona el botón para mostrarlo en el diálogo.")








