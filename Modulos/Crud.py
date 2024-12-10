import Modulos.BaseDatosJson as BaseDatos
import Modulos.Menu as Menu
import json
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
        marcar = input("¿Desea marcar alguna tarea como completada? (s/n): ")
        if marcar.lower() == 's':
            marcar_como_completada()
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

def exportar_tareas():
    with open('tareas.json', 'w') as archivo:
        json.dump(BaseDatos.Carga(), archivo, indent=4)
    print("Tareas exportadas a tareas.json")
    os.system("pause")
    Menu.menu()

def importar_tareas():
    try:
        with open('tareas.json', 'r') as archivo:
            tareas_importadas = json.load(archivo)
            tareas_existentes=BaseDatos.Carga()
            for tarea in tareas_importadas.values():  # Iteramos solo sobre los valores (diccionarios de tarea)
                nuevo_id = len(tareas_existentes) + 1
                tareas_existentes[nuevo_id] = {'titulo': tarea['titulo'], 'descripcion': tarea['descripcion'], 'estado': tarea['estado']}
                BaseDatos.Guarda(tareas_existentes)
            print("Tareas importadas exitosamente.")
    except FileNotFoundError:
        print("Archivo tareas.json no encontrado.")
    os.system("pause")
    Menu.menu()