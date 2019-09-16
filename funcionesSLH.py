##############################################
# Creadores: Sebastián López y Daniel Sequeira
# Creado el: 26/05/19 22:30
# Ult. Actualización: 17/06/19 19:40
# Version 1.8.0 Python 3.7.3
##############################################
# Importación de Librerias


# Variables Globales
lisEst = []
lisPro = []
lisAdm = []
dicPer = {'Est': lisEst, 'Pro': lisPro, 'Adm': lisAdm}


# Definición de Funciones
class Persona:

    def __init__(self, cd, nm, tl, vt=0):
        self.cedula = cd
        self.nombre = nm
        self.telefono = tl
        self.voto = vt

    def modVoto(self, vt):
        self.voto = vt

    def getCedula(self):
        return self.cedula

    def getNombre(self):
        return self.nombre

    def getTelefono(self):
        return self.telefono

    def getVoto(self):
        return self.voto

    def getTodo(self):
        return self.cedula, self.nombre, self.telefono, self.voto


class Estudiante(Persona):

    def __init__(self, cn, cr, cd, nm, tl, vt=0):
        self.carnet = cn
        self.carrera = cr
        Persona.__init__(self, cd, nm, tl, vt)

    def modCarnet(self, cn):
        self.carnet = cn

    def modCarrera(self, cr):
        self.carrera = cr

    def getCarnet(self):
        return self.carnet

    def getCarrera(self):
        return self.carrera

    def getTodo(self):
        datos = []
        datos.append(Estudiante.getCarnet(self))
        datos.append(Estudiante.getCarrera(self))
        persona = Persona.getTodo(self)
        for p in persona:
            datos.append(p)
        return datos


class Profesor(Persona):

    def __init__(self, pb, cd, nm, tl, vt=0, cn='2019-0', ac=False, cv=0):
        self.publicaciones = pb
        self.candidato = cn
        self.activo = ac
        self.cantidadvotos = cv
        Persona.__init__(self, cd, nm, tl, vt)

    def modPublicaciones(self, pb):
        self.publicaciones = pb

    def modCandidato(self, cn):
        self.candidato = cn

    def modNumCandidato(self, cn):
        self.candidato = "2019-"+str(cn)

    def modActivo(self, ac):
        self.activo = ac

    def modCantidadVotos(self,num):
        self.cantidadvotos = num

    def setCandidato(self):
        self.candidato = True

    def sumCantVotos(self):
        cv = Profesor.getCanVotos(self)
        cv += 1
        self.cantidadvotos = cv
        return cv

    def getCandidatoNum(self):
        return self.candidato

    def resetCV(self):
        self.cantidadvotos = 0

    def getPublicaciones(self):
        return self.publicaciones

    def getCandidato(self):
        return self.candidato

    def getActivo(self):
        return self.activo

    def getCanVotos(self):
        return self.cantidadvotos

    def getTodos(self):
        datos = []
        datos.append(Profesor.getPublicaciones(self))
        datos.append(Profesor.getCandidato(self))
        datos.append(Profesor.getActivo(self))
        persona = Persona.getTodo(self)
        for p in persona:
            datos.append(p)
        return datos


class Administrativo(Persona):

    def __init__(self, ps, ex, cd, nm, tl, vt=0):
        self.puesto = ps
        self.extension = ex
        Persona.__init__(self, cd, nm, tl, vt)

    def modPuesto(self, ps):
        self.puesto = ps

    def modExtension(self, ex):
        self.extension = ex

    def getPuesto(self):
        return self.puesto

    def getExtension(self):
        return self.extension

    def getTodo(self):
        datos = []
        datos.append(Administrativo.getPuesto(self))
        datos.append(Administrativo.getExtension(self))
        persona = Persona.getTodo(self)
        for p in persona:
            datos.append(p)
        return datos


def validarCNum(pnum, pcan):
    """
    Funcion: Valida si el dato ingresado es un numero con len segun lo pedido
    Entradas: `pnum`(str) y `pcan`(int) valor a analizar
    Salida:  Booleano True/False segun las especificaciones
    """
    try:
        pnum = abs(int(pnum))
        if len(str(pnum)) == pcan:
            return True
        return False
    except ValueError:
        return False


def validarLen(ptext, plen):
    """
    Funcion: Valida que el len de un texto sea menor a un numero especifico
    Entradas: `ptext`(str) y `plen`(int) valores analizar
    Salida: Booleano True/False segun las especificaciones
    """
    if isinstance(ptext, str):
        if len(ptext) <= plen:
            return True
    return False


# - FIN - #
#####  #####  #####  #   #   ##    #######
#        #    #      #   #   # #  #       #
###      #    #####  #####   #  ##         #
#        #        #  #   #   # #  #       #
#      #####  #####  #   #   ##    #######
