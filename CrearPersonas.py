###############################
# Creadores: Sebastián López y Daniel Sequeira
# Creado el: 27/05/19 01:50
# Ult. Actualización: 27/05/19 01:50
# Version 0.1.0 Python 3.7.3
###############################


# Importación de Librerias
from tkinter import *
import funcionesSLH as clase
import random
import ast
import json



anio = 20190000
# Definición de Funciones
#<>
nombres = []
def crear():

    #print(clase.dicPer['Est'])
    pcantidad = int(cantidad.get())
    texto.set("Se han creado las personas")
    #try:
    print("cantidad a crear:", pcantidad)
    if pcantidad > 100 or pcantidad < 1:
        texto.set("Debe ser un numero entre 1 y 100")
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
                objeto = clase.Administrativo(listaPuestos[random.randint(0,len(listaPuestos)-1)],random.randint(1100,9999) , cedula,nombres[i], telefono,0)

                clase.lisAdm.append(objeto)
            elif azar < 20:
                objeto = clase.Estudiante(anio + random.randint(1, 9999),listaCarreras[random.randint(0,len(listaCarreras)-1)], cedula, nombres[i],telefono,0)

                clase.lisEst.append(objeto)
            else:
                objeto = clase.Profesor(1, False, cedula, nombres[i], telefono, 0, True)
                print("Cedula de un profesor:",cedula)
                clase.lisPro.append(objeto)


    #except:
        texto.set("Debe ser un NUMERO entre 1 y 100")
    escribir()

def escribir():

    f = open("file.txt", "w")
    f.write(str(clase.dicPer))
    #pickle.dump(clase.dicPer, f)
    f.close()
    print("Termino")
    print(clase.dicPer)
def leer():
    print(clase.dicPer['Est'])
    f = open("file.txt","r")
    clase.dicPer = ast.literal_eval(f.read())
    print(clase.dicPer['Est'])
    f.close()

def limpiar():
    textboxTitulo.delete(0, END) # limpia el textbox
    texto.set("") # limpia el label


"""
# Instancia de la clase Tk
ventana = Tk()
ventana.geometry("470x200+450+100")
ventana.title("Cargar datos")

# Variables
cantidad = StringVar()
texto = StringVar()
listaCarreras = ["Computacion", "Computadores", "Mecatronica", "Ambiental", "Ingenieria de la Republica independiente de Forestal",
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
                  "Moffin", "Ghost", "Java", "C++", "Pokemon", "Nombren't","Joestar", "BadBunny",
                  "Yu-Gi-Oh", "Miyamoto", "MarioBros", "Abalahama", "Danvers", "Odinson", "404NotFound"]
listaPuestos= ["Auxiliar", "Coordinador","Secretarix", "Interino","Administrador","Asistente"]
# Label

labelTitulo = Label(ventana, text="Carga Automatica Aleatoria")
labelTitulo.grid(row=1, column=1)
labelCantidad = Label(ventana, text="Cantidad a crear: ")
labelValidacion = Label(ventana, text="",textvariable=texto)
labelValidacion.grid(row=70, column=1)
# Textbox
textboxTitulo = Entry(ventana, textvariable=cantidad)
textboxTitulo.grid(row=2,column=2)

# botones
botonCrear = Button(ventana, text='Crear', command=crear, width=15)
botonCrear.grid(row=30, column=1)
botonLimpiar = Button(ventana, text='Limpiar', command=limpiar, width=15)
botonLimpiar.grid(row=30, column=2)

# ejecución de ventana
ventana.mainloop()

#            ╔═╗
# ╔════════════════════════╗
# ║ Can I get some uhhh... ║
# ║        a 100 porfis ☻  ║    /)_(\
# ║                        ║    (o o)
# ║ -Daniel & CO           ║     \o/\__-----.
# ╚════════════════════════╝      \      __  \
#            ║ ║                   \| /_/  \ /\__/
#            ║ ║                    ||      \\
#            ║ ║                    ||      //
#            ║ ║                    /|     /|
# ═════════════════════════════════════════════════════
"""
