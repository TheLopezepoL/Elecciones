###############################
# Creadores: Sebastián López y Daniel Sequeira
# Creado el: 26/05/19 22:30
# Ult. Actualización: 27/05/19 01:40
# Version 0.1.1 Python 3.7.3
###############################
# Importación de Librerias


# Definición de Funciones
class Persona:
    cedula = 0
    nombre = ''
    telefono = 0
    voto = 0

    def __init__(self, cd, nm, tl, vt):
        self.cedula = cd
        self.nombre = nm
        self.telefono = tl
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
    carnet = ''
    carrera = ''

    def __init__(self, cd, nm, tl, vt):
        self.carnet = ''
        self.carrera = ''
        Persona.__init__(self, cd, nm, tl, vt)

    def setCarnet(self, cn):
        self.carnet = cn

    def setCarrera(self, cr):
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
    publicaciones = ''
    candidato = ''

    def __init__(self, cd, nm, tl, vt):
        self.publicaciones = ''
        self.candidato = ''
        Persona.__init__(self, cd, nm, tl, vt)

    def setPublicaciones(self, pb):
        self.publicaciones = pb

    def setCandidato(self, cn):
        self.candidato = cn

    def getPublicaciones(self):
        return self.publicaciones

    def getCandidato(self):
        return self.candidato

    def getTodo(self):
        datos = []
        datos.append(Profesor.getPublicaciones(self))
        datos.append(Profesor.getCandidato(self))
        persona = Persona.getTodo(self)
        for p in persona:
            datos.append(p)
        return datos

class Administrativo(Persona):
    puesto = ''
    extension = ''

    def __init__(self, cd, nm, tl, vt):
        self.puesto = ''
        self.extension = ''
        Persona.__init__(self, cd, nm, tl, vt)

    def setPuesto(self, ps):
        self.puesto = ps

    def setExtension(self, ex):
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

# - FIN - #
#####  #####  #####  #   #   ##    #######
#        #    #      #   #   # #  #       #
###      #    #####  #####   #  ##         #
#        #        #  #   #   # #  #       #
#      #####  #####  #   #   ##    #######
