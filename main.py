from streamlit_elements import elements, dashboard, nivo
import pandas as pd
import streamlit as st

# Ejemplo de stock_data (reemplaza esto con tus datos reales)
stock_data = pd.DataFrame({
    "Producto": ["Producto A", "Producto B", "Producto C"],
    "Cantidad": [50, 20, 5],
    "Fecha de Vencimiento": ["2025-01-01", "2024-01-20", "2024-02-15"],
    "Precio (S/.)": [12.5, 8.0, 15.0]
})

# Asegurarse de que la página es la correcta
page = "Análisis de Datos"

if page == "Análisis de Datos":
    st.title("Análisis de Datos")
    st.write("Explora los datos del inventario para identificar necesidades de reposición y evaluar prioridades de compra.")

    if stock_data.empty:
        st.warning("No hay datos disponibles para análisis.")
    else:
        # Mostrar datos para verificar
        st.subheader("Datos del Inventario")
        st.dataframe(stock_data)

        # Crear un layout para el dashboard
        layout = [
            dashboard.Item("low_stock_chart", 0, 0, 6, 3),  # Productos con bajo stock
            dashboard.Item("price_chart", 6, 0, 6, 3),     # Precios de productos
            dashboard.Item("expiry_chart", 0, 3, 6, 3),    # Vencimientos próximos
            dashboard.Item("summary_stats", 6, 3, 6, 3)    # Resumen de estadísticas
        ]

        # Datos para gráficos
        low_stock = stock_data[stock_data["Cantidad"] < 10]  # Productos con bajo stock
        product_prices = stock_data[["Producto", "Precio (S/.)"]]
        stock_data["Fecha de Vencimiento"] = pd.to_datetime(stock_data["Fecha de Vencimiento"])
        upcoming_expiry = stock_data[
            stock_data["Fecha de Vencimiento"] <= pd.Timestamp.now() + pd.Timedelta(days=30)
        ]

        # Crear el dashboard con elementos de Nivo
        with elements("data_analysis"):
            with dashboard.Grid(layout):
                # Gráfico de productos con bajo stock
                if not low_stock.empty:
                    with nivo.Bar(key="low_stock_chart"):
                        nivo.Bar(
                            data=[
                                {"Producto": row["Producto"], "Cantidad": row["Cantidad"]}
                                for _, row in low_stock.iterrows()
                            ],
                            keys=["Cantidad"],
                            indexBy="Producto",
                            margin={"top": 50, "right": 50, "bottom": 50, "left": 60},
                            padding=0.3,
                            axisBottom={
                                "legend": "Producto",
                                "legendPosition": "middle",
                                "legendOffset": 40,
                            },
                            axisLeft={
                                "legend": "Cantidad",
                                "legendPosition": "middle",
                                "legendOffset": -40,
                            },
                            colors={"scheme": "set3"},
                        )
                else:
                    st.info("No hay productos con bajo stock.")

                # Gráfico de precios de productos
                with nivo.Bar(key="price_chart"):
                    nivo.Bar(
                        data=[
                            {"Producto": row["Producto"], "Precio": row["Precio (S/.)"]}
                            for _, row in product_prices.iterrows()
                        ],
                        keys=["Precio"],
                        indexBy="Producto",
                        margin={"top": 50, "right": 50, "bottom": 50, "left": 60},
                        padding=0.3,
                        axisBottom={
                            "legend": "Producto",
                            "legendPosition": "middle",
                            "legendOffset": 40,
                        },
                        axisLeft={
                            "legend": "Precio (S/.)",
                            "legendPosition": "middle",
                            "legendOffset": -40,
                        },
                        colors={"scheme": "nivo"},
                    )

                # Gráfico de vencimientos próximos
                if not upcoming_expiry.empty:
                    with nivo.Pie(key="expiry_chart"):
                        nivo.Pie(
                            data=[
                                {"id": row["Producto"], "value": 1}
                                for _, row in upcoming_expiry.iterrows()
                            ],
                            margin={"top": 40, "right": 80, "bottom": 80, "left": 80},
                            innerRadius=0.5,
                            padAngle=0.7,
                            cornerRadius=3,
                            colors={"scheme": "category10"},
                        )
                else:
                    st.info("No hay productos con vencimientos próximos.")

                # Resumen de estadísticas
                with nivo.Wrapper(key="summary_stats"):
                    st.subheader("Resumen de Inventario")
                    st.write("Cantidad total de productos:", stock_data["Cantidad"].sum())
                    st.write("Gasto total estimado (S/.):", (stock_data["Cantidad"] * stock_data["Precio (S/.)"]).sum())
                    if not low_stock.empty:
                        st.write("Productos con bajo stock:")
                        st.dataframe(low_stock)
                    if not upcoming_expiry.empty:
                        st.write("Productos con vencimiento próximo:")
                        st.dataframe(upcoming_expiry)








