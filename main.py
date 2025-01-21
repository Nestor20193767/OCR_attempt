import streamlit as st
from streamlit_elements import elements, dashboard, html, nivo, mui

logo_url = "https://raw.githubusercontent.com/Nestor20193767/imagenesYLogos/main/Quios/QuiosLogo.png"


# Función para mostrar el chatbot dentro de un Paper y un Box
def mostrar_chatbot():
    """
    Muestra el chatbot dentro de un Paper y un Box con scroll.
    """
    # Inicializar el historial de mensajes del chat
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Crear un Paper para contener el chatbot
    with mui.Paper(
        elevation=3,
        sx={
            "height": "400px",  # Altura fija
            "overflowY": "scroll",  # Scroll vertical
            "padding": "16px",
            "backgroundColor": "#f5f5f5",
            "borderRadius": 3,
        }
    ):
        # Dentro del Paper, crear un Box para los mensajes del chatbot
        with mui.Box(sx={"display": "flex", "flexDirection": "column", "gap": "8px", "overflowY": "scroll", "maxHeight": "350px"}):
            
            # Mostrar historial de mensajes
            for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    if message["type"] == "text":
                        st.markdown(message["content"])
                    elif message["type"] == "image":
                        st.image(message["content"])

            # Capturar la entrada del usuario
            if prompt := st.chat_input("What is up?"):
                # Mostrar el mensaje del usuario
                with st.chat_message("user"):
                    st.markdown(prompt)
                # Agregar el mensaje del usuario al historial como texto
                st.session_state.messages.append({"role": "user", "type": "text", "content": prompt})

                # Generar la respuesta del bot
                if prompt.lower() == "muestrame una imagen":
                    response = "Aquí tienes una imagen:"
                    image_url = logo_url
                    
                    # Mostrar la respuesta del bot en la interfaz
                    with st.chat_message("assistant"):
                        st.markdown(response)
                        st.image(image_url)

                    # Agregar respuesta y imagen al historial
                    st.session_state.messages.append({"role": "assistant", "type": "text", "content": response})
                    st.session_state.messages.append({"role": "assistant", "type": "image", "content": image_url})
                else:
                    response = f"Echo: {prompt}"
                    
                    # Mostrar la respuesta del bot
                    with st.chat_message("assistant"):
                        st.markdown(response)

                    # Agregar la respuesta al historial
                    st.session_state.messages.append({"role": "assistant", "type": "text", "content": response})
                    
# Renderizar la interfaz en Streamlit Elements
 with elements("chatbot_section"):
    mostrar_chatbot()
                        
# --------------------------------------------------------------


                        



