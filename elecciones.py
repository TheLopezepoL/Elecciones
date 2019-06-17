###############################
# Creadores: Sebastián López y Daniel Sequeira
# Creado el: 26/05/19 22:30
# Ult. Actualización: 27/05/19 01:40
# Version 0.1.1 Python 3.7.3
###############################
# Importación de Librerias
from funcionesSLH import *
import tkinter as tk
from tkinter import *
from tkinter import Tk
from tkinter import ttk
from tkinter import messagebox
import random
import webbrowser
# Variables Globales

typeObj = 0
numCed = ''
strNom = ''
numTel = ''
typeCur = 0
numCar = ''
typePue = 0
numExt = ''
codERROR = ''
numAnno = 2019
cont = 0
# VENTANA
ventana = ''
tpub = ''
tret = ''
nombres = []
anio = 20190000
# Definición de Funciones
def validarReporte():
    global dicPer
    for k in dicPer:
        for o in dicPer[k]:
            if o.getVoto != 0:
                return abrirReportes()
    return messagebox.showerror('No se puede realizar la accion', 'No se ha generado ninguna votacion para mostrar los '
                                                                  'registros')

def reporteCandidatoIndividual():
    reporte = open("ReporteIndividual.html", "w")
    cuerpo = ""
    base = '<!DOCTYPE html> <html lang="en"> <head> \
                              <title>Table V04</title> \
                              <meta charset="UTF-8"> \
                            <meta name="viewport" content="width=device-width, initial-scale=1"> \
                            <link rel="icon" type="image/png" href="images/icons/favicon.ico"/> \
                             <link rel="stylesheet" type="text/css" href="vendor/bootstrap/css/bootstrap.min.css"> \
                             <link rel="stylesheet" type="text/css" href="fonts/font-awesome-4.7.0/css/font-awesome.min.css"> \
                            <link rel="stylesheet" type="text/css" href="vendor/animate/animate.css"> \
                            <link rel="stylesheet" type="text/css" href="vendor/select2/select2.min.css"> \
                         <link rel="stylesheet" type="text/css" href="vendor/perfect-scrollbar/perfect-scrollbar.css"> \
                          <link rel="stylesheet"type="text/css" href="css/util.css"> \
                            <link rel="stylesheet" type="text/css" href="css/main.css"> \
                                                                                      </head> \
                                                                                      <body> <h1> Seguidores por candidato</h1> \
    <div class="limiter">' \
           '<div class="container-table100">' \
                '<div class="wrap-table100">' \
                    ' <div class="table100 ver3 m-b-110">' \
                        ' <div class="table100-head">' \
                            '<table>' \
                                '<thead>' \
                                    '<tr class="row100 head">' \
                                    '<th class="cell100 column1">Nombre</th>' \
                                    '<th class="cell100 column2">cedula</th>' \
                                    '<th class="cell100 column3">tipo</th>' \
                                    '<th class="cell100 column3">Voto por</th>' \
                                    '</tr>' \
                                '</thead>' \
                            '</table>' \
                        '</div>'
    for j in dicPer["Pro"]:
        if j.getActivo():
            for i in dicPer["Pro"]:
                if i.getVoto()==int(j.getCandidatoNum()[-1]):
                    cuerpo = cuerpo + '<div class="table100-body js-pscroll"> \
                        <table> \
                            <tbody> \
                                <tr class="row100 body"> \
                                    <td class="cell100 column1">' + str(i.getNombre()) + '</td> \
                                    <td class="cell100 column2">' + str(i.getCedula()) + '</td> \
                                    <td class="cell100 column3">Profesor</td> \
                                    <td class="cell100 column4">'+str(j.getNombre())+'</td> \
                                </tr> \
                            </tbody> \
                        </table> \
                    </div>'
            for i in dicPer["Adm"]:
                if i.getVoto()==int(j.getCandidatoNum()[-1]):
                    cuerpo = cuerpo + '<div class="table100-body js-pscroll"> \
                        <table> \
                            <tbody> \
                                <tr class="row100 body"> \
                                    <td class="cell100 column1">' + str(i.getNombre()) + '</td> \
                                    <td class="cell100 column2">' + str(i.getCedula()) + '</td> \
                                    <td class="cell100 column3">Administrativo</td> \
                                    <td class="cell100 column4">' + str(j.getNombre()) + '</td> \
                                </tr> \
                            </tbody> \
                        </table> \
                    </div>'
            for i in dicPer["Est"]:
                if i.getVoto()==int(j.getCandidatoNum()[-1]):
                    cuerpo = cuerpo + '<div class="table100-body js-pscroll"> \
                        <table> \
                            <tbody> \
                                <tr class="row100 body"> \
                                    <td class="cell100 column1">' + str(i.getNombre()) + '</td> \
                                    <td class="cell100 column2">' + str(i.getCedula()) + '</td> \
                                    <td class="cell100 column3">Estudiante</td> \
                                      <td class="cell100 column4">' + str(j.getNombre()) + '</td> \
                                </tr> \
                            </tbody> \
                        </table> \
                    </div>'


            cuerpo = cuerpo + "</div>"
            cuerpo = cuerpo + ' <div class="table100 ver3 m-b-110">' \
                        ' <div class="table100-head">' \
                            '<table>' \
                                '<thead>' \
                                    '<tr class="row100 head">' \
                                    '<th class="cell100 column1">Nombre</th>' \
                                    '<th class="cell100 column2">cedula</th>' \
                                    '<th class="cell100 column3">tipo</th>' \
                                    '<th class="cell100 column3">Voto por</th>' \
                              '</tr>' \
                                '</thead>' \
                            '</table>' \
                        '</div>'

    fiin = '</div>' \
           '<script src="vendor/jquery/jquery-3.2.1.min.js"></script>' \
           '<script src="vendor/bootstrap/js/popper.js"></script>' \
           '<script src="vendor/bootstrap/js/bootstrap.min.js"></script>' \
           '<script src="vendor/select2/select2.min.js"></script>' \
           '<script src="vendor/perfect-scrollbar/perfect-scrollbar.min.js"></script>' \
           '<script>' \
           'var ps = new PerfectScrollbar(this);' \
           '$(window).on("resize", function(){' \
           ' ps.update();' \
           '})' \
           '});' \
           '</script>' \
           '<script src="js/main.js"></script>' \
           '</body>' \
           '</html>'

    reporte.write(base + cuerpo + fiin)
    reporte.close()
    webbrowser.open("ReporteIndividual.html")


