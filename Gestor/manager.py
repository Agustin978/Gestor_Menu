"""Administrador de la base de datos"""

import sqlite3
from sqlite3.dbapi2 import Cursor, connect
from typing_extensions import Concatenate

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
