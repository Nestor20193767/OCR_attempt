tengo este codigo: import streamlit as st
from streamlit_elements import elements, dashboard, html, nivo, mui

logo_url = "https://raw.githubusercontent.com/Nestor20193767/imagenesYLogos/main/Quios/QuiosLogo.png"

st.title("Echo Bot")
#st.image(logo_url)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar historial de mensajes
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if message["type"] == "text":
            st.markdown(message["content"])
        elif message["type"] == "image":
            st.image(message["content"])

# Capturar la entrada del usuario
if prompt := st.chat_input("What is up?"):
    # Mostrar el mensaje del usuario en la interfaz
    with st.chat_message("user"):
        st.markdown(prompt)
    # Agregar el mensaje del usuario al historial como texto
    st.session_state.messages.append({"role": "user", "type": "text", "content": prompt})

    # Generar la respuesta del bot
    if prompt.lower() == "muestrame una imagen":
        response = "Aquí tienes una imagen:"
        image_url = "https://raw.githubusercontent.com/Nestor20193767/imagenesYLogos/main/Quios/QuiosLogo.png"
        
        # Mostrar la respuesta del bot en la interfaz
        with st.chat_message("assistant"):
            st.markdown(response)
            st.image(image_url)

        # Agregar respuesta y imagen al historial
        st.session_state.messages.append({"role": "assistant", "type": "text", "content": response})
        st.session_state.messages.append({"role": "assistant", "type": "image", "content": image_url})
    else:
        response = f"Echo: {prompt}"
        
        # Mostrar la respuesta del bot en la interfaz
        with st.chat_message("assistant"):
            st.markdown(response)

        # Agregar la respuesta del bot al historial
        st.session_state.messages.append({"role": "assistant", "type": "text", "content": response})

                            
                        
# --------------------------------------------------------------


                        



