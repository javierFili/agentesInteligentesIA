from MateriasExistentes import MateriasExistentes
import numpy as np


class Responsable:
  def __init__(self):
    self.listasMaterias = []
    self.materiasHabilitadas = []
    self.estudianteHabilitados = []
    mate = MateriasExistentes()
    self.materiasExistentes = mate.materias

  def registrarCodigosMaterias(self, lista):
    self.listasMaterias.append(lista)

  def habilitarMaterias(self, minimo):
    listaMateriasTotal = []
    listaEstudiantesTotal = []
    for x in self.listasMaterias[0]:
      materias = x[1]
      estudiantes = x[0]
      listaMateriasTotal.append(materias)
      listaEstudiantesTotal.append(estudiantes)
    self.estudianteHabilitados = listaEstudiantesTotal
    listaMateriasTotal = self.convertirArray(listaMateriasTotal)
    for matEvaluar in self.materiasExistentes:
      cuantasHay = listaMateriasTotal.count(matEvaluar)
      if (cuantasHay >= minimo):
        self.materiasHabilitadas.append(matEvaluar)

  def convertirArray(self, lista):
    res = []
    for x in range(len(lista)):
      for y in range(len(lista[0])):
        res.append(lista[x][y])
    return res
