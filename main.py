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

# Titulo de acciones 
st.header("Acciones")

# Dividir en tres columnas para los botones
col1, col2, col3 = st.columns(3)

# Variable para rastrear el estado actual
estado_actual = None

# Botones en línea
with col1:
    if st.button("Agregar Nota"):
        estado_actual = "agregar"

with col2:
    if st.button("Exportar Notas"):
        estado_actual = "exportar"

with col3:
    if st.button("Importar Notas"):
        estado_actual = "importar"

# Contenido dinámico según el estado actual
if estado_actual == "agregar":
    st.subheader("Añadir una nueva nota")
    titulo = st.text_input("Título de la nota")
    descripcion = st.text_area("Descripción de la nota")

    if st.button("Guardar Nota"):
        if titulo.strip() and descripcion.strip():
            Sql.add_tarea(session, titulo, descripcion)
            st.success("¡Nota agregada!")
            notas = recargar_notas()  # Recargar notas después de agregar
        else:
            st.error("El título y la descripción no pueden estar vacíos.")

elif estado_actual == "exportar":
    st.subheader("Exportar Notas a CSV")
    archivo_exportar = "tareas_exportadas.csv"  # Nombre del archivo de exportación
    Sql.export_tareas(session, archivo_exportar)
    with open(archivo_exportar, "rb") as file:
        st.download_button(
            label="Descargar Archivo Exportado",
            data=file,
            file_name=archivo_exportar,
            mime="text/csv"
        )
        st.success("Notas exportadas correctamente.")

elif estado_actual == "importar":
    st.subheader("Importar Notas desde un CSV")
    archivo_importar = st.file_uploader("Seleccionar archivo CSV para importar", type="csv")
    if archivo_importar and st.button("Procesar Archivo"):
        try:
            Sql.import_tareas(session, archivo_importar)
            notas = recargar_notas()  # Recargar notas después de la importación
            st.success("Notas importadas correctamente.")
        except Exception as e:
            st.error(f"Error al importar las notas: {e}")