def crearReporteCantidadxVotante():
    contarVotos2()
    reporte = open("ReporteNoVotantes.html", "w")

    base = '<!DOCTYPE html> <html lang="en"> <head> \
                          <title>Table V04</title> \
                          <meta charset="UTF-8"> \
                        <meta name="viewport" content="width=device-width, initial-scale=1"> \
                        <link rel="icon" type="image/png" href="images/icons/favicon.ico"/> \
                         <link rel="stylesheet" type="text/css" href="vendor/bootstrap/css/bootstrap.min.css"> \
                         <link rel="stylesheet" type="text/css" href="fonts/font-awesome-4.7.0/css/font-awesome.min.css"> \
                        <link rel="stylesheet" type="text/css" href="vendor/animate/animate.css"> \
                        <link rel="stylesheet" type="text/css" href="vendor/select2/select2.min.css"> \
                     <link rel="stylesheet" type="text/css" href="vendor/perfect-scrollbar/perfect-scrollbar.css"> \
                      <link rel="stylesheet"type="text/css" href="css/util.css"> \
                        <link rel="stylesheet" type="text/css" href="css/main.css"> \
                                                                                  </head> \
                                                                                  <body> <h1> Cantidad de votantes por candidato</h1> \
<div class="limiter"><div class="container-table100"><div class="wrap-table100"> <div class="table100 ver1 m-b-110"> <div class="table100-head"><table><thead><tr class="row100 head"><th class="cell100 column1">Nombre</th><th class="cell100 column2">Cantidad</th><th class="cell100 column3">Procentaje</th></tr></thead></table></div>'
    cuerpo = ""



    por = len(dicPer["Pro"]) + len(dicPer["Est"])+ len(dicPer["Adm"])
    for  i in dicPer["Pro"]:
        if i.getActivo():
            print(i.getCanVotos())
            cuerpo = cuerpo + '<div class="table100-body js-pscroll"> \
              <table> \
              <tbody> \
              <tr class="row100 body"> \
              <td class="cell100 column1">'+str(i.getNombre())+'</td> \
              <td class="cell100 column2">'+str(i.getCanVotos())+'</td> \
              <td class="cell100 column3">'+str((i.getCanVotos()/por)*100)+'</td> \
              </tr> \
              </tbody> \
              </table> \
              </div>'



    fiin = '</div>' \
           '<script src="vendor/jquery/jquery-3.2.1.min.js"></script>' \
           '<script src="vendor/bootstrap/js/popper.js"></script>' \
           '<script src="vendor/bootstrap/js/bootstrap.min.js"></script>' \
           '<script src="vendor/select2/select2.min.js"></script>' \
           '<script src="vendor/perfect-scrollbar/perfect-scrollbar.min.js"></script>' \
           '<script>' \
        'var ps = new PerfectScrollbar(this);' \
           '$(window).on("resize", function(){' \
                                ' ps.update();' \
                                '})' \
                                '});' \
           '</script>' \
           '<script src="js/main.js"></script>' \
           '</body>' \
           '</html>'



    reporte.write(base + cuerpo + fiin)
    reporte.close()
    webbrowser.open("ReporteNoVotantes.html")
    print("si")




