class Estudiante:
  def __init__(self, carrera):
    self.dinero = 20
    self.tiempoEmpleado = 0
    self.materias = 6
    self.estado = 'inactivo'
    self.carrera = carrera
    self.codEstudiante = 12
    self.codMatricula = 0

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

  def pagarMatricula(self, cajero):
    res = False
    c = cajero
    if self.dinero >= c.getCosto():
      self.setDinero(self.getDinero() - c.getCosto())
      res = True
    return res

  def aunTieneDinero(self):
    return self.dinero

  def avanzarSigOf(self):
    return "avanzo"

  def mostrarMatricula(self):
    return self.codEstudiante, self.carrera, self.materias

  def setTiempoEmpleado(self, tiempo):
    self.tiempoEmpleado = self.tiempoEmpleado + tiempo

  def setCodigoMatricula(self, cod):
    self.codMatricula = cod
