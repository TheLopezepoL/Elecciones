###############################
# Creadores: Sebastián López y Daniel Sequeira
# Creado el: 26/05/19 22:30
# Ult. Actualización: 27/05/19 01:40
# Version 0.1.1 Python 3.7.3
###############################
# Importación de Librerias


# Variables Globales
lisEst = []
lisPro = []
lisAdm = []
dicPer = {'Est': lisEst, 'Pro': lisPro, 'Adm': lisAdm}

def hola():
    print("Error 404")
# Definición de Funciones
class Persona:


    def __init__(self, cd, nm, tl, vt=99):
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


    def __init__(self, cd, nm, tl, vt, carne, carrera):
        self.carnet = carne
        self.carrera = carrera

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



    def __init__(self, cd, nm, tl, vt, publi, candidato, activo):
        self.publicaciones = publi
        self.candidato = candidato
        self.activo = activo

    def __init__(self, pb, cn, cd, nm, tl, vt=0, ac=False):
        self.publicaciones = pb
        self.candidato = cn
        self.activo = ac
        Persona.__init__(self, cd, nm, tl, vt)

    def modPublicaciones(self, pb):
        self.publicaciones = pb

    def modCandidato(self, cn):
        self.candidato = cn

    def modActivo(self, ac):
        self.activo = ac

    def getPublicaciones(self):
        return self.publicaciones

    def getCandidato(self):
        return self.candidato

    def getActivo(self):
        return self.activo
    def getCedula(self):
        return self.cedula

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



    def __init__(self, cd, nm, tl, vt, puesto, extension):
        self.puesto = puesto
        self.extension = extension
    def __init__(self, ps, ex, cd, nm, tl, vt):
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
    try:
        pnum = abs(int(pnum))
        if len(str(pnum)) == pcan:
            return True
        return False
    except ValueError:
        return False


def validarVNum(pnum, pmen, pmay):
    try:
        pnum = int(pnum)
        if pmen <= pnum <= pmay:
            return True
    except ValueError:
        return False
    return False


def validarLen(ptext, plen):
    if isinstance(ptext, str):
        if len(ptext) == plen:
            return True
    return False


# - FIN - #
#####  #####  #####  #   #   ##    #######
#        #    #      #   #   # #  #       #
###      #    #####  #####   #  ##         #
#        #        #  #   #   # #  #       #
#      #####  #####  #   #   ##    #######
