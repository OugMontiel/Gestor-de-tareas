from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# Importar tareas desde un archivo CSV
import csv

# Crear el motor de conexión a una base de datos SQLite local
def create_engine_and_base():
    engine = create_engine('sqlite:///tareas.db')
    Base = declarative_base()
    return engine, Base

# Definir el modelo de tareas
def define_model(Base):
    class Tarea(Base):
        __tablename__ = 'tareas'
        id = Column(Integer, primary_key=True)
        titulo = Column(String)
        descripcion = Column(String)
        estado = Column(Boolean)
    return Tarea

# Crear las tablas en la base de datos
def create_tables(engine, Base):
    Base.metadata.create_all(engine)

# Crear una sesión
def create_session(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

# Crear una nueva tarea
def add_tarea(session, titulo, descripcion, estado):
    nueva_tarea = Tarea(titulo=titulo, descripcion=descripcion, estado=estado)
    session.add(nueva_tarea)
    session.commit()

# Leer tareas
def read_tareas(session):
    tareas = session.query(Tarea).all()
    for tarea in tareas:
        print(tarea.titulo, tarea.descripcion, tarea.estado)

# Actualizar una tarea
def update_tarea(session, id, nuevo_titulo=None, nueva_descripcion=None, nuevo_estado=None):
    tarea_a_actualizar = session.query(Tarea).filter_by(id=id).first()
    if tarea_a_actualizar:
        if nuevo_titulo:
            tarea_a_actualizar.titulo = nuevo_titulo
        if nueva_descripcion:
            tarea_a_actualizar.descripcion = nueva_descripcion
        if nuevo_estado is not None:
            tarea_a_actualizar.estado = nuevo_estado
        session.commit()

# Eliminar una tarea
def delete_tarea(session, id):
    tarea_a_eliminar = session.query(Tarea).filter_by(id=id).first()
    if tarea_a_eliminar:
        session.delete(tarea_a_eliminar)
        session.commit()


def import_tareas(session, archivo_csv):
    with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            estado = row['estado'].lower() in ['true', '1', 'yes']
            add_tarea(session, row['titulo'], row['descripcion'], estado)

# Exportar tareas a un archivo CSV
def export_tareas(session, archivo_csv):
    tareas = session.query(Tarea).all()
    with open(archivo_csv, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['id', 'titulo', 'descripcion', 'estado']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for tarea in tareas:
            writer.writerow({'id': tarea.id, 'titulo': tarea.titulo, 'descripcion': tarea.descripcion, 'estado': tarea.estado})

if __name__ == "__main__":
    # Crear el motor y la base
    engine, Base = create_engine_and_base()

    # Definir el modelo
    Tarea = define_model(Base)

    # Crear las tablas
    create_tables(engine, Base)

    # Crear una sesión
    session = create_session(engine)

    # # Añadir una nueva tarea
    # add_tarea(session, 'Comprar leche', 'Comprar leche en el supermercado', True)

    # # Leer tareas
    # read_tareas(session)

    # # Actualizar una tarea
    # update_tarea(session, 1, nuevo_estado=False)

    # # Eliminar una tarea
    # delete_tarea(session, 1)

    # # Importar tareas desde un archivo CSV
    # import_tareas(session, 'tareas_importadas.csv')

    # # Exportar tareas a un archivo CSV
    # export_tareas(session, 'tareas_exportadas.csv')