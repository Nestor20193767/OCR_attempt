import streamlit as st
import pandas as pd

# Crear un DataFrame de ejemplo
df = pd.DataFrame({
    'Nombre': ['Juan', 'Pedro', 'María'],
    'Edad': [23, 45, 34]
})

# Mostrar el DataFrame
st.write("DataFrame con botones:")
for i, row in df.iterrows():
    col1, col2 = st.columns([3, 1])  # Definir dos columnas, una para el DataFrame y otra para el botón
    with col1:
        st.write(row.to_dict())  # Mostrar la fila del DataFrame
    with col2:
        # Colocar un botón en cada fila
        if st.button(f'Acción {i}', key=f'boton_{i}'):
            st.write(f'Botón {i} presionado')

    










