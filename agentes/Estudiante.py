class Estudiante:
  def __init__(self, carrera):
    self.dinero = 12
    self.tiempo = 122
    self.materias = 6
    self.estado = 'inactivo'
    self.carrera = carrera

  def getCarrera(self):
    return self.carrera

  def getMaterias(self):
    return self.materias

  def resMaterias(self):
    self.materias = self.materias - 1

  def getEstado(self):
    return self.estado

  def setEstado(self, num):
    if num == 1:
      self.estado = 'inactivo'
    elif num == 2:
      self.estado = 'Pagando matricula'
    else:
      return None

  def setDinero(self, dinero):
    self.dinero = dinero

  def getDinero(self):
    return self.dinero

  def pagar_a(self, cajero):
    res = False
    c = cajero
    if self.dinero >= c.getCosto():
      self.setDinero(self.getDinero() - c.getCosto())
      res = True
    return res

  def aunTieneDinero(self):
    return self.dinero