def crearReporteNoVotantes():
    reporte = open("ReporteNoVotantes.html", "w")

    base = '<!DOCTYPE html> <html lang="en"> <head> \
                          <title>Table V04</title> \
                          <meta charset="UTF-8"> \
                        <meta name="viewport" content="width=device-width, initial-scale=1"> \
                        <link rel="icon" type="image/png" href="images/icons/favicon.ico"/> \
                         <link rel="stylesheet" type="text/css" href="vendor/bootstrap/css/bootstrap.min.css"> \
                         <link rel="stylesheet" type="text/css" href="fonts/font-awesome-4.7.0/css/font-awesome.min.css"> \
                        <link rel="stylesheet" type="text/css" href="vendor/animate/animate.css"> \
                        <link rel="stylesheet" type="text/css" href="vendor/select2/select2.min.css"> \
                     <link rel="stylesheet" type="text/css" href="vendor/perfect-scrollbar/perfect-scrollbar.css"> \
                      <link rel="stylesheet"type="text/css" href="css/util.css"> \
                        <link rel="stylesheet" type="text/css" href="css/main.css"> \
                                                                                  </head> \
                                                                                  <body> <h1> Lista de no votantes en 2019</h1>\
<div class="limiter"><div class="container-table100"><div class="wrap-table100"> <div class="table100 ver1 m-b-110"> <div class="table100-head"><table><thead><tr class="row100 head"><th class="cell100 column1">Cedula</th><th class="cell100 column2">Nombre</th><th class="cell100 column3">Tipo</th></tr></thead></table></div>'
    cuerpo = ""
    for  i in dicPer["Est"]:
        if i.getVoto()==0:
            cuerpo = cuerpo + '<div class="table100-body js-pscroll"> \
              <table> \
              <tbody> \
              <tr class="row100 body"> \
              <td class="cell100 column1">'+str(i.getCedula())+'</td> \
              <td class="cell100 column2">'+str(i.getNombre())+'</td> \
              <td class="cell100 column3">Estudiante</td> \
              </tr> \
              </tbody> \
              </table> \
              </div>'

    for i in dicPer["Pro"]:
        if i.getVoto() == 0:

            cuerpo = cuerpo + '<div class="table100-body js-pscroll"> \
              <table> \
              <tbody> \
              <tr class="row100 body"> \
              <td class="cell100 column1">' + str(i.getCedula()) + '</td> \
              <td class="cell100 column2">' + str(i.getNombre()) + '</td> \
              <td class="cell100 column3"> Profesor</td> \
              </tr> \
              </tbody> \
              </table> \
              </div>'

    for i in dicPer["Adm"]:
        if i.getVoto() == 0:

            cuerpo = cuerpo + '<div class="table100-body js-pscroll"> \
              <table> \
              <tbody> \
              <tr class="row100 body"> \
              <td class="cell100 column1">' + str(i.getCedula()) + '</td> \
              <td class="cell100 column2">' + str(i.getNombre()) + '</td> \
              <td class="cell100 column3">Administrativo</td> \
              </tr> \
              </tbody> \
              </table> \
              </div>'

    fiin = '</div>' \
           '<script src="vendor/jquery/jquery-3.2.1.min.js"></script>' \
           '<script src="vendor/bootstrap/js/popper.js"></script>' \
           '<script src="vendor/bootstrap/js/bootstrap.min.js"></script>' \
           '<script src="vendor/select2/select2.min.js"></script>' \
           '<script src="vendor/perfect-scrollbar/perfect-scrollbar.min.js"></script>' \
           '<script>' \
        'var ps = new PerfectScrollbar(this);' \
           '$(window).on("resize", function(){' \
                                ' ps.update();' \
                                '})' \
                                '});' \
           '</script>' \
           '<script src="js/main.js"></script>' \
           '</body>' \
           '</html>'



    reporte.write(base + cuerpo + fiin)
    reporte.close()
    webbrowser.open("ReporteNoVotantes.html")
    print("si")




def crearReporteCandidatos():
    reporte = open("ReporteCan.html", "w")
    print('"dd"')
    base = '<!DOCTYPE html> <html lang="en"> <head> \
                          <title>Table V04</title> \
                          <meta charset="UTF-8"> \
                        <meta name="viewport" content="width=device-width, initial-scale=1"> \
                        <link rel="icon" type="image/png" href="images/icons/favicon.ico"/> \
                         <link rel="stylesheet" type="text/css" href="vendor/bootstrap/css/bootstrap.min.css"> \
                         <link rel="stylesheet" type="text/css" href="fonts/font-awesome-4.7.0/css/font-awesome.min.css"> \
                        <link rel="stylesheet" type="text/css" href="vendor/animate/animate.css"> \
                        <link rel="stylesheet" type="text/css" href="vendor/select2/select2.min.css"> \
                     <link rel="stylesheet" type="text/css" href="vendor/perfect-scrollbar/perfect-scrollbar.css"> \
                      <link rel="stylesheet"type="text/css" href="css/util.css"> \
                        <link rel="stylesheet" type="text/css" href="css/main.css"> \
                                                                                  </head> \
                                                                                  <body>  <h1> Candidatos para rector en 2019</h1>\
<div class="limiter"><div class="container-table100"><div class="wrap-table100"> <div class="table100 ver1 m-b-110"> <div class="table100-head"><table><thead><tr class="row100 head"><th class="cell100 column1">Cedula</th><th class="cell100 column2">Nombre</th><th class="cell100 column3">Telefono</th><th class="cell100 column4">Publicaciones</th></tr></thead></table></div>'
    cuerpo = ""
    for  i in dicPer["Pro"]:
        if i.getActivo()==True:
            print(i.getActivo())
            cuerpo = cuerpo + '<div class="table100-body js-pscroll"> \
              <table> \
              <tbody> \
              <tr class="row100 body"> \
              <td class="cell100 column1">'+str(i.getCedula())+'</td> \
              <td class="cell100 column2">'+str(i.getNombre())+'</td> \
              <td class="cell100 column3">'+str(i.getTelefono())+'</td> \
              <td class="cell100 column4">'+str(i.getPublicaciones())+'</td> \
              </tr> \
              </tbody> \
              </table> \
              </div>'

    fiin = '</div>' \
           '<script src="vendor/jquery/jquery-3.2.1.min.js"></script>' \
           '<script src="vendor/bootstrap/js/popper.js"></script>' \
           '<script src="vendor/bootstrap/js/bootstrap.min.js"></script>' \
           '<script src="vendor/select2/select2.min.js"></script>' \
           '<script src="vendor/perfect-scrollbar/perfect-scrollbar.min.js"></script>' \
           '<script>' \
        'var ps = new PerfectScrollbar(this);' \
           '$(window).on("resize", function(){' \
                                ' ps.update();' \
                                '})' \
                                '});' \
           '</script>' \
           '<script src="js/main.js"></script>' \
           '</body>' \
           '</html>'
    reporte.write(base + cuerpo + fiin)
    reporte.close()
    webbrowser.open("ReporteCan.html")
    print("si")

