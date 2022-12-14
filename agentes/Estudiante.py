class Estudiante:
  def __init__(self, carrera):
    self.dinero = 20
    self.tiempoEmpleado = 0
    self.materias = ["calculo", "algebra", "Ingles", "Programacion1"]
    self.estado = 'inactivo'
    self.carrera = carrera
    self.codEstudiante = 12
    self.codMatricula = 0

  def getCarrera(self):
    return self.carrera

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

  def irCasa(self):
    self.estado = "inactivo "
  def mostrarMatricula(self):
    return self.codMatricula

  def darListaMaterias(self):
    return self.codEstudiante, self.materias

  def setTiempoEmpleado(self, tiempo):
    self.tiempoEmpleado = self.tiempoEmpleado + tiempo

  def setCodigoMatricula(self, cod):
    self.codMatricula = cod
