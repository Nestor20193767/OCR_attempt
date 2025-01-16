import streamlit as st
import pandas as pd
from datetime import datetime




# Crear el diálogo para mostrar el texto
@st.dialog("Mostrar tu texto")
def show_text_dialog(text):
    st.write(text)
    st.session_state.texto = 'existente'
        

if "texto" not in st.session_state:
    texto = st.text_input("Escribe algo...")
    boton = st.button("Got it")
    if boton:
        show_text_dialog(texto)
    










