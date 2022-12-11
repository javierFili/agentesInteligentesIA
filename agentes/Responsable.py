class Responsable:
    dinero = 10
    tiempo = 12

    estado = 'inactivo'

    def getEstado(self):
        return  self.estado

    def __init__(self):
        self.dinero = 12
        self.tiempo = 122

    def aunTieneDinero(self):
        return self.dinero
