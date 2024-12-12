import streamlit as st
import Modulos.BaseDatosJson as BaseDatos
import Modulos.Crud as Crud

# Título de la aplicación
st.title("Aplicación de Notas")

# Cargar las notas desde el archivo JSON
# Función para recargar las notas 
def recargar_notas(): return BaseDatos.Carga()
notas = recargar_notas()

# Mostrar las notas existentes
st.header("Tus Notas")
col1, col2, col3, col4 = st.columns(4)

cols = [col1, col2, col3, col4]
idx = 0

for key, nota in notas.items():
    color = "#d4edda" if nota['estado'] == "completado" else "#f8d7da"  # Verde claro para completado, rojo claro para pendiente
    boton_texto = "Marcar como completado" if nota['estado'] == "pendiente" else "Marcar como pendiente"
    with cols[idx % 4]:
        # st.subheader(f"Nota {key}")
        st.markdown(
            f"""
            <div style="background-color: {color}; padding: 10px; border-radius: 5px;">
                <h4 style='text-align: center;'>{nota['titulo']}</h4>
                <p style='text-align: justify;'>{nota['descripcion']}</p>
                <form action="" method="post">
                <button 
                  type="submit" 
                  name="nota_{key}" 
                  style="
                    width: 100%; 
                    background-color: {color};
                    border: none;
                    color: black; 
                    padding: 10px; 
                    border-radius: 5px;"
                  ></button>
                </form>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button(f"{boton_texto}"):
            Crud.cambiar_estado(key)
            notas = recargar_notas()
    idx += 1

# Añadir una nueva nota
st.header("Añadir una nueva nota")
titulo = st.text_input("Título de la nota")
descripcion = st.text_area("Descripción de la nota")

if st.button("Agregar Nota"):
    if titulo.strip() and descripcion.strip():
        Crud.agregar_nota(titulo, descripcion)
        st.success("¡Nota agregada!")
    else:
        st.error("El título y la descripción no pueden estar vacíos.")

# Eliminar una nota
st.header("Eliminar una Nota")
nota_id = st.selectbox("Selecciona una nota para eliminar", list(notas.keys()))

if st.button("Eliminar Nota"):
    try:
        Crud.eliminar_tarea(nota_id)
        st.success("¡Nota eliminada!")
    except ValueError as e:
        st.error("La nota seleccionada no existe.")
        st.error(str(e))
