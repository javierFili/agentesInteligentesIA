import numpy as np


class MapaUmss:
    colum = 10
    fila = 10

    def __init__(self):
        self.colm = 10
        self.fila = 10
        self.matriz = np.zeros((10, 10))

    def ingresarPosOficinas(self, fila, colum):
        self.matriz[fila][colum] = 2;
        return "oficina ingresada"

    def mostrarOfCobro(self, fila, colum):
        self.matriz[colum][fila] = 3
        return "aqui esta"
