###############################
# Creadores: Sebastián López y Daniel Sequeira
# Creado el: 27/05/19 01:50
# Ult. Actualización: 27/05/19 01:50
# Version 0.1.0 Python 3.7.3
###############################


# Importación de Librerias
from tkinter import *
import random
import pickle

# Definición de Funciones

listaPadron = []
def crear():
    pcantidad = int(cantidad.get())

    texto.set("Se han creado las personas")
    try:

        print(pcantidad)
        if pcantidad > 100 or pcantidad < 1:
            texto.set("Debe ser un numero entre 1 y 100")
        else:
            for i in range(pcantidad):
                listaPadron.append(listaNombres[random.randint(0, len(listaNombres) - 1)] + " " +listaApellidos[
                    random.randint(0, len(listaApellidos) - 1)] + " " + listaApellidos[
                                       random.randint(0, len(listaApellidos) - 1)])
                print(listaPadron[i])
            with open('listaPadron.txt', 'wb') as filehandle:
                # store the data as binary data stream
                pickle.dump(listaPadron, filehandle)

    except:
        texto.set("Debe ser un NUMERO entre 1 y 100")


def limpiar():
    textboxTitulo.delete(0, END) # limpia el textbox
    texto.set("") # limpia el label



# Instancia de la clase Tk
ventana = Tk()
ventana.geometry("470x200+450+100")
ventana.title("Cargar datos")

# Variables
cantidad = StringVar()
texto = StringVar()
listaNombres = ["Daniel", "Sebastian", "Jan", "Jafet", "Ariel", "Hillary",
                "Paula", "Sofia", "Muffin", "Maria", "Sylvia", "Giovanna", "Gimena",
                "Thanos", "Alex", "Kenneth", "Diego", "Erick", "Bartolomé", "Anastacio",
                "Isidro", "Benito", "Batman", "Yolanda", "Sacarías", "Armando", "Susana",
                "Yoda", "Jotaro", "Jospeh", "Jonathan", "Giorno", "Dio", "Goku", "Abbacchio",
                "Speed", "Apellidon't", "Bucciarati", "Polnareff", "Abdol", "Caesar",
                "Josuke", "Narancia", "Mista", "Iggy", "Aqua"]

listaApellidos = ["Joestar", "Horia", "Piedras", "Rios", "Sequeira", "Gómez", "Jupas", "XVII",
                  "ACDC", "Parada", "Wagon", "Snow", "Sama", "Kujo", "Retana", "Lopez", "Sparrow",
                  "Stark", "Rogers", "Balboa", "Schwarzenegger", "3000", "Camelas", "Del Rio",
                  "De Luz del Topo", "Joestar", "Jr", "Pool", "Gatjens", "SantaMaria", "Casas",
                  "Moffin", "Ghost", "Java", "C++", "Pokemon", "Nombren't","Joestar", "BadBunny",
                  "Yu-Gi-Oh", "Miyamoto", "MarioBros", "Abalahama", "Danvers", "Odinson", "404NotFound"]

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
# ║        a 100 porfis ☻ ║    /)_(\
# ║                        ║    (o o)
# ║ -Daniel & CO           ║     \o/\__-----.
# ╚════════════════════════╝      \      __  \
#            ║ ║                   \| /_/  \ /\__/
#            ║ ║                    ||      \\
#            ║ ║                    ||      //
#            ║ ║                    /|     /|
# ═════════════════════════════════════════════════════
