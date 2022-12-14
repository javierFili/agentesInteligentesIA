import numpy as np


class Director:
  def getEstado(self):
    return self.estado

  def __init__(self):
    self.estado = True
    self.tiempoTotal = 0
    self.listaMateriasCod = []

  def registrarMatricula(self, est):
    tiempoEmpleado = np.random.rand(1) * 10
    tiempoEmpleado = tiempoEmpleado.astype(np.uint8)
    if (est > 0):
      return True, tiempoEmpleado
    else:
      return False, tiempoEmpleado

  def registrarMaterias(self, est):
    tiempoEmpleado = np.random.rand(1) * 10
    tiempoEmpleado = tiempoEmpleado.astype(np.uint8)
    if (est[0] > 0):
      tupla = (est[0], est[1])
      self.listaMateriasCod.append(tupla)
      return True, tiempoEmpleado
    else:
      return False, tiempoEmpleado

  def entregarListaCodigosMaterias(self):
    return self.listaMateriasCod

  def irCasa(self):
    self.estado = "inactivo"
