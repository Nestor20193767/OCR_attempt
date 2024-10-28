import streamlit as st
from PIL import Image
import easyocr

# Título de la aplicación
st.title("OCR con Streamlit y EasyOCR")

# Cargar la imagen desde el usuario
imagen_subida = st.file_uploader("Sube una imagen", type=["jpg", "jpeg", "png"])

# Verifica si se ha cargado una imagen
if imagen_subida is not None:
    # Muestra la imagen cargada
    imagen = Image.open(imagen_subida)
    st.image(imagen, caption="Imagen Cargada", use_column_width=True)

    # Inicializar el lector de EasyOCR (en español)
    lector = easyocr.Reader(['es'])

    # Extraer texto de la imagen
    texto_extraido = lector.readtext(imagen, detail=0)

    # Mostrar el texto extraído
    st.write("Texto Extraído:")
    st.write("\n".join(texto_extraido))
