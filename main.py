import requests
import streamlit as st
from base64 import b64encode
from streamlit_elements import elements, dashboard, html

st.set_page_config(layout="wide")

# Some random image URL.
images_url = [
    "https://unsplash.com/photos/1CsaVdwfIew/download?ixid=MnwxMjA3fDB8MXxhbGx8fHx8fHx8fHwxNjUxNTE3OTQx&force=true&w=1920",
    "https://unsplash.com/photos/eHlVZcSrjfg/download?force=true&w=1920",
    "https://unsplash.com/photos/CSs8aiN_LkI/download?ixid=MnwxMjA3fDB8MXxhbGx8fHx8fHx8fHwxNjUxNTE2ODM1&force=true&w=1920",
    "https://unsplash.com/photos/GJ8ZQV7eGmU/download?force=true&w=1920",
]

# Download these images and get their bytes.
images_bytes = [requests.get(url).content for url in images_url]

# Encode these bytes to base 64.
images_b64 = [b64encode(bytes).decode() for bytes in images_bytes]

# Initialize a layout for our dashboard.
# It's gonna be a 2x2 grid, with each element being of height 3 and width 6 out of 12.
layout = [
    dashboard.Item("image0", 0, 0, 6, 3),
    dashboard.Item("image1", 6, 0, 6, 3),
    dashboard.Item("image2", 0, 3, 6, 3),
    dashboard.Item("image3", 6, 3, 6, 3),
]

with elements("image_grid"):
    with dashboard.Grid(layout):
        # We iterate over our images encoded as base64.
        # enumerate() will return the item's index i from 0 to 3, so I can generate
        # dashboard layout keys from "image0" to "image3".
        for i, b64 in enumerate(images_b64):
            html.img(
                # We pass our base 64 to <img src=...></img> to display our image.
                # See: https://stackoverflow.com/a/8499716
                src=f"data:image/png;base64,{b64}",
                # A simple CSS style to avoid image distortion on resize.
                css={"object-fit": "cover"},
                # We set the key to bind our image to a dashboard item.
                key=f"image{i}",
            )










