import numpy as np


class MapaUmss:
    colum = 9
    fila = 9

    def __init__(self):
        self.colm = 9
        self.fila = 9
        self.matriz = np.zeros((9, 9))
    
    def setPosEstudiante(self, fila, colum):
        self.matriz[colum][fila] = 1

    def setPosOficinas(self, fila, colum):
        self.matriz[colum][fila] = 2
        return "oficina ingresada"

    def setPosCajero(self, fila, colum):
        self.matriz[colum][fila] = 3
        return "aqui esta"

    def setPosResponsable(self, fila, colum):
        self.matriz[colum][fila] = 4