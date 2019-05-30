###############################
# Creadores: Sebastián López y Daniel Sequeira
# Creado el: 26/05/19 22:30
# Ult. Actualización: 27/05/19 01:40
# Version 0.1.1 Python 3.7.3
###############################
# Importación de Librerias
from funcionesSLH import *
from funcionesDSR import *
import tkinter as tk
from tkinter import *
from tkinter import Tk
from tkinter import ttk
from tkinter import messagebox


# Definición de Funciones


# Creación de GUI
# fondo -> (#395b7f) | imgTEC -> (#1f2e60) | iconos -> (#d1d3d4) | cuadros -> (#f2f2f4) | texto -> (#dee3e9)
raiz = Tk()
raiz.title("Elecciones TEC")
raiz.iconbitmap("icono2.ico")
raiz.config(bg="#395b7f")
raiz.geometry("375x550")
raiz.resizable(0, 0)
frameLogo = Frame(raiz, width=380, height=60, bg='#1f2e60')
frameLogo.grid(row=0, column=0)
imagen = PhotoImage(file='imagen.png')
lImagen = Label(frameLogo, image=imagen, bd=0).place(x=130, y=-17)

raiz.mainloop()


# Programa Principal


# - FIN - #
#####  #####  #####  #   #   ##    #######
#        #    #      #   #   # #  #       #
###      #    #####  #####   #  ##         #
#        #        #  #   #   # #  #       #
#      #####  #####  #   #   ##    #######
