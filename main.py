import streamlit as st
from jnius import autoclass

def nfc_init():
    try:
        # Importar las clases de Android necesarias a través de Pyjnius
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        NfcAdapter = autoclass('android.nfc.NfcAdapter')

        # Obtener el contexto de la actividad de Android
        context = PythonActivity.mActivity

        # Obtener el adaptador NFC
        nfc_adapter = NfcAdapter.getDefaultAdapter(context)

        if nfc_adapter is None:
            st.error("El dispositivo no tiene soporte NFC.")
        else:
            if nfc_adapter.isEnabled():
                st.success("Adaptador NFC inicializado y habilitado.")
            else:
                st.warning("El adaptador NFC está deshabilitado. Por favor, habilítelo en la configuración.")
    except Exception as e:
        st.error(f"Error al inicializar el adaptador NFC: {e}")

# Crear la interfaz de Streamlit
st.title("Interfaz NFC con Streamlit y Pyjnius")
st.write("Este ejemplo intenta inicializar el adaptador NFC en un dispositivo Android.")

# Botón para inicializar NFC
if st.button("Inicializar Adaptador NFC"):
    nfc_init()
    










