import Modulos.BaseDatosJson as BaseDatos

def agregar_tarea(titulo, descripcion):
    tareas=BaseDatos.Carga()
    tarea_id = len(tareas) + 1  # Asigna un ID único a cada tarea
    tareas[tarea_id] = {
        'titulo': titulo, 
        'descripcion': descripcion, 
        'estado': 'pendiente'
    }
    BaseDatos.Guarda(tareas)

def eliminar_tarea(tarea_id):
    tareas=BaseDatos.Carga()
    if tarea_id in tareas:
        del tareas[tarea_id]
        BaseDatos.Guarda(tareas)
    else:
        raise ValueError("La nota no existe.")

# def marcar_como_completada():
#     tareas=BaseDatos.Carga()
#     tarea_id = str(input("Ingrese el ID de la tarea a marcar como completada: "))
#     if tarea_id in tareas:
#         tareas[tarea_id]['estado'] = 'completado'
#         print("Tarea marcada como completada.")
#         BaseDatos.Guarda(tareas)
#     else:
#         print("Tarea no encontrada.")
    
# def exportar_tareas():
#     with open('tareas.json', 'w') as archivo:
#         json.dump(BaseDatos.Carga(), archivo, indent=4)
#     print("Tareas exportadas a tareas.json")
#     os.system("pause")
#     Menu.menu()

# def importar_tareas():
#     try:
#         with open('tareas.json', 'r') as archivo:
#             tareas_importadas = json.load(archivo)
#             tareas_existentes=BaseDatos.Carga()
#             for tarea in tareas_importadas.values():  # Iteramos solo sobre los valores (diccionarios de tarea)
#                 nuevo_id = len(tareas_existentes) + 1
#                 tareas_existentes[nuevo_id] = {'titulo': tarea['titulo'], 'descripcion': tarea['descripcion'], 'estado': tarea['estado']}
#                 BaseDatos.Guarda(tareas_existentes)
#             print("Tareas importadas exitosamente.")
#     except FileNotFoundError:
#         print("Archivo tareas.json no encontrado.")
#     os.system("pause")
#     Menu.menu()