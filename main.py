import streamlit as st
from streamlit_elements import elements, mui, html, dashboard, sync

# Configuración inicial del diseño de la cuadrícula
layout = [
    dashboard.Item("pie_chart", 0, 0, 6, 4),
    dashboard.Item("card_content", 6, 0, 6, 4),
    dashboard.Item("radar_chart", 0, 4, 6, 4),
    dashboard.Item("data_grid", 6, 4, 6, 4),
]

# Título de la aplicación
st.title("Streamlit Elements - Widgets Movibles")

# Contexto de streamlit-elements
with elements("widgets_dashboard"):
    # Crear un dashboard con widgets movibles y redimensionables
    with dashboard.Grid(layout, draggableHandle=".draggable", resizable=True):
        
        # Widget: Pie Chart
        with mui.Paper(key="pie_chart", elevation=3):
            with mui.CardContent():
                mui.Typography("Pie Chart", variant="h6", className="draggable")
                elements.Chart(
                    type="pie",
                    options={"responsive": True},
                    data={
                        "labels": ["Java", "Rust", "Scala", "Ruby", "Elixir"],
                        "datasets": [
                            {
                                "data": [485, 140, 300, 430, 360],
                                "backgroundColor": [
                                    "#FF6384",
                                    "#36A2EB",
                                    "#FFCE56",
                                    "#4BC0C0",
                                    "#9966FF",
                                ],
                            }
                        ],
                    },
                )
        
        # Widget: Card Content
        with mui.Paper(key="card_content", elevation=3):
            with mui.CardContent():
                mui.Typography("Card Content", variant="h6", className="draggable")
                mui.Typography(
                    "This impressive paella is a perfect party dish and fun meal to cook together with your guests. Add 1 cup of frozen peas along with the mussels, if you like.",
                    variant="body1",
                )
                html.img(
                    src="https://via.placeholder.com/400x200.png?text=Example+Image",
                    style={"width": "100%", "borderRadius": "8px"},
                )
        
        # Widget: Radar Chart
        with mui.Paper(key="radar_chart", elevation=3):
            with mui.CardContent():
                mui.Typography("Radar Chart", variant="h6", className="draggable")
                elements.Chart(
                    type="radar",
                    options={"responsive": True},
                    data={
                        "labels": ["Fruity", "Bitter", "Heavy", "Strong", "Sunny"],
                        "datasets": [
                            {
                                "label": "Chardonnay",
                                "data": [12, 19, 3, 5, 2],
                                "borderColor": "rgba(255,99,132,1)",
                                "backgroundColor": "rgba(255,99,132,0.2)",
                            },
                            {
                                "label": "Carmenere",
                                "data": [10, 15, 6, 8, 5],
                                "borderColor": "rgba(54,162,235,1)",
                                "backgroundColor": "rgba(54,162,235,0.2)",
                            },
                        ],
                    },
                )
        
        # Widget: Data Grid
        with mui.Paper(key="data_grid", elevation=3):
            with mui.CardContent():
                mui.Typography("Data Grid", variant="h6", className="draggable")
                mui.TableContainer(
                    mui.Table(
                        mui.TableHead(
                            mui.TableRow(
                                [
                                    mui.TableCell("ID"),
                                    mui.TableCell("First Name"),
                                    mui.TableCell("Last Name"),
                                    mui.TableCell("Age"),
                                ]
                            )
                        ),
                        mui.TableBody(
                            [
                                mui.TableRow(
                                    [
                                        mui.TableCell("1"),
                                        mui.TableCell("Jon"),
                                        mui.TableCell("Snow"),
                                        mui.TableCell("35"),
                                    ]
                                ),
                                mui.TableRow(
                                    [
                                        mui.TableCell("2"),
                                        mui.TableCell("Cersei"),
                                        mui.TableCell("Lannister"),
                                        mui.TableCell("42"),
                                    ]
                                ),
                                mui.TableRow(
                                    [
                                        mui.TableCell("3"),
                                        mui.TableCell("Jaime"),
                                        mui.TableCell("Lannister"),
                                        mui.TableCell("45"),
                                    ]
                                ),
                            ]
                        ),
                    ),
                )













