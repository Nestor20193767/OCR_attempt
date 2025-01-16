import streamlit as st
import pandas as pd

# Simulación de datos de stock
stock_data = pd.DataFrame({
    "Producto": ["Leche", "Pan", "Queso"],
    "Precio (S/.)": [3.5, 1.0, 5.0]
})

# Inicializar session_state para las ventas
if "ventas" not in st.session_state:
    st.session_state.ventas = []

# Página de ventas
page = "Ventas"

if page == "Ventas":
    st.title("Ventas")
    st.write("Registro de ventas.")
    
    col1, col2 = st.columns(2)
    
    # Asegurarse de que stock_data tiene datos antes de usarlo
    if not stock_data.empty:
        with col1:
            with st.form(key='form_venta'):
                producto_vendido = st.selectbox("Producto", stock_data["Producto"])
                cantidad_vendida = st.number_input("Cantidad Vendida", min_value=1, step=1)
                precio_venta = stock_data.loc[stock_data["Producto"] == producto_vendido, "Precio (S/.)"].values[0]
                
                add_button = st.form_submit_button("Añadir Producto")
                
                if add_button:
                    # Añadir la venta al session_state
                    st.session_state.ventas.append({
                        "Producto": producto_vendido,
                        "Precio Unitario": precio_venta,
                        "Cantidad": cantidad_vendida
                    })
        
        with col2:
            # Mostrar los productos añadidos en un text_area
            st.subheader("Productos añadidos")
            texto_ventas = ""
            for venta in st.session_state.ventas:
                texto_ventas += f"Producto: {venta['Producto']}\n"
                texto_ventas += f"Precio Unitario: S/. {venta['Precio Unitario']}\n"
                texto_ventas += f"Cantidad: {venta['Cantidad']}\n"
                texto_ventas += "-" * 50 + "\n"  # Línea divisoria
            
            # Calcular el número de líneas para ajustar la altura
            num_lineas = len(texto_ventas.split("\n"))
            altura_text_area = max(100, num_lineas * 20)  # Altura mínima de 100 px, 20 px por línea
            
            st.text_area("Lista de Productos", value=texto_ventas, height=altura_text_area, disabled=True)












