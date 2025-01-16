import streamlit as st
import pandas as pd
from datetime import datetime






# Crear el diálogo de Streamlit
@st.dialog("Mostrar tu texto")
def show_text_dialog():
    # Crear un campo de entrada para texto
    user_text = st.text_input("Escribe algo aquí...")
    
    # Cuando el usuario presiona el botón, mostrar el texto en el diálogo
    if st.button("Mostrar en el diálogo"):
        st.session_state.user_message = user_text
        st.rerun()  # Recargar la aplicación para mostrar el mensaje en el diálogo

# Verificar si ya hay un mensaje guardado en el estado de sesión
if "user_message" not in st.session_state:
    st.write("Ingresa un texto y presiona el botón para mostrarlo en el diálogo.")
else:
    # Mostrar el mensaje ingresado en el diálogo
    st.write(f"Tu mensaje es: {st.session_state.user_message}")







