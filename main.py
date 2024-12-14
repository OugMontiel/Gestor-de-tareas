import streamlit as st
import SqlAlchemy as Sql

# Crear el motor de conexión y el modelo Base
engine, Base = Sql.create_engine_and_base()

# Crear las tablas en la base de datos
Sql.create_tables(engine, Base)

# Crear una sesión
session = Sql.create_session(engine)

# Función para recargar las notas 
def recargar_notas(): return Sql.read_tareas(session)
notas = recargar_notas()

# Mostrar las notas existentes
st.header("Tus Notas")

# Crear contenedores en forma de grilla con columnas
col_count = 4  # Número de columnas por fila
cols = st.columns(col_count)

# Colores mejorados para tareas
color_completado = "#c8e6c9"  # Verde pastel
color_pendiente = "#ffcdd2"   # Rojo pastel

# Mostrar las tareas en un diseño de cuadrícula
for idx, tarea in enumerate(notas):
    # Seleccionar el color según el estado
    color = color_completado if tarea.estado else color_pendiente
    estado_texto = "✔️ " if not tarea.estado else "⏳ "

    # Mostrar cada tarea en su columna
    with cols[idx % col_count]:
        st.markdown(
            f"""
            <div style="background-color: {color}; padding: 15px; border-radius: 8px; box-shadow: 0px 4px 6px rgba(0,0,0,0.1);">
                <h4 style='text-align: center; font-size: 1.2em; color: #2c3e50;'>{tarea.titulo}</h4>
                <p style='text-align: justify; margin-bottom: 15px; color: #34495e;'>{tarea.descripcion}</p>
            """,
            unsafe_allow_html=True
        )
    # Botones de acción
        col_estado, col_eliminar = st.columns(2, gap="small")
        with col_estado:
            if st.button(estado_texto, key=f"estado_{tarea.id}"):
                # Cambiar el estado de la tarea
                Sql.change_estado(session, tarea.id)
                notas = recargar_notas()  # Actualizar notas
                break  

        with col_eliminar:
            if st.button("🗑️", key=f"eliminar_{tarea.id}"):
                # Eliminar la tarea
                Sql.delete_tarea(session, tarea.id)
                notas = recargar_notas()  # Actualizar notas
                break  

# Añadir una nueva nota
st.header("Añadir una nueva nota")

# Botón para mostrar el formulario
if st.button("Agregar Nota"):
    with st.expander("Formulario para añadir una nueva nota"):
        titulo = st.text_input("Título de la nota")
        descripcion = st.text_area("Descripción de la nota")

        # Botón para agregar la nota dentro del formulario
        if st.button("Guardar Nota"):
            if titulo.strip() and descripcion.strip():
                Sql.add_tarea(session, titulo, descripcion)
                st.success("¡Nota agregada!")
                notas = recargar_notas()
            else:
                st.error("El título y la descripción no pueden estar vacíos.")


# # Eliminar una nota
# st.header("Eliminar una Nota")
# nota_id = st.selectbox("Selecciona una nota para eliminar", list(notas.keys()))

# if st.button("Eliminar Nota"):
#     try:
#         Sql.delete_tarea(session, nota_id)
#         st.success("¡Nota eliminada!")
#     except ValueError as e:
#         st.error("La nota seleccionada no existe.")
#         st.error(str(e))
