import streamlit as st
from streamlit_elements import elements, dashboard, html, nivo, mui

logo_url = "https://raw.githubusercontent.com/Nestor20193767/imagenesYLogos/main/Quios/QuiosLogo.png"

st.title("Echo Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Layout del dashboard
layout = dashboard.Item("Chatbot", 0, 0, 6, 3)

# Callback para manejar cambios en el layout
def handle_layout_change(updated_layout):
    print("Layout actualizado:", updated_layout)

# Crear el dashboard con elementos de Streamlit Elements
with elements("data_analysis"):
    with dashboard.Grid(layout, onLayoutChange=handle_layout_change):

        # Contenedor principal para el chat
        with mui.Paper(
            sx={
                "display": "flex",
                "flexDirection": "column",
                "borderRadius": 3,
                "overflow": "hidden",
                "height": "100%",
            },
            elevation=4,
            key="chat_container",
        ):

            # Barra de título
            with mui.Box(
                sx={
                    "display": "flex",
                    "alignItems": "center",
                    "backgroundColor": "#f4f4f4",
                    "padding": "10px",
                    "borderBottom": "2px solid #ddd",
                },
                key="chat_title",
            ):
                mui.icon.SignalCellularAlt(sx={"fontSize": 24, "marginRight": "10px"})
                mui.Typography("Echo Bot", sx={"fontSize": 18, "fontWeight": "bold"})

            # Contenedor para los mensajes del chat
            with mui.Box(
                sx={
                    "flex": 1,
                    "padding": "10px",
                    "overflowY": "auto",
                    "backgroundColor": "#ffffff",
                },
                key="chat_messages",
            ):
                # Mostrar los mensajes del historial
                for message in st.session_state.messages:
                    role_style = (
                        {"color": "blue"} if message["role"] == "user" else {"color": "green"}
                    )
                    mui.Typography(
                        f"{message['role'].capitalize()}: {message['content']}",
                        sx={"marginBottom": "8px", **role_style},
                    )

            # Entrada del chat
            with mui.Box(
                sx={
                    "display": "flex",
                    "padding": "10px",
                    "borderTop": "2px solid #ddd",
                    "backgroundColor": "#f4f4f4",
                },
                key="chat_input",
            ):
                prompt = st.text_input("Escribe tu mensaje aquí:", key="chat_input_field")
                if prompt:
                    # Agregar el mensaje del usuario al historial
                    st.session_state.messages.append({"role": "user", "content": prompt})

                    # Respuesta del bot
                    response = f"Echo: {prompt}"
                    st.session_state.messages.append({"role": "assistant", "content": response})





