import streamlit as st
from streamlit_elements import elements, mui

def create_reminder_papers(df):
    """
    Generates mui.Paper elements for reminders.
    
    Parameters:
        df (pd.DataFrame): DataFrame with columns 'Recordatorio', 'Fecha', and 'Estado'.
    """
    st.title("Recordatorios")

    # Use session state to track updates to the DataFrame
    if "df" not in st.session_state:
        st.session_state.df = df

    # Function to mark a reminder as completed
    def mark_completed(index):
        st.session_state.df.loc[index, 'Estado'] = True

    with elements("mui-papers"):
        for idx, row in st.session_state.df.iterrows():
            # Generate a unique key for each paper
            unique_key = f"reminder-{idx}"
            
            with mui.Paper(
                elevation=3,
                sx={"padding": "16px", "marginBottom": "16px"},
                key=unique_key
            ):
                mui.Typography(row['Recordatorio'], variant="h6")
                mui.Typography(f"Fecha: {row['Fecha']}", variant="body2")
                
                # Show "Completado" button only if Estado is False
                if not row['Estado']:
                    # Pass the index to the onClick handler
                    mui.Button(
                        "Completado",
                        color="primary",
                        onClick=lambda idx=idx: mark_completed(idx)
                    )
                else:
                    mui.Typography("Estado: Completado", color="green", variant="body2")

# Example usage
import pandas as pd

# Example DataFrame
data = {
    "Recordatorio": ["Pagar facturas", "Llamar al médico", "Comprar regalos"],
    "Fecha": ["2025-01-20", "2025-01-21", "2025-01-22"],
    "Estado": [False, False, True]
}
df = pd.DataFrame(data)

# Call the function
create_reminder_papers(df)

