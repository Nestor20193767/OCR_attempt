import streamlit as st
from streamlit_elements import elements, dashboard, html, nivo, mui

logo_url = "https://raw.githubusercontent.com/Nestor20193767/imagenesYLogos/main/Quios/QuiosLogo.png"

st.title("Echo Bot")
#st.image(logo_url)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

st.write("cambie")

# --------------------------------------------------------------

layout = dashboard.Item("Chatbot", 0, 0, 6, 3)
# Callback para manejar cambios en el layout
def handle_layout_change(updated_layout):
            print("Layout actualizado:", updated_layout)





   # Crear el dashboard con elementos de Nivo
with elements("data_analysis"):
            with dashboard.Grid(layout, onLayoutChange=handle_layout_change):

                with mui.Paper(sx={"display": "flex", "flexDirection": "column", "borderRadius": 3, "overflow": "hidden"}, elevation=4, key="cantidad_bars"):

                    # Barra de título con icono y texto en la misma línea
                    with mui.Box(sx={"display": "flex", "alignItems": "center", "backgroundColor": "#f4f4f4", 
                                     "padding": "10px", "borderBottom": "2px solid #ddd", "overflowY": "scroll"},
                                key="titulo_cantidad_bar"):
                        # Icono
                        mui.icon.SignalCellularAlt(sx={"fontSize": 24, "marginRight": "10px"})
                        
                        # Título
                        mui.Typography("Echo bot", sx={"fontSize": 18, "fontWeight": "bold"})

                    # Gráfico de productos con bajo stock (actualizado para mostrar todos los productos)
                    with mui.Box(sx={"height": "90%"}, key="low_stock_chart"):

                        # Display chat messages from history on app rerun
                        for message in st.session_state.messages:
                            with st.chat_message(message["role"]):
                                st.markdown(message["content"])
                        
                        # React to user input
                        if prompt := st.chat_input("What is up?"):
                            # Display user message in chat message container
                            st.chat_message("user").markdown(prompt)
                            # Add user message to chat history
                            st.session_state.messages.append({"role": "user", "content": prompt})
                        
                            response = f"Echo: {prompt}"
                            # Display assistant response in chat message container
                            with st.chat_message("assistant"):
                                st.markdown(response)
                                #st.image(logo_url )
                                if response == "Echo: Muestrame una imagen":
                                    st.image(logo_url)
                                
                            # Add assistant response to chat history
                            st.session_state.messages.append({"role": "assistant", "content": response})
                        




