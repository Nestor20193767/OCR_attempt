import streamlit as st
from streamlit_elements import elements, mui, html

st.title("Streamlit Elements Demo")

# Use the elements context to render the components
with elements("demo"):
    # Add a Material-UI Card component
    with mui.Card(elevation=3):
        with mui.CardContent():
            mui.Typography("Hello, this is a Material-UI card!", variant="h5", gutterBottom=True)
            mui.Button("Click Me", variant="contained", color="primary")

    # Add an HTML component
    html.div(
        "This is an HTML element!",
        style={"color": "blue", "fontSize": "20px", "marginTop": "20px"}
    )
















