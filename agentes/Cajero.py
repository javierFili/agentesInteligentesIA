class Cajero:
    dinero = 10
    tiempo = 12
    estado = 'inactivo'
    costo = 5

    def getEstado(self):
        return  self.estado

    def setEstado(self, num):
        if num == 1:
            self.estado = 'inactivo'
        elif num == 2:
            self.estado = 'Cobrando matricula'
        else:
            return None

    def getCosto(self):
        return  self.costo

    def __init__(self):
        self.dinero = 12
        self.tiempo = 122

    def aunTieneDinero(self):
        return self.dinero

