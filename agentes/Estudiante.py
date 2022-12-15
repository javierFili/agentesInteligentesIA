class Estudiante:
  def __init__(self, carrera, cod):
    self.dinero = 20
    self.tiempoEmpleado = 0
    self.tiempoAsignado = 0
    self.materias = []
    self.estado = True
    self.carrera = carrera
    self.codEstudiante = cod
    self.codMatricula = 0

  def getCarrera(self):
    return self.carrera

  def setDinero(self, dinero):
    self.dinero = dinero

  def getDinero(self):
    return self.dinero

  def pagarMatricula(self, cajero):
    res = False
    c = cajero
    if self.dinero >= c.getCosto():
      self.setDinero(self.getDinero() - c.getCosto())
      res = True
    return res

  def irCasa(self):
    self.estado = False

  def mostrarMatricula(self):
    return self.codMatricula

  def darListaMaterias(self):
    return self.codEstudiante, self.materias

  def setTiempoEmpleado(self, tiempo):
    self.tiempoEmpleado = self.tiempoEmpleado + tiempo
    self.tiempoAsignado = self.tiempoAsignado - tiempo
    if (self.tiempoAsignado <= 0):
      self.estado = False

  def setTiempoAsignado(self, tiempo):
    self.tiempoAsignado = tiempo

  def setCodigoMatricula(self, cod):
    self.codMatricula = cod
