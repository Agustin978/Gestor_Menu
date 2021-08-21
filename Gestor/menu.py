"""Menu del programa"""

import helpers
import manager

def loop():
    while True:
        print("\nBienvenido al gestor del restaurante.")
        opcion= input("Ingrese una opcion:\n[1]Agregar una categoria.\n[2]Agregar un plato.\n[3]Mostrar menu.\n[4]Eliminar un plato.\n[5]Salir del programa.\nOpcion:")
        print("\n")

        helpers.clear()

        if opcion=="1":
            manager.agregar_categorias()
        elif opcion=="2":
            manager.agregar_plato()
        elif opcion=="3":
            manager.mostrar_menu()
        elif opcion=="4":
            manager.eliminar_plato()
        elif opcion=="5":
            print("Gracias por usar nuestro programa.")
            break
        else:
            print("No se selecciono una opcion valida.")     