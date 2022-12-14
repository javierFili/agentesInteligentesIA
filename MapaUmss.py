import numpy as np


class MapaUmss:
  def __init__(self):
    self.matriz = np.zeros((10, 10))

  def setPosEstudiante(self, fila, colum):
    self.matriz[colum][fila] = 1

  def setPosOficinasMatriculas(self, fila, colum):
    self.matriz[colum][fila] = 2
    return "oficina ingresada"

  def setPosOficinaDirector(self, fila, colum):
    self.matriz[colum][fila] = 3
    return "aqui esta"

  def setPosOficinaResponsable(self, fila, colum):
    self.matriz[colum][fila] = 4
