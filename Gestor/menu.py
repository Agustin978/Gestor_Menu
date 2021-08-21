"""Menu del programa"""

import helpers
import manager

def loop():
    while True:
        print("\nBienvenido al gestor del restaurante.")
        opcion= input("Ingrese una opcion:\n[1]Agregar una categoria.\n[2]Agregar un plato.\n[3]Mostrar menu.\n[4]Salir del programa.\nOpcion:")
        print("\n")

        helpers.clear()

        if opcion=="1":
            manager.agregar_categorias()
        elif opcion=="2":
            pass 
        elif opcion=="3":
            pass
        elif opcion=="4":
            print("Gracias por usar nuestro programa.")
            break
        else:
            print("No se selecciono una opcion valida.")     