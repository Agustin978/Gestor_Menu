"""Funciones ayuda"""

import os
import platform
import sqlite3

#Funciones para limpiar el boofer
def clear():
    if platform.system()=="Windows":
        os.system("cls")
    else:
        os.system("clear")
"""
def bucle():
    conection= sqlite3.connect("restaurante.db")
    cursor= conection.cursor()


    modifica= input("Ingrese el nombre del plato que desea modificar:\n>")

    try:
        nombre= input("Ingrese el nombre del plato:\n>")
        precio= int(input("Ingrese el valor del plato:\n>"))
        plato=[nombre,precio]
        cursor.execute("UPDATE platos SET nombre={}, precio{}, WHERE nombre={}".format(plato[0], plato[1],modifica))
    except sqlite3.ProgrammingError:
        print("ERROR... No se encontro el plato solicitado. Intentelo nuevamente")
    except ValueError:
        print("Uno de los valores ingresados no es valido. Intente nuevamente")
    finally:
        pass


    categorias= cursor.execute("SELECT * FROM categorias")
    
    while True:
        try:
            for categoria in categorias:
                print("[{}]: {}".format(categoria[0],categoria[1]))

            opcion=int(input("Ingrese la categoria a la que pertenece el plato:\n>"))
            cursor.execute("SELECT * FROM categorias WHERE id={}".format(opcion))
        
        except ValueError:
            print("El valor ingresado no es valido")
        except sqlite3.OperationalError:
            print("El id:{} no corresponde a ninguna categoria almacenada. Intente nuevamente.".format(opcion))
        finally:
            pass

        platos= cursor.execute("SELECT * FROM platos WHERE categoria_id={}".format(opcion))

        #Tengo que hacer todavia el bloque while y for para modificar algun plato de la categoria
        op_2= input("Ingrese el nombre del plato que desea modificar:\n>")
        """




