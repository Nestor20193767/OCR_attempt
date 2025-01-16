import streamlit as st
from smartcard.System import readers
from smartcard.util import toHexString

def list_readers():
    available_readers = readers()
    if not available_readers:
        return None
    return available_readers

def read_card(reader):
    try:
        # Abrir la conexión con el lector de tarjetas
        connection = reader.createConnection()
        connection.connect()

        # Comando APDU para seleccionar un archivo en la tarjeta (esto puede variar dependiendo de la tarjeta)
        command = [0x00, 0xA4, 0x04, 0x00, 0x00]  # Comando de selección de archivo
        response, sw1, sw2 = connection.transmit(command)

        # Mostrar la respuesta de la tarjeta en formato hexadecimal
        return toHexString(response), f"Estado de la respuesta: {sw1} {sw2}"
    except Exception as e:
        return None, f"Error al leer la tarjeta: {str(e)}"

# Título de la aplicación Streamlit
st.title("Interfaz de Lectura de Tarjetas Inteligentes")

# Listar los lectores disponibles
available_readers = list_readers()

if available_readers is None:
    st.write("No se encontraron lectores de tarjetas.")
else:
    # Mostrar la lista de lectores y permitir al usuario seleccionar uno
    reader_names = [reader.name for reader in available_readers]
    selected_reader_name = st.selectbox("Selecciona un lector de tarjetas:", reader_names)

    # Leer la tarjeta con el lector seleccionado
    selected_reader = next(reader for reader in available_readers if reader.name == selected_reader_name)
    if st.button("Leer Tarjeta"):
        response, status = read_card(selected_reader)

        if response:
            st.write(f"Respuesta de la tarjeta: {response}")
        else:
            st.write(status)

    