def crear(cantidadX):
    if messagebox.askokcancel("Está seguro?","Desea crear "+str(cantidadX)+" personas?"):
        #try:
        pcantidad = int(cantidadX)
        print("cantidad a crear:", pcantidad)
        if pcantidad > 100 or pcantidad < 1:
            messagebox.showerror('No se puede realizar la accion', 'Debe ser un numero entre 1 y 100')
        else:
            for i in range(pcantidad):
                nombres.append(listaNombres[random.randint(0, len(listaNombres) - 1)] + " " + listaApellidos[
                    random.randint(0, len(listaApellidos) - 1)] + " " + listaApellidos[
                                   random.randint(0, len(listaApellidos) - 1)])
                print("Nombre creado:", nombres[i])
                cedula = random.randint(100000000, 799999999)
                telefono = random.randint(60000000, 89999999)
                azar = random.randint(0, 30)
                print("Se creo a:",nombres)
                if azar <= 5:
                    objeto = Administrativo(listaPuestos[random.randint(0,len(listaPuestos)-1)],random.randint(1100,9999) , cedula,nombres[i], telefono,0)


                    lisAdm.append(objeto)
                elif azar < 20:
                    objeto = Estudiante(anio + random.randint(1, 9999),listaCarreras[random.randint(0,len(listaCarreras)-1)], cedula, nombres[i],telefono,0)

                    lisEst.append(objeto)
                else:
                    #objeto = Profesor(1, False, cedula, nombres[i], telefono, 0, True)
                    objeto= Profesor("Publicacion",cedula,nombres[i],telefono)
                    print("Cedula de un profesor:",cedula)
                    print("nombre",objeto.getNombre())
                    print("cedula",objeto.getCedula())
                    print("telefono",objeto.getTelefono())
                    print("voto",objeto.getVoto())
                    print("publicaciones",objeto.getPublicaciones())
                    print("candidato",objeto.getCandidato())
                    print("activo",objeto.getActivo())
                    print("cantidad de votos",objeto.getCanVotos())
                    lisPro.append(objeto)


        #except:
        #    messagebox.showerror('No se puede realizar la accion', 'Debe ser unicamente un valor numerico')
        escribir()

def escribir():

    f = open("file.txt", "w")
    f.write(str(dicPer))
    #pickle.dump(clase.dicPer, f)
    f.close()
    print("Termino")
    print(dicPer)

def dlimpiar():
    textboxTitulo.insert(END, 'a')  # limpia el label

listaCarreras = ["Computacion", "Computadores", "Mecatronica", "Ambiental",
                     "Ingenieria de la Republica independiente de Forestal",
                     "Materiales", "Administracion", "Ati", "Agronomia"]
listaNombres = ["Daniel", "Sebastian", "Jan", "Jafet", "Ariel", "Hillary",
                    "Paula", "Sofia", "Muffin", "Maria", "Sylvia", "Giovanna", "Gimena",
                    "Thanos", "Alex", "Kenneth", "Diego", "Erick", "Bartolome", "Anastacio",
                    "Isidro", "Benito", "Batman", "Yolanda", "Sacarias", "Armando", "Susana",
                    "Yoda", "Jotaro", "Jospeh", "Jonathan", "Giorno", "Dio", "Goku", "Abbacchio",
                    "Speed", "Apellidon't", "Bucciarati", "Polnareff", "Abdol", "Caesar",
                    "Josuke", "Narancia", "Mista", "Iggy", "Aqua"]

listaApellidos = ["Joestar", "Horia", "Piedras", "Rios", "Sequeira", "Gomez", "Jupas", "XVII",
                      "ACDC", "Parada", "Wagon", "Snow", "Sama", "Kujo", "Retana", "Lopez", "Sparrow",
                      "Stark", "Rogers", "Balboa", "Schwarzenegger", "3000", "Camelas", "Del Rio",
                      "De Luz del Topo", "Joestar", "Jr", "Pool", "Gatjens", "SantaMaria", "Casas",
                      "Moffin", "Ghost", "Java", "C++", "Pokemon", "Nombren't", "Joestar", "BadBunny",
                      "Yu-Gi-Oh", "Miyamoto", "MarioBros", "Abalahama", "Danvers", "Odinson", "404NotFound"]
listaPuestos = ["Auxiliar", "Coordinador", "Secretarix", "Interino", "Administrador", "Asistente"]
# Variables


def validarVotacion():
    global lisPro
    if lisPro:
        for l in lisPro:
            print("valida votacion getActivo",l.getActivo)
            if l.getActivo:
                return abrirGenerar()
    return messagebox.showerror('No se puede realizar la accion', 'No hay candidatos inscritos en el sistema para '
                                                                  'generar la votacion')


def validarCandidato():
    global lisPro
    if not lisPro:
        return messagebox.showerror('No se puede realizar la accion', 'No hay profesores inscritos en el sistema para '
                                                               'registrar candidatos.')
    else:
        return abrirCandidato()


def rgb(rgb):
    return "#%02x%02x%02x" % rgb #devuelve el formato RBG para escoger los colores


def Xlimpiar():
    return ""

cont = 0

