from funcionesSLH import *
import CrearPersonas as personas
import tkinter as tk
from tkinter import *
from tkinter import Tk
from tkinter import ttk
from tkinter import messagebox
import funcionesSLH as clase
import webbrowser

# Definición de Funciones
def rgb(rgb):
    return "#%02x%02x%02x" % rgb #devuelve el formato RBG para escoger los colores

def reporteCandidatos():
    webbrowser.open("ReporteCan.html")


#raiz
raiz = Tk()
raiz.title("Elecciones TEC")
raiz.geometry("500x500+500+0")
raiz.config(bg="#395b7f")

#Variables
cedula = StringVar()


labelTitulo = Label(raiz,text="Ver Reportes")
labelTitulo.place(x=170, y=50)
labelTitulo.config(font=('Century gothic', 12), bd=5)



#Botones
botonCandidatos= Button(raiz, text='Ver Candidatos', bg=rgb((122, 255, 185)), fg='Black',font=("Century ghotic",15), command=lambda:reporteCandidatos())
botonCandidatos.place(x=270, y=240)
botonCandidatos.config( height = "1", cursor='hand2')

botonregistrar= Button(raiz, text='Registrar', bg=rgb((122, 255, 185)), fg='Black',font=("Century ghotic",15), command=lambda:personas.ventana.mainloop())
botonregistrar.place(x=150, y=240)
botonregistrar.config(width="6", height = "1", cursor='hand2')


# Programa principal
raiz.mainloop()
