import streamlit as st
from streamlit_elements import elements, mui, dashboard

# Dashboard Layout Configuration
layout = [
    dashboard.Item("card1", 0, 0, 6, 2),  # (item_id, x, y, width, height)
    dashboard.Item("card2", 6, 0, 6, 2),
]

# Sidebar and Title
st.sidebar.title("Dashboard Configuration")
st.title("Interactive Dashboard with Streamlit Elements")

# Render Dashboard
with elements("dashboard"):
    # Initialize the dashboard grid
    with dashboard.Grid(layout, draggableHandle=".draggable"):
        # First Card
        with mui.Card(key="card1", elevation=3):
            with mui.CardContent():
                mui.Typography("Card 1", variant="h5", gutterBottom=True)
                mui.Button("Button in Card 1", variant="contained", color="primary")

        # Second Card
        with mui.Card(key="card2", elevation=3):
            with mui.CardContent():
                mui.Typography("Card 2", variant="h5", gutterBottom=True)
                mui.TextField(label="Input in Card 2", variant="outlined")
