def registrarCan(cedula):
    global cont
    print(dicPer)
    profesor = Profesor
    if messagebox.askyesnocancel(message="¿Desea registrar este candidato?", title="Registrar Candidato"):
        for i in range(len(lisPro)):
            x = lisPro[i]
            print("cedulas encpontradas:",x.getCedula())
            if str(cedula) == str(x.getCedula()):
                print("Numero antes",lisPro[i].getCandidatoNum())
                print(lisPro[i].getActivo())
                lisPro[i].modActivo(True)
                print(lisPro[i].getActivo())
                lisPro[i].modNumCandidato(cont+1)
                cont+=1
                print("Numero despues",lisPro[i].getCandidatoNum())
                messagebox.showinfo(title="Exito", message="Se ha creado el candidato!")
                break
    messagebox.showerror(title="Error",message="No se ha encontrado esta cedula!")
    return cont


def abrirCandidato():
    vcandidato = tk.Toplevel()
    vcandidato.title("Registrar Candidato")
    # vcandidato.iconbitmap("icono2.ico")
    vcandidato.config(bg="#395b7f")
    vcandidato.geometry("375x550")
    vcandidato.resizable(0, 0)
    fcandidato = Frame(vcandidato, width=380, height=60, bg='#1f2e60')
    fcandidato.grid(row=0, column=0)
    imagen = PhotoImage(file='imagen.png')
    lImagen = Label(fcandidato, image=imagen, bd=0).place(x=133, y=-17)
    cedula = StringVar()
    textBoxCedula = Entry(vcandidato, bg=rgb((122, 255, 185)), textvariable=cedula)
    textBoxCedula.place(x=250, y=150)
    textBoxCedula.config(width='10', font=('Century gothic', 15), bd=5, relief='ridge')

    # Labels
    labelTitulo = Label(vcandidato, text='Ingrese la cédula', bd=0)
    labelTitulo.place(x=18, y=130)
    labelTitulo.config(bg='#395b7f', fg='#d1d3d4', cursor='hand2', font=('Century gothic', 12))


    labelTitulo = Label(vcandidato, text='Registrar Candidato', bd=0)
    labelTitulo.place(x=20, y=70)
    labelTitulo.config(bg='#395b7f', fg='#d1d3d4', cursor='hand2', font=('Century gothic', 17))

    # Botones
    botonLimpiar = Button(vcandidato, text='Limpiar', bg=rgb((122, 255, 185)), fg='Black', font=("Century ghotic", 15),
                          command=lambda: Xlimpiar())
    botonLimpiar.place(x=270, y=240)
    botonLimpiar.config(width="6", height="1", cursor='hand2')

    botonregistrar = Button(vcandidato, text='Registrar', bg=rgb((122, 255, 185)), fg='Black',
                            font=("Century ghotic", 15),
                            command=lambda: registrarCan(textBoxCedula.get()))
    botonregistrar.place(x=150, y=240)
    botonregistrar.config(width="6", height="1", cursor='hand2')

    vcandidato.mainloop()
    return ''


def auxRegistrar():
    if 3 >= typeObj.get() >= 1:
        if validarCNum(numCed.get(), 9):
            if validarLen(strNom.get(), 50):
                if validarCNum(numTel.get(), 8):
                    if typeObj.get() == 1:
                        if len(numCar.get()) > 0:
                            if typeCur.get() > 0:
                                if messagebox.askyesno('Confirmar', 'El miembro se va a registrar en el sistema.'
                                                                    ' ¿Desea continuar?'):
                                    return registrar()
                                else:
                                    return ''
                            return codERROR.set('Seleccione una carrera')
                        return codERROR.set('Ingrese un dato en el carnet')
                    elif typeObj.get() == 2:
                        global tpub
                        print(len(tpub.get('1.0', END)))
                        if len(tpub.get('1.0', END)) > 1:
                            if messagebox.askyesno('Confirmar', 'El miembro se va a registrar en el sistema. Desea continuar?'):
                                return registrar()
                            else:
                                return ''
                        return codERROR.set('Ingrese un dato en las publicaciones')
                    else:
                        if typePue.get() > 0:
                            if len(numExt.get()) > 0:
                                if messagebox.askyesno('Confirmar', 'El miembro se va a registrar en el sistema. Desea continuar?'):
                                    return registrar()
                                else:
                                    return ''
                            return codERROR.set('Ingrese un dato en la extension')
                        return codERROR.set('Seleccione un puesto')
                return codERROR.set('El numero de telefono debe ser de 8 NUMEROS')
            return codERROR.set('El nombre no debe sobrepasar los 50 digitos')
        return codERROR.set('La cedula debe ser de 9 NUMEROS')
    return codERROR.set('Seleccione el tipo de votante')


def registrar():
    ced = numCed.get()
    nom = strNom.get()
    tel = numTel.get()
    tip = typeObj.get()
    if tip == 1:
        carnet = numCar.get()
        carrera = typeCur.get()
        obj = Estudiante(carnet, carrera, ced, nom, tel)
        lisEst.append(obj)
    elif tip == 2:
        publi = str(tpub.get('1.0', END))
        obj = Profesor(publi, ced, nom, tel)
        print("nombre", obj.getNombre())
        print("cedula", obj.getCedula())
        print("telefono", obj.getTelefono())
        print("voto", obj.getVoto())
        print("publicaciones", obj.getPublicaciones())
        print("candidato", obj.getCandidato())
        print("activo", obj.getActivo())
        print("cantidad de votos", obj.getCanVotos())
        lisPro.append(obj)
    else:
        puesto = typePue.get()
        exten = numExt.get()
        obj = Administrativo(puesto, exten, ced, nom, tel)
        lisAdm.append(obj)
    ventana.withdraw()
    limpiar('')
    return print(dicPer)


