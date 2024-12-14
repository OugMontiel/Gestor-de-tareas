import streamlit as st
import SqlAlchemy as Sql

# Crear el motor de conexión y el modelo Base
engine, Base = Sql.create_engine_and_base()

# Crear las tablas en la base de datos
Sql.create_tables(engine, Base)

# Crear una sesión
session = Sql.create_session(engine)

# Título de la aplicación
st.title("Aplicación de Notas")

# Función para recargar las notas 
def recargar_notas(): return Sql.read_tareas(session)
notas = recargar_notas()

# Mostrar las tareas en columnas
for tarea in notas:
    color = "#d4edda" if tarea.estado else "#f8d7da"  # Verde claro para completado, rojo claro para pendiente
    boton_texto = "Marcar como completado" if not tarea.estado else "Marcar como pendiente"
    
    with cols[idx % 4]:
        st.markdown(
            f"""
            <div style="background-color: {color}; padding: 10px; border-radius: 5px;">
                <h4 style='text-align: center;'>{tarea.titulo}</h4>
                <p style='text-align: justify;'>{tarea.descripcion}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button(f"{boton_texto} ({tarea.id})"):
            Sql.change_estado(session, tarea.id)
            notas = recargar_notas()
    idx += 1


# # Añadir una nueva nota
# st.header("Añadir una nueva nota")
# titulo = st.text_input("Título de la nota")
# descripcion = st.text_area("Descripción de la nota")

# if st.button("Agregar Nota"):
#     if titulo.strip() and descripcion.strip():
#         Sql.agregar_nota(titulo, descripcion)
#         st.success("¡Nota agregada!")
#     else:
#         st.error("El título y la descripción no pueden estar vacíos.")

# # Eliminar una nota
# st.header("Eliminar una Nota")
# nota_id = st.selectbox("Selecciona una nota para eliminar", list(notas.keys()))

# if st.button("Eliminar Nota"):
#     try:
#         Sql.eliminar_tarea(nota_id)
#         st.success("¡Nota eliminada!")
#     except ValueError as e:
#         st.error("La nota seleccionada no existe.")
#         st.error(str(e))
