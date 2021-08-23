"""Administrador de la base de datos"""

from os import PathLike
import sqlite3
from sqlite3.dbapi2 import Cursor, connect
import helpers

def crear_db():
    conection= sqlite3.connect("restaurante.db")
    cursor= conection.cursor()

    #Bloque try catch por si la tabla de categorias ya existe
    try:
        cursor.execute('''CREATE TABLE categorias(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre VARCHAR(100) UNIQUE NOT NULL)
                    ''')
    except sqlite3.OperationalError:
        print("La tabla de categorias ya fue creada.")
    else:
        print("La tabla de categorias se creo correctamente.")
    finally:
        pass

    #Bloque try catch por si la tabla de los platos ya existe
    try:
        cursor.execute('''CREATE TABLE platos(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre VARCHAR(100) UNIQUE NOT NULL,
                    precio FLOAT NOT NULL,
                    categoria_id INTEGER NOT NULL,
                    FOREIGN KEY(categoria_id) REFERENCES categoria(id))
                    ''')
    except sqlite3.OperationalError:
        print("La tabla de platos ya fue creada.")
    else:
        print("La tabla de Platos se creo correctamente")
    finally:
        pass

    #Cierre de la coneccion
    conection.close()

#Funcion para la creacion de las categorias
def agregar_categorias():
    categoria=input("Ingrese el nombre de la nueva categoria:\n>")

    conection= sqlite3.connect("restaurante.db")
    cursor= conection.cursor()

    #Bloque try catch para no ingresar categorias repatidas
    try:
        cursor.execute("INSERT INTO categorias VALUES (null,'{}')".format(categoria))
    except sqlite3.IntegrityError:
        print("La categoria '{}' ya se encuentra creada en la base de datos del Restaurante".format(categoria))
    else:
        print("La categoria '{}' se creo exitosamente.".format(categoria))
    finally:
        pass

    #Realizo el comit a la base y el cierre de la coneccion
    conection.commit()
    conection.close()

#Funcion para agregar patos a las categorias
def agregar_plato():
    conection= sqlite3.connect("restaurante.db")
    cursor= conection.cursor()

    categorias= cursor.execute("SELECT * FROM categorias").fetchall()
    print("\nInfgrese a que categoria pertenece el plato a ingresar")

    for categoria in categorias:
        print("[{}]: {}".format(categoria[0], categoria[1]))
    
    opcion= int(input("Seleccione la categoria:\n>"))
    nombre= input("Ingrese el nombre del nuevo plato:\n>")
    precio= float(input("Ingrese el valor del plato:\n>"))
    plato=[nombre, precio]

    #Bloque try catch para evitar ingresar un plato ya exixstente
    try:
        cursor.execute("INSERT INTO platos VALUES (null, '{}',{}, {})".format(plato[0],plato[1],opcion))
    except sqlite3.IntegrityError:
        print("El plato '{}' ya se encuentra almacenado en la base de datos del restaurante.".format(plato))
    else:
        print("El plato '{}' se almaceno correctamente en la base de datos.".format(plato))
    finally:
        pass

    #Realizo el comit y el cierre de la base de datos
    conection.commit()
    conection.close()

#Funcion para la muestra del menu completo del restaurante
def mostrar_menu():
    conection= sqlite3.connect("restaurante.db")
    cursor= conection.cursor()
    
    helpers.clear()
    categorias= cursor.execute("SELECT * FROM categorias").fetchall()
    for categoria in categorias:
        print("\n\t{}".format(categoria[1]))
        platos= cursor.execute("SELECT * FROM platos WHERE categoria_id={}".format(categoria[0]))
        for plato in platos:
            print("[{}]: {} ${}".format(plato[0], plato[1], plato[2]))
    
    #Cierre de la coneccion con la base de datos
    conection.close()

#Funcion para eliminar platos del menu del restaurante
def eliminar_plato():
    conection= sqlite3.connect("restaurante.db")
    cursor= conection.cursor()

    categorias= cursor.execute("SELECT * FROM categorias").fetchall()
    print("Ingrese a que categoria pertenece el plato que desea eliminar:")

    for categoria in categorias:
        print("[{}]: {}".format(categoria[0], categoria[1]))
    
    opcion= int(input("Seleccione la categoria:\n>"))

    for categoria in categorias:
        
        if categoria[0]==opcion:
            
            platos= cursor.execute("SELECT * FROM platos WHERE categoria_id={}".format(categoria[0]))
            print("Seleccione el plato que desea eliminar:")
            
            for plato in platos:
                print("[{}]: {} ${}".format(plato[0], plato[1], plato[2]))
            
            try:
                op= int(input("Ingrese el numero del plato que desea eliminar:\n>"))
                cursor.execute("DELETE FROM platos WHERE id={}".format(op))
            except ValueError:
                print("Error al ingresar el id, el valor '{}' no es valido. Intente nuevamente.".format(op))
            finally:
                pass

            print("Lista de platos de {}".format(categoria[1]))
            for plato in platos:
                print("[{}]: {} ${}".format(plato[0], plato[1], plato[2]))
            
            #Realizo el comit y cierro la coneccion con la base de datos
            conection.commit()
            conection.close()

#Funcion para modificar datos de algun plato
def modificar_plato():
    helpers.clear()
    conection= sqlite3.connect("restaurante.db")
    cursor= conection.cursor()


    modifica= input("Ingrese el nombre del plato que desea modificar:\n>")

    try:
        nombre= input("Ingrese el nombre del plato:\n>")
        precio= float(input("Ingrese el valor del plato:\n>"))
        plato=[nombre,precio]
        cursor.execute("UPDATE platos SET nombre={}, precio={} WHERE nombre={}".format(plato[0], plato[1],modifica))
    except sqlite3.ProgrammingError:
        print("ERROR... No se encontro el plato solicitado. Intentelo nuevamente")
    except ValueError:
        print("Uno de los valores ingresados no es valido. Intente nuevamente")
    finally:
        pass
    conection.commit()
    conection.close()
    


    
                

#Llamada a la funcion para crear la base de datos
crear_db()


