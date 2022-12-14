import numpy as np


class Cajero:
  def getEstado(self):
    return self.estado

  def setEstado(self, num):
    if num == 1:
      self.estado = 'inactivo'
    elif num == 2:
      self.estado = 'Cobrando matricula'
    else:
      return None

  def getCosto(self):
    return self.costo

  def __init__(self):
    self.estado = 'inactivo'
    self.dineroRecaudado = 0
    self.tiempo = 122
    self.cobro = False
    self.registro = []
    self.costo = 14

  def cobrarMatricula(self, codEstudiante):
    tiempoEmpleado = np.random.rand(1) * 10
    tiempoEmpleado = tiempoEmpleado.astype(np.uint8)
    # el tiempo empleado en realizar el cobro.
    try:
      # verificamos que el estudiante no haya sido previamente registrado
      estaraRegistrado = self.registro.index(codEstudiante)
      return False, tiempoEmpleado

    except:
      self.registro.append(codEstudiante)
      print("Registro de est:", self.registro)
      return True, tiempoEmpleado

  def darMatricula(self, estudiante):
    return estudiante.setCodigoMatricula(1231)
