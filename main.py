import streamlit as st
import pandas as pd
from datetime import datetime

hoy = datetime.now()
dia = hoy.day

# Crear el diálogo para mostrar el texto
@st.dialog("Mostrar tu texto")
def show_text_dialog(text):
    st.write(text)
    #st.session_state.texto = 'existente'
        
import nfc
clf = nfc.ContactlessFrontend()

# Obtener la lista de dispositivos NFC disponibles
devices = clf.list_devices()

st.write(devices)

texto = st.text_input("Escribe algo...")
boton = st.button("Got it")
st.write(hoy.date())
if boton:
    if dia == 16:
        show_text_dialog(texto)
    










