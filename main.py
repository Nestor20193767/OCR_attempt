import streamlit as st

# Estilo CSS para la columna con scrollbar
st.markdown(
    """
    <style>
    .scrollable-container {
        height: 500px; /* Altura fija */
        overflow-y: auto; /* Scroll vertical */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Contenedor fijo (sin scrollbar)
with st.container():
    col1, col2 = st.columns(2)

    # Contenido de la columna fija
    with col1:
        st.header("Columna fija")
        st.write("Este contenido permanecerá fijo y no tendrá un scrollbar.")
        for i in range(10):
            st.write(f"Elemento fijo {i + 1}")

    # Contenedor desplazable con scrollbar
    with col2:
        st.header("Columna con scrollbar")
        st.markdown('<div class="scrollable-container">', unsafe_allow_html=True)
        for i in range(50):  # Muchos elementos para generar scrollbar
            st.write(f"Elemento desplazable {i + 1}")
        st.markdown('</div>', unsafe_allow_html=True)




