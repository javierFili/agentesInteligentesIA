from MapaUmss import MapaUmss
from agentes.Cajero import Cajero
from agentes.Director import Director
from agentes.Estudiante import Estudiante
from agentes.Responsable import Responsable

if __name__ == '__main__':
    mapa = MapaUmss()
    mapa.ingresarPosOficinas(2, 3)
    mapa.mostrarOfCobro(3, 4)
    print(mapa.matriz)
    est = Estudiante()
    print(est.dinero)
