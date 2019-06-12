from funcionesSLH import *
from CrearPersonas import *
import tkinter as tk
from tkinter import *
from tkinter import Tk
from tkinter import ttk
from tkinter import messagebox
import funcionesSLH as clase

def crearReporte(num):
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
                                                                                  <body>  \
<div class="limiter"><div class="container-table100"><div class="wrap-table100"> <div class="table100 ver1 m-b-110"> <div class="table100-head"><table><thead><tr class="row100 head"><th class="cell100 column1">Cedula</th><th class="cell100 column2">Nombre</th><th class="cell100 column3">Telefono</th><th class="cell100 column4">Publicaciones</th></tr></thead></table></div>'
    cuerpo = ""
    for  i in dicPer["Pro"]:
        cuerpo = cuerpo + '<div class="table100-body js-pscroll"> \
              <table> \
              <tbody> \
              <tr class="row100 body"> \
              <td class="cell100 column1">'+str(+i.getCedula())+'</td> \
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
    print("si")

crearReporte(3)