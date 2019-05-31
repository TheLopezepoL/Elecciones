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

