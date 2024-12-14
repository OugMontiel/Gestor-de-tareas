from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import csv

# Crear el motor de conexión a una base de datos SQLite local
def create_engine_and_base():
    engine = create_engine('sqlite:///tareas.db')
    Base = declarative_base()
    return engine, Base

# Crear el motor de conexión y el modelo Base
engine, Base = create_engine_and_base()

# Definir el modelo de tareas
class Tarea(Base):
    __tablename__ = 'tareas'
    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    descripcion = Column(String)
    estado = Column(Boolean)

    def __repr__(self):
        return f"Tarea(id={self.id}, titulo='{self.titulo}', descripcion='{self.descripcion}', estado={self.estado})"

# Crear las tablas en la base de datos
def create_tables(engine, Base):
    # Definir el modelo de tareas
    class Tarea(Base):
        __tablename__ = 'tareas'
        id = Column(Integer, primary_key=True)
        titulo = Column(String)
        descripcion = Column(String)
        estado = Column(Boolean)

        def __repr__(self):
            return f"Tarea(id={self.id}, titulo='{self.titulo}', descripcion='{self.descripcion}', estado={self.estado})"
    Base.metadata.create_all(engine)

# Crear una sesión
def create_session(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

# Crear una nueva tarea
def add_tarea(session, titulo, descripcion):
    nueva_tarea = Tarea(titulo=titulo, descripcion=descripcion, estado=True)
    session.add(nueva_tarea)
    session.commit()

# Leer tareas
def read_tareas(session):
    tareas = session.query(Tarea).all()
    return tareas

# Cambiar el estado 
def change_estado(session, id):
    tarea_a_actualizar = session.query(Tarea).filter_by(id=id).first()
    if tarea_a_actualizar:
        tarea_a_actualizar.estado = not tarea_a_actualizar.estado
        session.commit()

# Eliminar una tarea
def delete_tarea(session, id):
    tarea_a_eliminar = session.query(Tarea).filter_by(id=id).first()
    if tarea_a_eliminar:
        session.delete(tarea_a_eliminar)
        session.commit()

# Importar tareas desde un archivo CSV
def import_tareas(session, archivo_csv):
    with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            add_tarea(session, row['titulo'], row['descripcion'], row['estado'])

# Exportar tareas a un archivo CSV
def export_tareas(session, archivo_csv):
    tareas = session.query(Tarea).all()
    with open(archivo_csv, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['id', 'titulo', 'descripcion', 'estado']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for tarea in tareas:
            writer.writerow({'id': tarea.id, 'titulo': tarea.titulo, 'descripcion': tarea.descripcion, 'estado': tarea.estado})

