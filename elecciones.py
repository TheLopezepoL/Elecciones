###############################
# Creadores: Sebastián López y Daniel Sequeira
# Creado el: 26/05/19 22:30
# Ult. Actualización: 27/05/19 01:40
# Version 0.1.1 Python 3.7.3
###############################
# Importación de Librerias
from funcionesSLH import *
from CrearPersonas import *
import tkinter as tk
from tkinter import *
from tkinter import Tk
from tkinter import ttk
from tkinter import messagebox

# Variables Globales
typeObj = 0
numCed = ''
strNom = ''
numTel = ''
numCar = ''
typeCur = 0
typePue = 0
strPub = ''


# VENTANA
ventana = ''
raiz = ''
tpub = ''


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
    global raiz
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
    global typeObj
    global ventana
    global numCed
    global strNom
    global numTel
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
    lced.place(x=25, y=75)
    tced = Entry(ventana, bg='#d1d3d4', fg='#403f3d', bd=0, relief='flat', textvariable=numCed)
    tced.config(width='13', font=('Helvetica', 11))
    tced.place(x=80, y=75)
    lnom = Label(ventana, text='Nombre Completo: ', bd=0)
    lnom.config(fg='#d1d3d4', bg='#395b7f', font=('Helvetica', 11))
    lnom.place(x=25, y=105)
    tnom = Entry(ventana, bg='#d1d3d4', fg='#403f3d', bd=0, relief='flat', textvariable=strNom)
    tnom.config(width='25', font=('Helvetica', 11))
    tnom.place(x=153, y=105)
    ltel = Label(ventana, text='Telefono: ', bd=0)
    ltel.config(fg='#d1d3d4', bg='#395b7f', font=('Helvetica', 11))
    ltel.place(x=25, y=135)
    ttel = Entry(ventana, bg='#d1d3d4', fg='#403f3d', bd=0, relief='flat', textvariable=numTel)
    ttel.config(width='13', font=('Helvetica', 11))
    ttel.place(x=89, y=135)
    oest = Radiobutton(ventana, text='Estudiante', variable=typeObj, value=1, command=miembroEst)
    oest.config(bg='#395b7f', fg='#d1d3d4', font=('Helvetica', 11), cursor='hand2')
    oest.place(x=25, y=165)
    opro = Radiobutton(ventana, text='Profesor', variable=typeObj, value=2, command=miembroPro)
    opro.config(bg='#395b7f', fg='#d1d3d4', font=('Helvetica', 11), cursor='hand2')
    opro.place(x=25, y=195)
    oadm = Radiobutton(ventana, text='Administrativo', variable=typeObj, value=3, command=miembroAdm)
    oadm.config(bg='#395b7f', fg='#d1d3d4', font=('Helvetica', 11), cursor='hand2')
    oadm.place(x=25, y=225)
    ldis = Label(ventana, bd=0)
    ldis.config(width=54, height=13, bg='#395b7f')
    ldis.place(x=0, y=265)
    tret = Entry(ventana, bg='#395b7f', fg='red', bd=0, relief='flat')
    tret.config(width='36', font=('Helvetica', 11), cursor='arrow')
    tret.place(x=45, y=470)
    breg = Button(ventana, text='Registrar', bg='#d1d3d4', fg='#403f3d', font=('Helvetica', 11))
    breg.config(width="7", height="1", bd=3, relief='raised', cursor='hand2')
    breg.place(x=75, y=505)
    blim = Button(ventana, text='Limpiar', bg='#d1d3d4', fg='#403f3d', font=('Helvetica', 11), command=limpiar)
    blim.config(width="7", height="1", bd=3, relief='raised', cursor='hand2')
    blim.place(x=225, y=505)
    ventana.mainloop()
    return ''


def limpiar():
    global numCar
    global ventana
    typeObj.set(0)
    numCed.set('')
    strNom.set('')
    numTel.set('')
    numCar = ''
    typeCur.set('')
    typePue.set('')
    ventana.withdraw()
    abrirMiembro()
    return ''


