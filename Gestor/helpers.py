"""Funciones ayuda"""

import os
import platform

#Funciones para limpiar el boofer
def clear():
    if platform.system()=="Windows":
        os.system("cls")
    else:
        os.system("clear")