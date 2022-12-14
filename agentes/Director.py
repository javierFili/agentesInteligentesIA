import numpy as np


class Director:
  def getEstado(self):
    return self.estado

  def __init__(self):
    self.estado = 'inactivo'
    self.listaMateriasCod = []

  def aunTieneDinero(self):
    return self.dinero

  def registrarMatricula(self, est):
    tiempoEmpleado = np.random.rand(1) * 10
    tiempoEmpleado = tiempoEmpleado.astype(np.uint8)
    if (est[0] > 0):
      tupla = (est[0], est[2])
      self.listaMateriasCod.append(tupla)
      return True, tiempoEmpleado
    else:
      return False, tiempoEmpleado

  def registrarMaterias(self, est):
    return "regitrados"

  def entregarListaCodigosMaterias(self, responsable):
    return "entragado"
