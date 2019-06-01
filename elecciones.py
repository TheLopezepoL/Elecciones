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
def validarCandidato():
    global lisPro
    if not lisPro:
        messagebox.showerror('No se puede realiizar la accion', 'No hay profesores inscritos en el sistema para '
                                                                'registrar candidatos.')
    else:
        abrirCandidato()
    return ''

def abrirCandidato():
    raiz.withdraw()
    vcandidato = tk.Toplevel()
    vcandidato.mainloop()


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
icoCan = PhotoImage(file='icoCan.png')
icoGen = PhotoImage(file='icogen.png')
icoCar = PhotoImage(file='icoCar.png')
icoRep = PhotoImage(file='icoRep.png')
lImagen = Label(frameLogo, image=imagen, bd=0).place(x=133, y=-17)
botMiembro = Button(raiz, image=icoCan, bg='#395b7f', bd=0)
botMiembro.config(cursor='hand2')
botMiembro.place(x=55, y=100)
botCandidato = Button(raiz, image=icoCan, bg='#395b7f', bd=0, command=validarCandidato)
botCandidato.config(cursor='hand2')
botCandidato.place(x=220, y=100)
botCargar = Button(raiz, image=icoCar, bg='#395b7f', bd=0)
botCargar.config(cursor='hand2')
botCargar.place(x=55, y=250)
botGenerar = Button(raiz, image=icoGen, bg='#395b7f', bd=0)
botGenerar.config(cursor='hand2')
botGenerar.place(x=220, y=250)
botRegistro = Button(raiz, image=icoRep, bg='#395b7f', bd=0)
botRegistro.config(cursor='hand2')
botRegistro.place(x=138, y=400)
texMiembro = Label(raiz, text='Registrar Miembro', bd=0)
texMiembro.place(x=55, y=200)
texMiembro.config(bg='#395b7f', fg='#d1d3d4', cursor='hand2', width=15)
texCandidato = Label(raiz, text='Registrar Candidato', bd=0)
texCandidato.place(x=220, y=200)
texCandidato.config(bg='#395b7f', fg='#d1d3d4', cursor='hand2', width=15)
texCargar = Label(raiz, text='Cargar Datos', bd=0)
texCargar.place(x=55, y=350)
texCargar.config(bg='#395b7f', fg='#d1d3d4', cursor='hand2', width=15)
texGenerar = Label(raiz, text='Generar Votacion', bd=0)
texGenerar.place(x=220, y=350)
texGenerar.config(bg='#395b7f', fg='#d1d3d4', cursor='hand2', width=15)
texRegistro = Label(raiz, text='Mostar Registros', bd=0)
texRegistro.place(x=138, y=500)
texRegistro.config(bg='#395b7f', fg='#d1d3d4', cursor='hand2', width=15)
raiz.mainloop()


# Programa Principal


# - FIN - #
#####  #####  #####  #   #   ##    #######
#        #    #      #   #   # #  #       #
###      #    #####  #####   #  ##         #
#        #        #  #   #   # #  #       #
#      #####  #####  #   #   ##    #######
