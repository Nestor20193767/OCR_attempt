import streamlit as st
from streamlit_elements import elements, dashboard, mui

# URL del logo
logo_url = "https://raw.githubusercontent.com/Nestor20193767/imagenesYLogos/main/Quios/QuiosLogo.png"

st.title("Echo Bot")

# Inicializar historial de chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Layout del dashboard
layout = dashboard.Item("Chatbot", 0, 0, 6, 3)

# Callback para manejar cambios en el layout
def handle_layout_change(updated_layout):
    print("Layout actualizado:", updated_layout)

# Crear el dashboard con elementos
with elements("data_analysis"):
    with dashboard.Grid(layout, onLayoutChange=handle_layout_change):
        with mui.Box(
            sx={
                "display": "flex",
                "flexDirection": "column",
                "borderRadius": "10px",
                "overflow": "hidden",
                "border": "1px solid #ccc",
                "height": "100%",
            },
            key="chat_box",
        ):
            # Título del chatbot
            with mui.Box(
                sx={
                    "backgroundColor": "#f4f4f4",
                    "padding": "10px",
                    "borderBottom": "1px solid #ddd",
                },
                key="chat_title",
            ):
                mui.Typography("Echo Bot", sx={"fontSize": 20, "fontWeight": "bold"})

            # Contenedor de mensajes
            with mui.Box(
                sx={
                    "flex": 1,
                    "padding": "10px",
                    "overflowY": "auto",
                    "backgroundColor": "#ffffff",
                },
                key="chat_messages",
            ):
                for message in st.session_state.messages:
                    role_style = (
                        {"color": "blue"} if message["role"] == "user" else {"color": "green"}
                    )
                    mui.Typography(
                        f"{message['role'].capitalize()}: {message['content']}",
                        sx={"marginBottom": "8px", **role_style},
                    )

            # Input del chat
            with mui.Box(
                sx={
                    "padding": "10px",
                    "borderTop": "1px solid #ddd",
                    "backgroundColor": "#f4f4f4",
                    "display": "flex",
                    "alignItems": "center",
                },
                key="chat_input",
            ):
                # Input y envío de mensajes
                prompt = st.text_input("Escribe tu mensaje aquí:", key="chat_input_field")
                if prompt:
                    # Agregar mensaje del usuario al historial
                    st.session_state.messages.append({"role": "user", "content": prompt})

                    # Respuesta del bot
                    response = f"Echo: {prompt}"
                    st.session_state.messages.append({"role": "assistant", "content": response})




