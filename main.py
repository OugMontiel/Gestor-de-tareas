import streamlit as st
import Modulos.BaseDatosJson as BaseDatos


# Título de la aplicación
st.title("Aplicación de Notas")

# Cargar las notas desde el archivo JSON
notas = BaseDatos.Carga()

# Mostrar las notas existentes
st.header("Tus Notas")
for key, nota in notas.items():
    st.subheader(f"Nota {key}")
    st.text(f"Título: {nota['titulo']}")
    st.text(f"Descripción: {nota['descripcion']}")
    st.text(f"Estado: {nota['estado']}")

# Añadir una nueva nota
st.header("Añadir una nueva nota")
titulo = st.text_input("Título de la nota")
descripcion = st.text_area("Descripción de la nota")
estado = st.selectbox("Estado de la nota", ["pendiente", "completado"])

if st.button("Agregar Nota"):
    if titulo.strip() and descripcion.strip():
        nueva_nota_id = str(len(notas) + 1)
        notas[nueva_nota_id] = {
            "titulo": titulo,
            "descripcion": descripcion,
            "estado": estado
        }
        BaseDatos.Guarda(notas)
        st.success("¡Nota agregada!")
    else:
        st.error("El título y la descripción no pueden estar vacíos.")

# Eliminar una nota
st.header("Eliminar una Nota")
nota_id = st.selectbox("Selecciona una nota para eliminar", list(notas.keys()))

if st.button("Eliminar Nota"):
    if nota_id in notas:
        del notas[nota_id]
        BaseDatos.Guarda(notas)
        st.success("¡Nota eliminada!")
    else:
        st.error("La nota seleccionada no existe.")
