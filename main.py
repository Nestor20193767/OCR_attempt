import streamlit as st
from streamlit_elements import elements, mui, html, dashboard

# Configuración inicial del diseño de la cuadrícula
layout = [
    dashboard.Item("card1", 0, 0, 4, 2),  # id, x, y, ancho, alto
    dashboard.Item("card2", 4, 0, 4, 2),
    dashboard.Item("card3", 8, 0, 4, 2),
]

# Título de la aplicación
st.title("Cartas Movibles con Áreas de Arrastre")

# Contexto de elementos
with elements("movable_cards"):
    # Crear una cuadrícula movible
    with dashboard.Grid(layout, draggableHandle=".draggable", resizable=True):
        # Primera Carta
        with mui.Card(key="card1", elevation=3):
            with mui.CardContent():
                mui.Typography("Carta Movible 1", variant="h5", gutterBottom=True)
                mui.Button("Botón 1", variant="contained", color="primary")
                # Área de arrastre
                html.div(
                    "⬍",
                    style={"cursor": "move", "marginTop": "10px", "color": "gray"},
                    draggable="true",  # Asegura que sea movible
                )

        # Segunda Carta
        with mui.Card(key="card2", elevation=3):
            with mui.CardContent():
                mui.Typography("Carta Movible 2", variant="h5", gutterBottom=True)
                mui.Button("Botón 2", variant="contained", color="secondary")
                # Área de arrastre
                html.div(
                    "⬍",
                    style={"cursor": "move", "marginTop": "10px", "color": "gray"},
                    draggable="true",
                )

        # Tercera Carta
        with mui.Card(key="card3", elevation=3):
            with mui.CardContent():
                mui.Typography("Carta Movible 3", variant="h5", gutterBottom=True)
                mui.Button("Botón 3", variant="contained", color="success")
                # Área de arrastre
                html.div(
                    "⬍",
                    style={"cursor": "move", "marginTop": "10px", "color": "gray"},
                    draggable="true",
                )


