def miembroEst():
    global ventana
    ventana.withdraw()
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
    lced.place(x=25, y=75)
    tced = Entry(ventana, bg='#d1d3d4', fg='#403f3d', bd=0, relief='flat', textvariable=numCed)
    tced.config(width='13', font=('Helvetica', 11))
    tced.place(x=80, y=75)
    lnom = Label(ventana, text='Nombre Completo: ', bd=0)
    lnom.config(fg='#d1d3d4', bg='#395b7f', font=('Helvetica', 11))
    lnom.place(x=25, y=105)
    tnom = Entry(ventana, bg='#d1d3d4', fg='#403f3d', bd=0, relief='flat', textvariable=strNom)
    tnom.config(width='25', font=('Helvetica', 11))
    tnom.place(x=153, y=105)
    ltel = Label(ventana, text='Telefono: ', bd=0)
    ltel.config(fg='#d1d3d4', bg='#395b7f', font=('Helvetica', 11))
    ltel.place(x=25, y=135)
    ttel = Entry(ventana, bg='#d1d3d4', fg='#403f3d', bd=0, relief='flat', textvariable=numTel)
    ttel.config(width='13', font=('Helvetica', 11))
    ttel.place(x=89, y=135)
    oest = Radiobutton(ventana, text='Estudiante', variable=typeObj, value=1, command=miembroEst)
    oest.config(bg='#395b7f', fg='#d1d3d4', font=('Helvetica', 11), cursor='hand2')
    oest.place(x=25, y=165)
    opro = Radiobutton(ventana, text='Profesor', variable=typeObj, value=2, command=miembroPro)
    opro.config(bg='#395b7f', fg='#d1d3d4', font=('Helvetica', 11), cursor='hand2')
    opro.place(x=25, y=195)
    oadm = Radiobutton(ventana, text='Administrativo', variable=typeObj, value=3, command=miembroAdm)
    oadm.config(bg='#395b7f', fg='#d1d3d4', font=('Helvetica', 11), cursor='hand2')
    oadm.place(x=25, y=225)
    ldis = Label(ventana, bd=0)
    ldis.config(width=54, height=13, bg='#395b7f')
    ldis.place(x=0, y=265)
    tret = Entry(ventana, bg='#395b7f', fg='red', bd=0, relief='flat')
    tret.config(width='36', font=('Helvetica', 11), cursor='arrow')
    tret.place(x=45, y=470)
    breg = Button(ventana, text='Registrar', bg='#d1d3d4', fg='#403f3d', font=('Helvetica', 11))
    breg.config(width="7", height="1", bd=3, relief='raised', cursor='hand2')
    breg.place(x=75, y=505)
    blim = Button(ventana, text='Limpiar', bg='#d1d3d4', fg='#403f3d', font=('Helvetica', 11), command=limpiar)
    blim.config(width="7", height="1", bd=3, relief='raised', cursor='hand2')
    blim.place(x=225, y=505)

    lcar = Label(ldis, text='Carnet: ', bd=0)
    lcar.config(fg='#d1d3d4', bg='#395b7f', font=('Helvetica', 11))
    lcar.place(x=25, y=10)
    tcar = Entry(ldis, bg='#d1d3d4', fg='#403f3d', bd=0, relief='flat', textvariable=numCar)
    tcar.config(width='13', font=('Helvetica', 11))
    tcar.place(x=80, y=10)
    lcur = Label(ldis, text='Carrera: ', bd=0)
    lcur.config(fg='#d1d3d4', bg='#395b7f', font=('Helvetica', 11))
    lcur.place(x=25, y=40)

    mcur = Menubutton(ldis, text='Seleccione una carrera')
    mcur.menu = Menu(mcur, tearoff=0)
    mcur["menu"] = mcur.menu
    mcur.config(bg='#d1d3d4', fg='#403f3d', cursor='hand2', font=('Helvetica', 9))

    mcur.menu.add_radiobutton(label='CI - Ingenieria en Computacion', variable=typeCur, value=1)
    mcur.menu.add_radiobutton(label='ATI - Administracion de la Informacion', variable=typeCur, value=2)
    mcur.menu.add_radiobutton(label='E - Electronica', variable=typeCur, value=3)
    mcur.menu.add_radiobutton(label='AE - Administracion de Empresas', variable=typeCur, value=4)
    mcur.menu.add_radiobutton(label='CA - Ingenieria en Computadoras', variable=typeCur, value=5)

    mcur.place(x=82, y=40)

    ventana.mainloop()
    return ''


