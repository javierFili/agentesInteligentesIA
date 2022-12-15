import numpy as np
from MapaUmss import MapaUmss
from agentes.Estudiante import Estudiante
from MateriasExistentes import MateriasExistentes
import string
import random

if __name__ == '__main__':
  # mapa = MapaUmss()
  # mapa.setPosEstudiante(0, 4)
  # mapa.setPosOficinasMatriculas(4, 0)
  # mapa.setPosCajero(8, 4)
  # mapa.setPosResponsable(4, 8)
  # print(mapa.matriz)
  # valor = np.where(mapa.matriz == 4)
  # x = valor[0]
  # y = valor[1]
  # print(mapa.matriz[x, y], x, y)
  #
  # vectorD = np.random.rand(4) * 10
  # vectorD = vectorD.astype(np.uint8)
  #
  # list = [23, 'asd', True]
  # try:
  #   if (list.index(23) != -1):
  #     print("entra",list.index(True))
  # except:
  #   print("no entra")
  #
  #
  #
  # print(vectorD)
  # b = []
  # a = (3, 4)
  # d = (2, [1, 3, 2, 3])
  # b.append(a)
  # b.append(d)
  # print(b)
  estudiantes = []
  n = 10
  matExistentes = MateriasExistentes()
  while (n > 0):
    n = n - 1
    est = Estudiante("Ing.Sistemas", n)
    vectorD = np.random.rand(1) * 20
    vectorD = vectorD.astype(np.uint8)
    est.setDinero(vectorD)
    m = 5
    while (m > 0):
      nroMateria = np.random.rand(1) * 20
      nroMateria = nroMateria.astype(np.uint8)
      materia = matExistentes.getMateria(nroMateria[0])
      print(materia)
      try:
        est.materias.index(materia)
      except:
        est.materias.append(materia)
        m = m - 1
    estudiantes.append(est)
    print(vectorD)
  print(estudiantes)
  # seria interesante tener una lista de muchas materias y que esas materias se eligan de manera aleatoria.
  # number_of_strings = 5
  # length_of_string = 8
  # for x in range(number_of_strings):
  #   print(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)))
