import Modulos.Crud as Crud
import sys
import os


title="""
        Menú de Gestión de Tareas

"""
ListaMenu=[
        "Agregar tarea",
        "Listar tareas",
        "Marcar como completada",
        "Eliminar tarea",
        "Exportar tareas",
        "Importar tareas",
        "Salir"
]


def menu():
    os.system("cls")
    print(title)
    try:
        [print(f"{i+1}. {item}") for i, item in enumerate(ListaMenu)]
        Op=int(input("Seleccione: >>_"))
        match Op:
            case 1: Crud.agregar_tarea()
            case 2: Crud.listar_tareas()
            case 3: Crud.marcar_como_completada()
            case 4: Crud.eliminar_tarea()
            case 5:
                pass
            case 6:
                pass
            case 7: sys.exit() 
        
    except ValueError:
            print("El valor ingresado no es valido ingrese una opcion valida")