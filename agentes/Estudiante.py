class Estudiante:
    dinero = 10
    tiempo = 12
    materias = 6
    estado = 'inactivo'

    def __init__(self):
        self.dinero=12
        self.tiempo=122

    def getMaterias(self, pos):
        return  self.materias[pos]

    def getEstado(self):
        return  self.estado

    def aunTieneDinero(self):
        return  self.dinero