def abrirMiembro():
    global numCar
    global ventana
    global numCed
    global typeObj
    global strNom
    global numTel
    global typeCur
    global numCar
    global typePue
    global numExt
    global codERROR
    global ventana
    global tret
    codERROR.set('')
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
    oest = Radiobutton(ventana, text='Estudiante', variable=typeObj, value=1, command=lambda: miembroEst())
    oest.config(bg='#395b7f', fg='#d1d3d4', font=('Helvetica', 11), cursor='hand2')
    oest.place(x=25, y=165)
    opro = Radiobutton(ventana, text='Profesor', variable=typeObj, value=2, command=lambda: miembroPro())
    opro.config(bg='#395b7f', fg='#d1d3d4', font=('Helvetica', 11), cursor='hand2')
    opro.place(x=25, y=195)
    oadm = Radiobutton(ventana, text='Administrativo', variable=typeObj, value=3, command=lambda: miembroAdm())
    oadm.config(bg='#395b7f', fg='#d1d3d4', font=('Helvetica', 11), cursor='hand2')
    oadm.place(x=25, y=225)
    ldis = Label(ventana, bd=0)
    ldis.config(width=54, height=13, bg='#395b7f')
    ldis.place(x=0, y=265)
    tret = Entry(ventana, bg='#395b7f', fg='red', bd=0, relief='flat', textvariable=codERROR)
    tret.config(width='36', font=('Helvetica', 11), cursor='arrow')
    tret.place(x=45, y=470)
    breg = Button(ventana, text='Registrar', bg='#d1d3d4', fg='#403f3d', font=('Helvetica', 11), command=auxRegistrar)
    breg.config(width="7", height="1", bd=3, relief='raised', cursor='hand2')
    breg.place(x=75, y=505)
    blim = Button(ventana, text='Limpiar', bg='#d1d3d4', fg='#403f3d', font=('Helvetica', 11), command=lambda: limpiar('y'))
    blim.config(width="7", height="1", bd=3, relief='raised', cursor='hand2')
    blim.place(x=225, y=505)
    ventana.mainloop()
    return ''


def limpiar(funcion):
    global numCar
    global ventana
    global numCed
    global typeObj
    global strNom
    global numTel
    global typeCur
    global numCar
    global typePue
    global numExt
    global codERROR
    global ventana
    typeObj.set(0)
    numCed.set('')
    strNom.set('')
    numTel.set('')
    typeCur.set(0)
    numCar.set('')
    typePue.set(0)
    numExt.set('')
    codERROR.set('')
    ventana.withdraw()
    if funcion != '':
        abrirMiembro()
    return ''


def miembroEst():
    global numCar
    global ventana
    global numCed
    global typeObj
    global strNom
    global numTel
    global typeCur
    global numCar
    global typePue
    global numExt
    global codERROR
    global ventana
    global tret
    codERROR.set('')
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
    tret = Entry(ventana, bg='#395b7f', fg='red', bd=0, relief='flat', textvariable=codERROR)
    tret.config(width='36', font=('Helvetica', 11), cursor='arrow')
    tret.place(x=45, y=470)
    breg = Button(ventana, text='Registrar', bg='#d1d3d4', fg='#403f3d', font=('Helvetica', 11), command=auxRegistrar)
    breg.config(width="7", height="1", bd=3, relief='raised', cursor='hand2')
    breg.place(x=75, y=505)
    blim = Button(ventana, text='Limpiar', bg='#d1d3d4', fg='#403f3d', font=('Helvetica', 11), command=lambda: limpiar('y'))
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
    global numCar
    global ventana
    global numCed
    global typeObj
    global strNom
    global numTel
    global typeCur
    global numCar
    global typePue
    global numExt
    global codERROR
    global tpub
    global ventana
    global tret
    codERROR.set('')
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
    tret = Entry(ventana, bg='#395b7f', fg='red', bd=0, relief='flat', textvariable=codERROR)
    tret.config(width='36', font=('Helvetica', 11), cursor='arrow')
    tret.place(x=45, y=470)
    breg = Button(ventana, text='Registrar', bg='#d1d3d4', fg='#403f3d', font=('Helvetica', 11), command=auxRegistrar)
    breg.config(width="7", height="1", bd=3, relief='raised', cursor='hand2')
    breg.place(x=75, y=505)
    blim = Button(ventana, text='Limpiar', bg='#d1d3d4', fg='#403f3d', font=('Helvetica', 11), command=lambda: limpiar('y'))
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
    global numCar
    global ventana
    global numCed
    global typeObj
    global strNom
    global numTel
    global typeCur
    global numCar
    global typePue
    global numExt
    global codERROR
    global ventana
    global tret
    codERROR.set('')
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
    tret = Entry(ventana, bg='#395b7f', fg='red', bd=0, relief='flat', textvariable=codERROR)
    tret.config(width='36', font=('Helvetica', 11), cursor='arrow')
    tret.place(x=45, y=470)
    breg = Button(ventana, text='Registrar', bg='#d1d3d4', fg='#403f3d', font=('Helvetica', 11), command=auxRegistrar)
    breg.config(width="7", height="1", bd=3, relief='raised', cursor='hand2')
    breg.place(x=75, y=505)
    blim = Button(ventana, text='Limpiar', bg='#d1d3d4', fg='#403f3d', font=('Helvetica', 11), command=lambda: limpiar('y'))
    blim.config(width="7", height="1", bd=3, relief='raised', cursor='hand2')
    blim.place(x=225, y=505)

    lpue = Label(ldis, text='Puesto: ',  bd=0)
    lpue.config(fg='#d1d3d4', bg='#395b7f', font=('Helvetica', 11))
    lpue.place(x=25, y=30)
    lext = Label(ldis, text='Extencion: ',  bd=0)
    lext.config(fg='#d1d3d4', bg='#395b7f', font=('Helvetica', 11))
    lext.place(x=25, y=70)
    text = Entry(ldis, bg='#d1d3d4', fg='#403f3d', bd=0, relief='flat', textvariable=numExt)
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
    ventana = tk.Toplevel()
    ventana.geometry("375x550+450+100")
    ventana.config(bg="#395b7f")
    ventana.title("Cargar datos")
    imagen = PhotoImage(file='imagen.png')
    lImagen = Label(ventana, image=imagen, bd=0).place(x=133, y=-17)
    cantidad = StringVar()
    texto = StringVar()

    # Label
    labelMensaje = Label(ventana, text='Ingrese la cantidad a crear', bd=0)
    labelMensaje.place(x=20, y=130)
    labelMensaje.config(bg='#395b7f', fg='#d1d3d4', cursor='hand2', font=('Century gothic', 12))

    labelTitulo = Label(ventana, text='Carga Automatica Aleatoria', bd=0)
    labelTitulo.place(x=20, y=70)
    labelTitulo.config(bg='#395b7f', fg='#d1d3d4', cursor='hand2', font=('Century gothic', 17))
    labelCantidad = Label(ventana, text="Cantidad a crear: ")

    # Textbox
    textboxTitulo = Entry(ventana, textvariable=cantidad)
    textboxTitulo.place(x=20, y=160)
    textboxTitulo.config(font=('Century gothic', 11), bd=5, relief='ridge')

    # botones
    botonCrear = Button(ventana, text='Crear', bg='#d1d3d4', fg='#403f3d', font=('Helvetica', 11),
                        command=lambda: crear(cantidad.get()))
    botonCrear.config(width="7", height="1", bd=3, relief='raised', cursor='hand2')
    botonCrear.place(x=25, y=230)
    botonLimpiar = Button(ventana, text='Limpiar', bg='#d1d3d4', fg='#403f3d', font=('Helvetica', 11),
                          command=lambda: dlimpiar())
    botonLimpiar.config(width="7", height="1", bd=3, relief='raised', cursor='hand2')
    botonLimpiar.place(x=120, y=230)

    # ejecución de ventana
    ventana.mainloop()


    return ''


