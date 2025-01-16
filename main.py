import streamlit as st
import pandas as pd
from datetime import datetime




# Función para mostrar el diálogo con el texto escrito
@st.dialog("Mostrar tu texto")
def show_text_dialog():
    if "user_message" in st.session_state:
        # Mostrar el mensaje que se ingresó previamente en el cuadro de texto
        st.write(f"Tu mensaje es: {st.session_state.user_message}")
    else:
        st.write("No has ingresado ningún texto aún.")

# Mostrar la interfaz principal para escribir y un botón
st.write("Ingresa un texto y presiona el botón para mostrarlo en el diálogo.")

user_text = st.text_input("Escribe algo aquí...")

# Botón para activar el diálogo y mostrar el texto escrito
if st.button("Mostrar en el diálogo"):
    if user_text:  # Si hay texto ingresado
        st.session_state.user_message = user_text
        st.rerun()  # Recargar la página para activar el diálogo y mostrar el texto
    else:
        st.write("Por favor, ingresa algo antes de presionar el botón.")








