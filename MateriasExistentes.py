class MateriasExistentes:
  def __init__(self):
    self.materias = [
        "Sistemas y Métodos"
      , "Análisis Matemático I"
      , "Sistemas Digitales I"
      , "Introducción a la Programación"
      , "Derecho Aplicado a la Informática"
      , "Álgebra"
      , "Análisis Matemático II"
      , "Arquitectura de Computadores"
      ,"Base de Datos"
      , "Estructura de Datos y Algoritmos"
      , "Introducción a la Ingeniería del Software"
      , "Introducción a las Comunicaciones"
      , "Sistemas Operativos"
      , "Laboratorio I"
      , "Análisis de Sistemas"
      , "Probabilidad y Estadística"
      , "Laboratorio II"
      , "Álgebra Lineal"
      , "Diseño de Sistemas"
      , "Física I"]

  # solo tenemos 8 materias ojo!
  def getMateria(self, pos):
    return self.materias[pos]
