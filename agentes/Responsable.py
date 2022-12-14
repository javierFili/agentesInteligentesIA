class Responsable:
  def __init__(self):
    self.listasMaterias = []
    self.materiasHabilitadas = []
    self.estudianteHabilitados = []

  def registrarCodigosMaterias(self, lista):
    self.listasMaterias.append(lista)

  def habilitarMaterias(self, minimo, maximo):
    for x in self.listasMaterias:
      self.materiasHabilitadas.append(x[0][1])
      self.estudianteHabilitados.append(x[0][0])
