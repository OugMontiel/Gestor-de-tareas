import Modulos.Crud as Crud
import sys
import os

def menu():
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
    while True:
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
                case 5: Crud.exportar_tareas()
                case 6: Crud.importar_tareas()
                case 7: sys.exit() 
            
        except ValueError:
                print("El valor ingresado no es valido ingrese una opcion valida")