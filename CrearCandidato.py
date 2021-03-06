from funcionesSLH import *
from CrearPersonas import *
import tkinter as tk
from tkinter import *
from tkinter import Tk
from tkinter import ttk
from tkinter import messagebox
import funcionesSLH as clase


# Definición de Funciones
def rgb(rgb):
    return "#%02x%02x%02x" % rgb #devuelve el formato RBG para escoger los colores


def Xlimpiar():
    # todos los text box pasan a ser ""
    textBoxCedula.delete(0, END)
    textBoxCedula.insert(0, "")

def registrar(cedula):
    print(dicPer)
    profesor = clase.Profesor
    if messagebox.askyesnocancel(message="¿Desea registrar este candidato?", title="Registrar Candidato"):
        for i in range(len(clase.lisPro)-1):
            x = clase.lisPro[i]
            print("cedulas encpontradas:",x.getCedula())
            if str(cedula) == str(x.getCedula()):
                print(lisPro[i].getCandidato())
                clase,lisPro[i].modCandidato(True)
                print(lisPro[i].getCandidato())
                messagebox.showinfo(title="Exito", message="Se ha creado el candidato!")
                break
        messagebox.showerror(title="Error",message="No se ha encontrado esta cedula!")



#raiz
ventana = Tk()
ventana.title("Elecciones TEC")
ventana.geometry("500x500+500+0")
ventana.config(bg="#395b7f")

#Variables
cedula = StringVar()


# TextBox
textBoxCedula = Entry(raiz,bg=rgb((122, 255, 185)), textvariable=cedula)
textBoxCedula.place(x=250, y=150)
textBoxCedula.config(width='10', font=('Century gothic', 15), bd=5, relief='ridge')

#Labels
labelCedula = Label(raiz,text="Ingrese la cedula:")
labelCedula.place(x=50, y=150)
labelCedula.config(font=('Century gothic', 12), bd=5)

labelConfirmacion = Label(raiz,text=":)")
labelConfirmacion.place(x=50, y=350)
labelConfirmacion.config(font=('Century gothic', 12), bd=5)

labelTitulo = Label(raiz,text="Registar candidato")
labelTitulo.place(x=170, y=50)
labelTitulo.config(font=('Century gothic', 12), bd=5)



#Botones
botonLimpiar= Button(raiz, text='Limpiar', bg=rgb((122, 255, 185)), fg='Black',font=("Century ghotic",15), command=lambda:Xlimpiar())
botonLimpiar.place(x=270, y=240)
botonLimpiar.config(width="6", height = "1", cursor='hand2')

botonregistrar= Button(raiz, text='Registrar', bg=rgb((122, 255, 185)), fg='Black',font=("Century ghotic",15), command=lambda:registrar(textBoxCedula.get()))
botonregistrar.place(x=150, y=240)
botonregistrar.config(width="6", height = "1", cursor='hand2')


# Programa principal
raiz.mainloop()

