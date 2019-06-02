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
def validarReporte():
    global dicPer
    for k in dicPer:
        for o in dicPer[k]:
            if o.getVoto != 0:
                return abrirReportes()
    return messagebox.showerror('No se puede realizar la accion', 'No se ha generado ninguna votacion para mostrar los '
                                                                  'registros')


def validarVotacion():
    global lisPro
    if lisPro:
        for l in lisPro:
            if l.getActivo:
                return abrirGenerar()
        return messagebox.showerror('No se puede realizar la accion', 'No hay candidatos inscritos en el sistema para'
                                                                      'generar la votacion')
    return messagebox.showerror('No se puede realizar la accion', 'No hay candidatos inscritos en el sistema para '
                                                                  'generar la votacion')


def validarCandidato():
    global lisPro
    if not lisPro:
        return messagebox.showerror('No se puede realizar la accion', 'No hay profesores inscritos en el sistema para '
                                                               'registrar candidatos.')
    else:
        return abrirCandidato()


def abrirCandidato():
    raiz.withdraw()
    vcandidato = tk.Toplevel()
    vcandidato.title("Registrar Candidato")
    vcandidato.iconbitmap("icono2.ico")
    vcandidato.config(bg="#395b7f")
    vcandidato.geometry("375x550")
    vcandidato.resizable(0, 0)
    fcandidato = Frame(vcandidato, width=380, height=60, bg='#1f2e60')
    fcandidato.grid(row=0, column=0)
    imagen = PhotoImage(file='imagen.png')
    lImagen = Label(fcandidato, image=imagen, bd=0).place(x=133, y=-17)
    vcandidato.mainloop()
    return ''


def abrirMiembro():
    raiz.withdraw()
    ventana = tk.Toplevel()
    ventana.title("Registrar Miembro")
    ventana.iconbitmap("icono2.ico")
    ventana.config(bg="#395b7f")
    ventana.geometry("375x550")
    ventana.resizable(0, 0)
    frame = Frame(ventana, width=380, height=60, bg='#1f2e60')
    frame.grid(row=0, column=0)
    imagen = PhotoImage(file='imagen.png')
    lImagen = Label(frame, image=imagen, bd=0).place(x=133, y=-17)
    lced = Label(ventana, text='Cedula: ', bd=0)
    lced.config(fg='#d1d3d4', bg='#395b7f', font=('Helvetica', 11))
    lced.place(x=35, y=100)
    tced = Text(ventana)
    ventana.mainloop()
    return ''


def abrirCargar():
    raiz.withdraw()
    ventana = tk.Toplevel()
    ventana.title("Registrar Miembro")
    ventana.iconbitmap("icono2.ico")
    ventana.config(bg="#395b7f")
    ventana.geometry("375x550")
    ventana.resizable(0, 0)
    frame = Frame(ventana, width=380, height=60, bg='#1f2e60')
    frame.grid(row=0, column=0)
    imagen = PhotoImage(file='imagen.png')
    lImagen = Label(frame, image=imagen, bd=0).place(x=133, y=-17)
    ventana.mainloop()
    return ''


def abrirGenerar():
    raiz.withdraw()
    ventana = tk.Toplevel()
    ventana.title("Registrar Miembro")
    ventana.iconbitmap("icono2.ico")
    ventana.config(bg="#395b7f")
    ventana.geometry("375x550")
    ventana.resizable(0, 0)
    frame = Frame(ventana, width=380, height=60, bg='#1f2e60')
    frame.grid(row=0, column=0)
    imagen = PhotoImage(file='imagen.png')
    lImagen = Label(frame, image=imagen, bd=0).place(x=133, y=-17)
    ventana.mainloop()
    return ''


def abrirReportes():
    raiz.withdraw()
    ventana = tk.Toplevel()
    ventana.title("Registrar Miembro")
    ventana.iconbitmap("icono2.ico")
    ventana.config(bg="#395b7f")
    ventana.geometry("375x550")
    ventana.resizable(0, 0)
    frame = Frame(ventana, width=380, height=60, bg='#1f2e60')
    frame.grid(row=0, column=0)
    imagen = PhotoImage(file='imagen.png')
    lImagen = Label(frame, image=imagen, bd=0).place(x=133, y=-17)
    ventana.mainloop()
    return ''


# Creación de GUI
# fondo -> (#395b7f) | imgTEC -> (#1f2e60) | iconos -> (#d1d3d4) | cuadros -> (#f2f2f4) | texto -> (#d1d3d4)
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
botMiembro = Button(raiz, image=icoCan, bg='#395b7f', bd=0, command=abrirMiembro)
botMiembro.config(cursor='hand2')
botMiembro.place(x=55, y=100)
botCandidato = Button(raiz, image=icoCan, bg='#395b7f', bd=0, command=validarCandidato)
botCandidato.config(cursor='hand2')
botCandidato.place(x=220, y=100)
botCargar = Button(raiz, image=icoCar, bg='#395b7f', bd=0, command=abrirCargar)
botCargar.config(cursor='hand2')
botCargar.place(x=55, y=250)
botGenerar = Button(raiz, image=icoGen, bg='#395b7f', bd=0, command=validarVotacion)
botGenerar.config(cursor='hand2')
botGenerar.place(x=220, y=250)
botRegistro = Button(raiz, image=icoRep, bg='#395b7f', bd=0, command=validarReporte)
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
