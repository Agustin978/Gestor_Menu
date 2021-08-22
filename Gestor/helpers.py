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

def bucle():
    conection= sqlite3.connect("restaurante.db")
    cursor= conection.cursor()

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





