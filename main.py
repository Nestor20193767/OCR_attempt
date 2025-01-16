import streamlit as st
import pandas as pd

# Simulación de datos de stock
stock_data = pd.DataFrame({
    "Producto": ["Leche", "Pan", "Queso"],
    "Precio (S/.)": [3.5, 1.0, 5.0]
})

# Crear un DataFrame vacío para almacenar las ventas
ventas_df = pd.DataFrame(columns=["Producto", "Precio Unitario (S/.)", "Cantidad", "Total (S/.)"])

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
                    # Agregar la venta al DataFrame
                    nueva_fila = {
                        "Producto": producto_vendido,
                        "Precio Unitario (S/.)": precio_venta,
                        "Cantidad": cantidad_vendida,
                        "Total (S/.)": precio_venta * cantidad_vendida
                    }
                    ventas_df = pd.concat([ventas_df, pd.DataFrame([nueva_fila])], ignore_index=True)
        
        with col2:
            st.subheader("Productos añadidos")
            if not ventas_df.empty:
                # Mostrar el DataFrame sin índice
                st.dataframe(hide_index=True, use_container_width=True)
            else:
                st.write("No hay productos añadidos todavía.")



    










