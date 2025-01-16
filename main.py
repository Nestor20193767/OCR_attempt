import streamlit as st
import pandas as pd
from datetime import datetime






# Crear el diálogo de Streamlit
@st.dialog("Mostrar tu texto")
def show_text_dialog():
    # Crear un campo de entrada para texto
    user_text = st.text_input("Escribe algo aquí...")
    
    # Cuando el usuario presiona el botón, mostrar el texto en el diálogo
    if st.button("Mostrar en el diálogo"):
        st.session_state.user_message = user_text
        st.rerun()  # Recargar la aplicación para mostrar el mensaje en el diálogo

# Verificar si ya hay un mensaje guardado en el estado de sesión
if "user_message" not in st.session_state:
    st.write("Ingresa un texto y presiona el botón para mostrarlo en el diálogo.")
else:
    # Mostrar el mensaje ingresado en el diálogo
    st.write(f"Tu mensaje es: {st.session_state.user_message}")





# Configuración inicial de Streamlit
st.set_page_config(page_title="Gestión de Proyectos", page_icon="📝")

# Inicializar datos si no existen en el estado de la sesión
if "projects" not in st.session_state:
    st.session_state.projects = []

if "messages" not in st.session_state:
    st.session_state.messages = []

if "notes" not in st.session_state:
    st.session_state.notes = []

# Función para agregar un proyecto
def add_project(name):
    st.session_state.projects.append({
        "id": len(st.session_state.projects) + 1,
        "name": name,
        "timestamp": datetime.now()
    })

# Función para agregar un mensaje
def add_message(content, project_id):
    st.session_state.messages.append({
        "id": len(st.session_state.messages) + 1,
        "content": content,
        "project_id": project_id,
        "timestamp": datetime.now(),
        "pinned": False,
        "archived": False
    })

# Función para agregar una nota
def add_note(content):
    st.session_state.notes.append({
        "id": len(st.session_state.notes) + 1,
        "content": content,
        "timestamp": datetime.now()
    })

# Encabezado principal
st.title("Gestión de Proyectos")

# Sección para crear un nuevo proyecto
st.header("Crear un Nuevo Proyecto")
with st.form("new_project_form"):
    project_name = st.text_input("Nombre del Proyecto:")
    project_submit = st.form_submit_button("Crear Proyecto")

    if project_submit and project_name:
        add_project(project_name)
        st.success(f"Proyecto '{project_name}' creado exitosamente.")

# Mostrar proyectos existentes
st.header("Proyectos Existentes")
if st.session_state.projects:
    project_names = [proj["name"] for proj in st.session_state.projects]
    project_selected = st.selectbox("Selecciona un Proyecto", options=project_names)

    # Mostrar mensajes relacionados con el proyecto seleccionado
    if project_selected:
        st.subheader(f"Mensajes para el Proyecto: {project_selected}")
        project_id = next(proj["id"] for proj in st.session_state.projects if proj["name"] == project_selected)
        project_messages = [msg for msg in st.session_state.messages if msg["project_id"] == project_id]

        if project_messages:
            for msg in project_messages:
                st.markdown(f"`{msg['timestamp']}` - {msg['content']}")

                # Opciones de fijar y archivar
                pinned = st.checkbox("📌 Fijar", value=msg["pinned"], key=f"pinned-{msg['id']}")
                archived = st.checkbox("🗑️ Archivar", value=msg["archived"], key=f"archived-{msg['id']}")

                msg["pinned"] = pinned
                msg["archived"] = archived
        else:
            st.info("No hay mensajes para este proyecto.")

        # Agregar nuevo mensaje al proyecto seleccionado
        st.subheader("Agregar Mensaje")
        new_message = st.text_area("Escribe un mensaje:")
        if st.button("Agregar Mensaje"):
            if new_message:
                add_message(new_message, project_id)
                st.success("Mensaje agregado exitosamente.")
            else:
                st.warning("Escribe un mensaje antes de enviarlo.")
else:
    st.info("No hay proyectos disponibles. Crea uno nuevo arriba.")

# Sección de notas
st.header("Notas")
with st.form("new_note_form"):
    note_content = st.text_area("Escribe una nota:")
    note_submit = st.form_submit_button("Agregar Nota")

    if note_submit and note_content:
        add_note(note_content)
        st.success("Nota agregada exitosamente.")

# Mostrar todas las notas
if st.session_state.notes:
    for note in st.session_state.notes:
        st.info(note["content"])
else:
    st.info("No hay notas disponibles.")

