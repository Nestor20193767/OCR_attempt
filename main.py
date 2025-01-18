import streamlit as st
from streamlit_elements import elements, mui
import pandas as pd

def create_reminder_papers(df):
    """
    Generates mui.Paper elements for reminders and displays them alongside the DataFrame.
    
    Parameters:
        df (pd.DataFrame): DataFrame with columns 'Recordatorio', 'Fecha', and 'Estado'.
    """
    st.title("Gestor de Recordatorios")

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

    # Right Column: Display the Papers
    with col2:
        st.header("Recordatorios")

        with elements("mui-papers"):
            for idx, row in st.session_state.df.iterrows():
                unique_key = f"reminder-{idx}"  # Unique key for each paper
                
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
    "Recordatorio": ["Pagar facturas", "Llamar al médico", "Comprar regalos"],
    "Fecha": ["2025-01-20", "2025-01-21", "2025-01-22"],
    "Estado": [False, False, True]
}
df = pd.DataFrame(data)

# Call the function
create_reminder_papers(df)


