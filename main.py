import streamlit as st

# Aplicar estilos para habilitar el scrollbar
st.markdown(
    """
    <style>
    .scrollable-container {
        height: 400px; /* Altura fija del contenedor */
        overflow-y: auto; /* Habilitar el desplazamiento vertical */
        padding-right: 10px; /* Espacio para el scrollbar */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Crear dos columnas dentro de un contenedor
col1, col2 = st.columns(2)

# Columna fija (sin scrollbar)
with col1:
    st.header("Columna Fija")
    st.write("Este contenido permanecerá fijo y no tendrá un scrollbar.")
    for i in range(10):
        st.write(f"Elemento fijo {i + 1}")

# Columna con scrollbar
with col2:
    st.header("Columna Desplazable")
    st.markdown('<div class="scrollable-container">', unsafe_allow_html=True)
    for i in range(50):  # Muchos elementos para que se genere un scrollbar
        st.write(f"Elemento desplazable {i + 1}")
    st.markdown('</div>', unsafe_allow_html=True)




