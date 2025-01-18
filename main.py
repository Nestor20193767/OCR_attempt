import pandas as pd
import random
import datetime
from streamlit_elements import elements, dashboard, nivo, mui

# Crear un DataFrame con datos ficticios
data = {
    "Producto": [
        "Arroz", "Frijoles", "Aceite", "Azúcar", "Café", "Leche", "Huevos", "Pan", "Pollo", "Pescado"
    ],
    "Cantidad": [random.randint(5, 100) for _ in range(10)],
    "Fecha de Vencimiento": [
        (datetime.date.today() + datetime.timedelta(days=random.randint(1, 365))).strftime('%Y-%m-%d')
        for _ in range(10)
    ],
    "Precio (S/.)": [round(random.uniform(1.0, 20.0), 2) for _ in range(10)],
}

df = pd.DataFrame(data)

# Layout para el dashboard
layout = [
    dashboard.Item("table", 0, 0, 4, 2),
    dashboard.Item("bar_chart", 4, 0, 4, 2),
    dashboard.Item("line_chart", 0, 2, 4, 2),
    dashboard.Item("pie_chart", 4, 2, 4, 2),
]

# Callback para manejar cambios en el layout
def handle_layout_change(updated_layout):
    print("Layout actualizado:", updated_layout)

# Preparar datos para gráficos
bar_chart_data = [
    {"Producto": row["Producto"], "Cantidad": row["Cantidad"]}
    for _, row in df.iterrows()
]

line_chart_data = [
    {"Producto": row["Producto"], "Precio": row["Precio (S/.)"]}
    for _, row in df.iterrows()
]

pie_chart_data = [
    {"Producto": row["Producto"], "value": row["Cantidad"]}
    for _, row in df.iterrows()
]

# Función para generar colores aleatorios
def random_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

# Crear el dashboard
with elements("dashboard"):
    with dashboard.Grid(layout, onLayoutChange=handle_layout_change):
        # Tabla de datos
        with mui.Box(sx={"height": 300}, key="table"):
            mui.TableContainer(
                mui.Table(
                    mui.TableHead(
                        mui.TableRow(
                            [mui.TableCell(col) for col in df.columns]
                        )
                    ),
                    mui.TableBody(
                        mui.TableRow(
                            [mui.TableCell(str(row[col])) for col in df.columns]
                        ) for _, row in df.iterrows()
                    )
                )
            )
        
        # Gráfico de barras (Cantidad por Producto)
        with mui.Box(sx={"height": 300}, key="bar_chart"):
            nivo.Bar(
                data=bar_chart_data,
                keys=["Cantidad"],
                indexBy="Producto",
                margin={"top": 50, "right": 50, "bottom": 50, "left": 60},
                padding=0.3,
                valueScale={"type": "linear"},
                indexScale={"type": "band", "round": True},
                colors={ "scheme": "nivo" },
                axisBottom={"tickSize": 5, "tickPadding": 5, "tickRotation": 0},
                axisLeft={"tickSize": 5, "tickPadding": 5, "tickRotation": 0},
            )
        
        # Gráfico de líneas (Precio por Producto)
        with mui.Box(sx={"height": 300}, key="line_chart"):
            nivo.Line(
                data=[{"id": "Precio", "data": line_chart_data}],
                xScale={"type": "point"},
                yScale={"type": "linear", "min": "auto", "max": "auto", "stacked": True, "reverse": False},
                axisBottom={"tickSize": 5, "tickPadding": 5, "tickRotation": 0},
                axisLeft={"tickSize": 5, "tickPadding": 5, "tickRotation": 0},
                colors={"scheme": "set2"},
                pointSize=10,
                pointColor={"theme": "background"},
                pointBorderWidth=2,
                pointBorderColor={"from": "serieColor"},
                useMesh=True,
            )
        
        # Gráfico de pastel (Cantidad por Producto) con colores aleatorios
        with mui.Box(sx={"height": 300}, key="pie_chart"):
            nivo.Pie(
                data=pie_chart_data,
                margin={"top": 50, "right": 50, "bottom": 50, "left": 50},
                innerRadius=0.5,
                padAngle=0.7,
                cornerRadius=3,
                borderWidth=1,
                borderColor={"from": "color", "modifiers": [["darker", 0.2]]},
                radialLabelsSkipAngle=0,  # Mostrar todas las etiquetas
                radialLabelsTextColor="#000000",
                radialLabelsLinkColor={"from": "color"},
                radialLabelsLinkStrokeWidth=1,
                radialLabelsLinkDiagonalLength=16,  # Ajustar la longitud diagonal
                radialLabelsLinkHorizontalLength=24,  # Ajustar la longitud horizontal
                enableSliceLabels=True,  # Habilitar etiquetas en las rebanadas
                sliceLabelsSkipAngle=0,  # Mostrar etiquetas dentro de las rebanadas
                sliceLabelsTextColor="#333333",
                colors=[random_color() for _ in pie_chart_data],  # Colores aleatorios para las rebanadas
                legends=[
                    {
                        "anchor": "bottom",
                        "direction": "row",
                        "translateX": 0,
                        "translateY": 50,
                        "itemWidth": 100,
                        "itemHeight": 20,
                        "itemTextColor": "#999",
                        "symbolSize": 12,
                        "symbolShape": "circle",
                        "effects": [
                            {
                                "on": "hover",
                                "style": {
                                    "itemTextColor": "#000"
                                }
                            }
                        ]
                    }
                ],
            )



