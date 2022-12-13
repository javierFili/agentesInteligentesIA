from MapaUmss import MapaUmss
from agentes.Cajero import Cajero
from agentes.Director import Director
from agentes.Estudiante import Estudiante
from agentes.Responsable import Responsable

if __name__ == '__main__':
  mapa = MapaUmss()
  mapa.setPosEstudiante(0, 4)
  mapa.setPosOficinasMatriculas(4, 0)
  mapa.setPosCajero(8, 4)
  mapa.setPosResponsable(4, 8)

  est = Estudiante()
  dir = Director()
  caj = Cajero()
  res = Responsable()