def miembroPro():
    global tpub
    global ventana
    ventana.withdraw()
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
    lced.place(x=25, y=75)
    tced = Entry(ventana, bg='#d1d3d4', fg='#403f3d', bd=0, relief='flat', textvariable=numCed)
    tced.config(width='13', font=('Helvetica', 11))
    tced.place(x=80, y=75)
    lnom = Label(ventana, text='Nombre Completo: ', bd=0)
    lnom.config(fg='#d1d3d4', bg='#395b7f', font=('Helvetica', 11))
    lnom.place(x=25, y=105)
    tnom = Entry(ventana, bg='#d1d3d4', fg='#403f3d', bd=0, relief='flat', textvariable=strNom)
    tnom.config(width='25', font=('Helvetica', 11))
    tnom.place(x=153, y=105)
    ltel = Label(ventana, text='Telefono: ', bd=0)
    ltel.config(fg='#d1d3d4', bg='#395b7f', font=('Helvetica', 11))
    ltel.place(x=25, y=135)
    ttel = Entry(ventana, bg='#d1d3d4', fg='#403f3d', bd=0, relief='flat', textvariable=numTel)
    ttel.config(width='13', font=('Helvetica', 11))
    ttel.place(x=89, y=135)
    oest = Radiobutton(ventana, text='Estudiante', variable=typeObj, value=1, command=miembroEst)
    oest.config(bg='#395b7f', fg='#d1d3d4', font=('Helvetica', 11), cursor='hand2')
    oest.place(x=25, y=165)
    opro = Radiobutton(ventana, text='Profesor', variable=typeObj, value=2, command=miembroPro)
    opro.config(bg='#395b7f', fg='#d1d3d4', font=('Helvetica', 11), cursor='hand2')
    opro.place(x=25, y=195)
    oadm = Radiobutton(ventana, text='Administrativo', variable=typeObj, value=3, command=miembroAdm)
    oadm.config(bg='#395b7f', fg='#d1d3d4', font=('Helvetica', 11), cursor='hand2')
    oadm.place(x=25, y=225)
    ldis = Label(ventana, bd=0)
    ldis.config(width=54, height=13, bg='#395b7f')
    ldis.place(x=0, y=265)
    tret = Entry(ventana, bg='#395b7f', fg='red', bd=0, relief='flat')
    tret.config(width='36', font=('Helvetica', 11), cursor='arrow')
    tret.place(x=45, y=470)
    breg = Button(ventana, text='Registrar', bg='#d1d3d4', fg='#403f3d', font=('Helvetica', 11))
    breg.config(width="7", height="1", bd=3, relief='raised', cursor='hand2')
    breg.place(x=75, y=505)
    blim = Button(ventana, text='Limpiar', bg='#d1d3d4', fg='#403f3d', font=('Helvetica', 11), command=limpiar)
    blim.config(width="7", height="1", bd=3, relief='raised', cursor='hand2')
    blim.place(x=225, y=505)

    lpub = Label(ldis, text='Publicaciones: ', bd=0)
    lpub.config(fg='#d1d3d4', bg='#395b7f', font=('Helvetica', 11))
    lpub.place(x=25, y=30)
    tpub = Text(ldis, bg='#d1d3d4', fg='#403f3d', bd=0, relief='flat')
    tpub.config(width='27', font=('Helvetica', 11))
    tpub.place(x=129, y=25)

    ventana.mainloop()

    return ''


