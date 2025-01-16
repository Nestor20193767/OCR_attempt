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
                texto_ventas += "-" * 80 + "\n"  # Línea divisoria
            
            # Calcular el número de líneas para ajustar la altura
            num_lineas = len(texto_ventas.split("\n"))
            altura_text_area = max(150, num_lineas * 20)  # Altura mínima de 150 px, 20 px por línea
            
            st.text_area("Lista de Productos", value=texto_ventas, height=altura_text_area, disabled=True)
            
            # Sección de pago
            st.subheader("Método de Pago")
            pago = st.radio("Selecciona método de pago", ("YAPE", "Efectivo"))
            
            if pago == "YAPE":
                if st.button("Realizar Venta"):
                    st.success("Venta realizada con éxito mediante YAPE.")
                    st.session_state.ventas.clear()  # Limpiar la lista de productos después de la venta
            elif pago == "Efectivo":
                # Calcular el precio total
                total = sum([venta['Precio Unitario'] * venta['Cantidad'] for venta in st.session_state.ventas])
                total = round(total, 2)
                
                # Mostrar calculadora para efectivo
                monto_recibido = st.number_input(f"Total: S/. {total} - Monto Recibido", min_value=total, value=total, step=0.1)
                
                if monto_recibido > total:
                    vuelto = round(monto_recibido - total, 2)
                    st.write(f"**Vuelto a devolver:** S/. {vuelto}")
                elif monto_recibido == total:
                    st.write("**Pago Exacto. No hay vuelto.**")
                else:
                    st.warning("El monto recibido es menor que el total. Asegúrate de ingresar la cantidad correcta.")
                
                # Botón para realizar venta
                if st.button("Realizar Venta"):
                    st.success("Venta realizada con éxito mediante Efectivo.")
                    st.session_state.ventas.clear()  # Limpiar la lista de productos después de la venta