def sacarVotantes():
    cont = 0
    for p in lisPro:
        if p.getActivo():
            cont+=1
    return cont


def votar():
    ncan = sacarVotantes()
    for t in dicPer:
        for p in dicPer[t]:
            voto = random.randint(0, ncan)
            p.modVoto(voto)
    return numAnno.set(0)


def auxVotar():
    if numAnno.get() >= 2017:
        if messagebox.askyesno('Confirmar', '¿Desea elegir un nuevo rector?'):
            return votar()
        return ''
    return messagebox.showerror('Falta Informacion', 'Porfavor seleccione un año e intentelo de nuevo')


def limpiarVotos():
    for t in dicPer:
        for p in dicPer[t]:
            p.modVoto(0)
            if isinstance(p, Profesor):
               p.resetCV()
    return auxVotar()


def contarVotos():
    for t in dicPer:
        for p in dicPer[t]:
            voto = p.getVoto()
            cod = str(numAnno) + '-' + str(voto)
            for c in lisPro:
                if c.getCandidato() == cod:
                    c.sumCantVotos()
                    break
    return ''



def contarVotos2():
    contX =0
    for i in dicPer["Pro"]:
        if i.getActivo():
            contX +=1

    for i in dicPer["Est"]:
        num = random.randint(0,contX)
        i.modVoto= num
    for i in dicPer["Pro"]:
        num = random.randint(0, contX)
        i.modVoto = num
    for i in dicPer["Adm"]:
        num = random.randint(0, contX)
        i.modVoto = num

    for i in dicPer["Est"]:
        for j in dicPer["Pro"]:
            if i.getVoto() == int(j.getCandidatoNum()[-1]):
                j.modCantidadVotos(j.getCanVotos()+1)
    for i in dicPer["Pro"]:
        for j in dicPer["Pro"]:
            if i.getVoto() == int(j.getCandidatoNum()[-1]):
                j.modCantidadVotos(j.getCanVotos()+1)
    for i in dicPer["Adm"]:
        for j in dicPer["Pro"]:
            if i.getVoto() == int(j.getCandidatoNum()[-1]):
                j.modCantidadVotos(j.getCanVotos()+1)


def abrirGenerar():
    ventana = tk.Toplevel()
    ventana.title("Registrar MiembroAAAA")
    ventana.iconbitmap("icono2.ico")
    ventana.config(bg="#395b7f")
    ventana.geometry("375x250")
    ventana.resizable(0, 0)
    frame = Frame(ventana, width=380, height=60, bg='#1f2e60')
    frame.grid(row=0, column=0)
    imagen = PhotoImage(file='imagen.png')
    lImagen = Label(frame, image=imagen, bd=0).place(x=133, y=-17)

    lanno = Label(ventana, text='Indicar año: ',  bd=0)
    lanno.config(fg='#d1d3d4', bg='#395b7f', font=('Helvetica', 11))
    lanno.place(x=67, y=95)
    bele = Button(ventana, text='Elegir', bg='#d1d3d4', fg='#403f3d', font=('Helvetica', 11), command=lambda: auxVotar())
    bele.config(width="7", height="1", bd=3, relief='raised', cursor='hand2')
    bele.place(x=75, y=185)
    breg = Button(ventana, text='Regresar', bg='#d1d3d4', fg='#403f3d', font=('Helvetica', 11), command=lambda: ventana.withdraw())
    breg.config(width="7", height="1", bd=3, relief='raised', cursor='hand2')
    breg.place(x=225, y=185)

    manno = Menubutton(ventana, text='Seleccione un año')
    manno.menu = Menu(manno, tearoff=0)
    manno["menu"] = manno.menu
    manno.config(bg='#d1d3d4', fg='#403f3d', cursor='hand2', font=('Helvetica', 9))

    manno.menu.add_radiobutton(label='2017', variable=numAnno, value=2017)
    manno.menu.add_radiobutton(label='2018', variable=numAnno, value=2018)
    manno.menu.add_radiobutton(label='2019', variable=numAnno, value=2019)
    manno.menu.add_radiobutton(label='2020', variable=numAnno, value=2020)
    manno.menu.add_radiobutton(label='2021', variable=numAnno, value=2021)

    manno.place(x=157, y=95)

    ventana.mainloop()

    return ''