def miembroAdm():
    global ventana
    ventana.withdraw()
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
    lced.place(x=25, y=75)
    tced = Entry(ventana, bg='#d1d3d4', fg='#403f3d', bd=0, relief='flat', textvariable=numCed)
    tced.config(width='13', font=('Helvetica', 11))
    tced.place(x=80, y=75)
    lnom = Label(ventana, text='Nombre Completo: ', bd=0)
    lnom.config(fg='#d1d3d4', bg='#395b7f', font=('Helvetica', 11))
    lnom.place(x=25, y=105)
    tnom = Entry(ventana, bg='#d1d3d4', fg='#403f3d', bd=0, relief='flat', textvariable=strNom)
    tnom.config(width='25', font=('Helvetica', 11))
    tnom.place(x=153, y=105)
    ltel = Label(ventana, text='Telefono: ', bd=0)
    ltel.config(fg='#d1d3d4', bg='#395b7f', font=('Helvetica', 11))
    ltel.place(x=25, y=135)
    ttel = Entry(ventana, bg='#d1d3d4', fg='#403f3d', bd=0, relief='flat', textvariable=numTel)
    ttel.config(width='13', font=('Helvetica', 11))
    ttel.place(x=89, y=135)
    oest = Radiobutton(ventana, text='Estudiante', variable=typeObj, value=1, command=miembroEst)
    oest.config(bg='#395b7f', fg='#d1d3d4', font=('Helvetica', 11), cursor='hand2')
    oest.place(x=25, y=165)
    opro = Radiobutton(ventana, text='Profesor', variable=typeObj, value=2, command=miembroPro)
    opro.config(bg='#395b7f', fg='#d1d3d4', font=('Helvetica', 11), cursor='hand2')
    opro.place(x=25, y=195)
    oadm = Radiobutton(ventana, text='Administrativo', variable=typeObj, value=3, command=miembroAdm)
    oadm.config(bg='#395b7f', fg='#d1d3d4', font=('Helvetica', 11), cursor='hand2')
    oadm.place(x=25, y=225)
    ldis = Label(ventana, bd=0)
    ldis.config(width=54, height=13, bg='#395b7f')
    ldis.place(x=0, y=265)
    tret = Entry(ventana, bg='#395b7f', fg='red', bd=0, relief='flat')
    tret.config(width='36', font=('Helvetica', 11), cursor='arrow')
    tret.place(x=45, y=470)
    breg = Button(ventana, text='Registrar', bg='#d1d3d4', fg='#403f3d', font=('Helvetica', 11))
    breg.config(width="7", height="1", bd=3, relief='raised', cursor='hand2')
    breg.place(x=75, y=505)
    blim = Button(ventana, text='Limpiar', bg='#d1d3d4', fg='#403f3d', font=('Helvetica', 11), command=limpiar)
    blim.config(width="7", height="1", bd=3, relief='raised', cursor='hand2')
    blim.place(x=225, y=505)

    lpue = Label(ldis, text='Puesto: ',  bd=0)
    lpue.config(fg='#d1d3d4', bg='#395b7f', font=('Helvetica', 11))
    lpue.place(x=25, y=30)
    lext = Label(ldis, text='Extencion: ',  bd=0)
    lext.config(fg='#d1d3d4', bg='#395b7f', font=('Helvetica', 11))
    lext.place(x=25, y=70)
    text = Entry(ldis, bg='#d1d3d4', fg='#403f3d', bd=0, relief='flat')
    text.config(width='13', font=('Helvetica', 11))
    text.place(x=100, y=70)

    mpue = Menubutton(ldis, text='Seleccione un puesto')
    mpue.menu = Menu(mpue, tearoff=0)
    mpue["menu"] = mpue.menu
    mpue.config(bg='#d1d3d4', fg='#403f3d', cursor='hand2', font=('Helvetica', 9))

    mpue.menu.add_radiobutton(label='Secretaria', variable=typePue, value=1)
    mpue.menu.add_radiobutton(label='Asistente Administrativa', variable=typePue, value=2)
    mpue.menu.add_radiobutton(label='Coordinador', variable=typePue, value=3)
    mpue.menu.add_radiobutton(label='Director', variable=typePue, value=4)

    mpue.place(x=80, y=30)

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
def programaPrincipal():
    global typeObj
    global numCed
    global strNom
    global numTel
    global numCar
    global typeCur
    global typePue
    global raiz
    global strPub
    raiz = Tk()

    typeObj = IntVar()
    numCed = StringVar()
    strNom = StringVar()
    numTel = StringVar()
    typeCur = IntVar()
    numCar = StringVar()
    typePue = IntVar()

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
    return ''

# Programa Principal

programaPrincipal()

# - FIN - #
#####  #####  #####  #   #   ##    #######
#        #    #      #   #   # #  #       #
###      #    #####  #####   #  ##         #
#        #        #  #   #   # #  #       #
#      #####  #####  #   #   ##    #######
