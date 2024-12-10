import Modulos.BaseDatosJson as BaseDatos
import Modulos.Menu as Menu
import os

def agregar_tarea():
    tareas=BaseDatos.Carga()
    titulo = input("Ingrese el título de la tarea: ")
    descripcion = input("Ingrese la descripción: ")
    tarea_id = len(tareas) + 1  # Asigna un ID único a cada tarea
    tareas[tarea_id] = {'titulo': titulo, 'descripcion': descripcion, 'estado': 'pendiente'}
    
    BaseDatos.Guarda(tareas)
    print("Tarea agregada exitosamente.")
    os.system("pause")
    Menu.menu()

def listar_tareas():
    tareas=BaseDatos.Carga()
    if not tareas:
        print("No hay tareas pendientes.")
    else:
        for tarea_id, tarea in tareas.items():
            print(f"Tarea {tarea_id}: {tarea['titulo']} - {tarea['descripcion']} ({tarea['estado']})")
    os.system("pause")
    Menu.menu()
            

def marcar_como_completada():
    tareas=BaseDatos.Carga()
    tarea_id = str(input("Ingrese el ID de la tarea a marcar como completada: "))
    if tarea_id in tareas:
        tareas[tarea_id]['estado'] = 'completado'
        print("Tarea marcada como completada.")
        BaseDatos.Guarda(tareas)
    else:
        print("Tarea no encontrada.")
    os.system("pause")
    Menu.menu()

def eliminar_tarea():
    tareas=BaseDatos.Carga()
    tarea_id = str(input("Ingrese el ID de la tarea a eliminar: "))
    if tarea_id in tareas:
        del tareas[tarea_id]
        print("Tarea eliminada.")
        BaseDatos.Guarda(tareas)
    else:
        print("Tarea no encontrada.")
    os.system("pause")
    Menu.menu()