def abrirReportes():
    raiz.title("Reportes Elecciones TEC")
    raiz.iconbitmap("icono2.ico")
    raiz.config(bg="#395b7f")
    raiz.geometry("375x550")
    raiz.resizable(0, 0)
    frameLogo = Frame(raiz, width=380, height=60, bg='#1f2e60')
    frameLogo.grid(row=0, column=0)
    imagen = PhotoImage(file='imagen.png')
    icoCan = PhotoImage(file='reportes2.png')
    icoGen = PhotoImage(file='reporte4.png')
    icoCar = PhotoImage(file='reporte3.png')
    icoRep = PhotoImage(file='reporte5.png')
    lImagen = Label(frameLogo, image=imagen, bd=0).place(x=133, y=-17)
    botMiembro = Button(raiz, image=icoCan, bg='#395b7f', bd=0, command=lambda: crearReporteCandidatos())
    botMiembro.config(cursor='hand2')
    botMiembro.place(x=55, y=100)
    botCandidato = Button(raiz, image=icoCan, bg='#395b7f', bd=0, command=lambda: crearReporteCantidadxVotante())
    botCandidato.config(cursor='hand2')
    botCandidato.place(x=220, y=100)
    botCargar = Button(raiz, image=icoCar, bg='#395b7f', bd=0, command=lambda: reporteCandidatoIndividual())
    botCargar.config(cursor='hand2')
    botCargar.place(x=55, y=250)
    botGenerar = Button(raiz, image=icoGen, bg='#395b7f', bd=0, command=lambda: abrirGenerar())
    botGenerar.config(cursor='hand2')
    botGenerar.place(x=220, y=250)
    botRegistro = Button(raiz, image=icoRep, bg='#395b7f', bd=0, command=lambda: crearReporteNoVotantes())
    botRegistro.config(cursor='hand2')
    botRegistro.place(x=138, y=400)
    texMiembro = Label(raiz, text='Candidatos para Rector', bd=0)
    texMiembro.place(x=55, y=200)
    texMiembro.config(bg='#395b7f', fg='#d1d3d4', cursor='hand2',)
    texCandidato = Label(raiz, text='Cantidad de votantes', bd=0)
    texCandidato.place(x=220, y=200)
    texCandidato.config(bg='#395b7f', fg='#d1d3d4', cursor='hand2', )
    texCargar = Label(raiz, text='Seguidores por candidato', bd=0)
    texCargar.place(x=55, y=350)
    texCargar.config(bg='#395b7f', fg='#d1d3d4', cursor='hand2', )
    texGenerar = Label(raiz, text='Votantes por rol', bd=0)
    texGenerar.place(x=220, y=350)
    texGenerar.config(bg='#395b7f', fg='#d1d3d4', cursor='hand2', )
    texRegistro = Label(raiz, text='No votantes', bd=0)
    texRegistro.place(x=138, y=500)
    texRegistro.config(bg='#395b7f', fg='#d1d3d4', cursor='hand2', )
    raiz.mainloop()


# Creación de GUI
# fondo -> (#395b7f) | imgTEC -> (#1f2e60) | iconos -> (#d1d3d4) | cuadros -> (#f2f2f4) | texto -> (#d1d3d4)
raiz = Tk()

typeObj = IntVar()
numCed = StringVar()
strNom = StringVar()
numTel = StringVar()
typeCur = IntVar()
numCar = StringVar()
typePue = IntVar()
numExt = StringVar()
codERROR = StringVar()
numAnno = IntVar()

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
botMiembro = Button(raiz, image=icoCan, bg='#395b7f', bd=0, command=lambda: abrirMiembro())
botMiembro.config(cursor='hand2')
botMiembro.place(x=55, y=100)
botCandidato = Button(raiz, image=icoCan, bg='#395b7f', bd=0, command=lambda: validarCandidato())
botCandidato.config(cursor='hand2')
botCandidato.place(x=220, y=100)
botCargar = Button(raiz, image=icoCar, bg='#395b7f', bd=0, command=lambda: abrirCargar())
botCargar.config(cursor='hand2')
botCargar.place(x=55, y=250)
botGenerar = Button(raiz, image=icoGen, bg='#395b7f', bd=0, command=lambda: abrirGenerar())
botGenerar.config(cursor='hand2')
botGenerar.place(x=220, y=250)
botRegistro = Button(raiz, image=icoRep, bg='#395b7f', bd=0, command=lambda: validarReporte())
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

# - FIN - #
#####  #####  #####  #   #   ##    #######
#        #    #      #   #   # #  #       #
###      #    #####  #####   #  ##         #
#        #        #  #   #   # #  #       #
#      #####  #####  #   #   ##    #######
