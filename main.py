import streamlit as st
from streamlit_elements import elements, mui
import pandas as pd

def create_reminder_papers_with_scroll(df):
    """
    Generates mui.Paper elements for reminders and displays them in a scrollable mui.Box.

    Parameters:
        df (pd.DataFrame): DataFrame with columns 'Recordatorio', 'Fecha', and 'Estado'.
    """
    st.title("Gestor de Recordatorios con Scroll")

    # Initialize session state for the DataFrame
    if "df" not in st.session_state:
        st.session_state.df = df

    # Function to mark a reminder as completed
    def mark_completed(index):
        st.session_state.df.loc[index, 'Estado'] = True

    # Split into two columns
    col1, col2 = st.columns(2)

    # Left Column: Display the DataFrame
    with col1:
        st.header("Estado del DataFrame")
        st.dataframe(st.session_state.df)

    # Right Column: Display the Papers in a scrollable Box
    with col2:
        st.header("Recordatorios")

        with elements("mui-papers"):
            # mui.Box with scroll
            with mui.Box(
                sx={
                    "height": "400px",  # Fixed height for the box
                    "overflowY": "scroll",  # Enable vertical scrolling
                    "padding": "16px",
                    "border": "1px solid #ccc",
                    "backgroundColor": "#f9f9f9",
                }
            ):
                for idx, row in st.session_state.df.iterrows():
                    unique_key = f"reminder-{idx}"  # Unique key for each paper
                    
                    # Render each Paper
                    with mui.Paper(
                        elevation=3,
                        sx={"padding": "16px", "marginBottom": "16px"},
                        key=unique_key
                    ):
                        mui.Typography(row['Recordatorio'], variant="h6")
                        mui.Typography(f"Fecha: {row['Fecha']}", variant="body2")
                        
                        # Show "Completado" button only if Estado is False
                        if not row['Estado']:
                            mui.Button(
                                "Completado",
                                color="primary",
                                onClick=lambda idx=idx: mark_completed(idx)
                            )
                        else:
                            mui.Typography("Estado: Completado", color="green", variant="body2")


# Example usage
data = {
    "Recordatorio": [f"Tarea {i}" for i in range(1, 51)],  # 50 reminders to test scroll
    "Fecha": [f"2025-01-{str(i % 31 + 1).zfill(2)}" for i in range(1, 51)],  # Cyclic dates
    "Estado": [False] * 50
}
df = pd.DataFrame(data)

# Call the function
create_reminder_papers_with_scroll(df)


