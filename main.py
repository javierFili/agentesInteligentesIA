import kivy.app
import kivy.uix.gridlayout
import kivy.uix.boxlayout
import kivy.uix.button
import kivy.uix.textinput
import kivy.uix.label
import numpy as np
from MapaUmss import MapaUmss
from agentes.Cajero import Cajero
from agentes.Director import Director
from agentes.Estudiante import Estudiante
from agentes.Responsable import Responsable
from MateriasExistentes import MateriasExistentes


class BuzzleApp(kivy.app.App):

  def ponerPosiciones(self, *args):
    limitX = self.mapa.matriz[0].size
    limitY = self.mapa.matriz[0].size
    print(self.mapa.matriz[0][4])
    for x in range(limitX):
      for y in range(limitY):
        if (self.mapa.matriz[x][y] == 1):
          self.all_widgets[x, y].text = "[color=FFFFF]Estudiante[/color]"
          self.all_widgets[x, y].background_normal = 'imagenes/estudiante.png'
          self.all_widgets[x, y].background_down = 'imagenes/estudiante.png'
          with self.all_widgets[x, y].canvas.before:
            kivy.graphics.Color(0, 1, 0, 1)  # green; colors range from 0-1 not 0-255
            self.rect = kivy.graphics.Rectangle(size=self.all_widgets[x, y].size,
                                                pos=self.all_widgets[x, y].pos)
        if (self.mapa.matriz[x][y] == 2):
          self.all_widgets[x, y].text = "[color=FFFFF]Oficina[/color]"
          self.all_widgets[x, y].background_normal = 'imagenes/matriculas.jpg'
          self.all_widgets[x, y].background_down = 'imagenes/matriculas.jgp'
          with self.all_widgets[x, y].canvas.before:
            kivy.graphics.Color(0, 1, 0, 1)  # green; colors range from 0-1 not 0-255
            self.rect = kivy.graphics.Rectangle(size=self.all_widgets[x, y].size,
                                                pos=self.all_widgets[x, y].pos)
        if (self.mapa.matriz[x][y] == 3):
          self.all_widgets[x, y].text = "[color=FFFFF]Cajero[/color]"
          self.all_widgets[x, y].background_normal = 'imagenes/director.png'
          self.all_widgets[x, y].background_down = 'imagenes/director.png'
          with self.all_widgets[x, y].canvas.before:
            kivy.graphics.Color(0, 1, 0, 1)  # green; colors range from 0-1 not 0-255
            self.rect = kivy.graphics.Rectangle(size=self.all_widgets[x, y].size,
                                                pos=self.all_widgets[x, y].pos)
        if (self.mapa.matriz[x][y] == 4):
          self.all_widgets[x, y].text = "[color=FFFFF]Responsable[/color]"
          self.all_widgets[x, y].background_normal = 'imagenes/responsable.jpeg'
          self.all_widgets[x, y].background_down = 'imagenes/responsable.jpeg'
          with self.all_widgets[x, y].canvas.before:
            kivy.graphics.Color(0, 1, 0, 1)  # green; colors range from 0-1 not 0-255
            self.rect = kivy.graphics.Rectangle(size=self.all_widgets[x, y].size,
                                                pos=self.all_widgets[x, y].pos)

  def build(self):
    # para estudiante, caja, director,responsable, en orden estara.
    vectorD = np.random.rand(4) * 10
    vectorD = vectorD.astype(np.uint8)

    self.mapa = MapaUmss()
    self.mapa.setPosEstudiante(1, vectorD[0])
    self.mapa.setPosOficinasMatriculas(2, vectorD[1])
    self.mapa.setPosCajero(3, vectorD[2])
    self.mapa.setPosResponsable(4, vectorD[3])
    self.est = Estudiante("", 0)
    self.dir = Director()
    self.caj = Cajero()
    self.res = Responsable()
    self.costoMatricula = 14

    boxLayout = kivy.uix.boxlayout.BoxLayout(orientation="vertical")

    gridLayout = kivy.uix.gridlayout.GridLayout(rows=10, size_hint_y=9)
    boxLayout_buttons = kivy.uix.boxlayout.BoxLayout(orientation="horizontal")

    boxLayout.add_widget(gridLayout)
    boxLayout.add_widget(boxLayout_buttons)

    self.all_widgets = np.zeros(shape=(10, 10), dtype="O")

    for row_idx in range(self.all_widgets.shape[0]):
      for col_idx in range(self.all_widgets.shape[1]):
        self.all_widgets[row_idx, col_idx] = kivy.uix.button.Button(text=str("V") + ", " + str("V"),
                                                                    font_size=15)
        self.all_widgets[row_idx, col_idx].markup = True
        gridLayout.add_widget(self.all_widgets[row_idx, col_idx])

    ponerPosicionesDatos = kivy.uix.button.Button(text="Poner datos", font_size=15, size_hint_x=1)
    ponerPosicionesDatos.bind(on_press=self.ponerPosiciones)
    correrAgentes = kivy.uix.button.Button(text='iniciar', font_size=15, size_hint_x=1)
    correrAgentes.bind(on_press=self.correrMatriz)
    # agrega el boton
    boxLayout_buttons.add_widget(correrAgentes)
    boxLayout_buttons.add_widget(ponerPosicionesDatos)

    return boxLayout

  def buscarOficina(self, cod):
    valor = np.where(self.mapa.matriz == cod)
    x = valor[0]
    y = valor[1]
    print(self.mapa.matriz[x, y], x, y)
    # es la posicion x y de la posicion de la oficina
    return valor

  # la estudiante=1, caja=2, director=3, responsable=4
  def correrMatriz(self, *args):
    estudiantes = self.crearEstudiantesDatosAleatorios()
    for estudiante in estudiantes:
      self.est = estudiante
      print(self.est.codEstudiante, self.est.codMatricula, self.est.materias, self.est.dinero)
    cobrarMatricula = self.caj.cobrarMatricula(self.est.codEstudiante)
    comprarMatricula = self.est.pagarMatricula(self.caj)
    if (cobrarMatricula[0] and comprarMatricula):
      print(self.est.codEstudiante, " compro matricula")
      self.est.setTiempoEmpleado(cobrarMatricula[1])
      self.caj.darMatricula(self.est)
      print("Tiempo empleado de est:", self.est.tiempoEmpleado, "Y codMatricula:", self.est.codMatricula)
      print("Estudiante debe avanzar ala siguiente oficina: Director ")
      ubicacionOfDirector = self.buscarOficina(3)
      print("La oficina del director esta en ", ubicacionOfDirector[0], ubicacionOfDirector[1])
      print("Estudiante se dirige a esa oficina")
      print("Estudiante muestra la matricula, al director, el director la registra, da el visto bueno")
      registro = self.dir.registrarMatricula(self.est.mostrarMatricula())
      if (registro):
        print("Estudiante entrega la lista de materias que desea inscribirse")
        print("Director registra estas materias y las guarda en una lista")
        self.dir.registrarMaterias(self.est.darListaMaterias())
        print("Estudiante se va a casa")
        self.est.irCasa()
        # cuando termina o almenos tiene un estudiante
        print("Director busca la oficina de Responsable, para entregarle la lista de codigos y materias ")
        print("Director tiene la siguiente lista de codigos y materias:", self.dir.listaMateriasCod)
        ubicacionOfResponsable = self.buscarOficina(4)
        print("La oficina del Responsable esta en ", ubicacionOfResponsable[0], ubicacionOfResponsable[1])
        self.res.registrarCodigosMaterias(self.dir.entregarListaCodigosMaterias())
        print("DIrecot entrega lista y se marcha")
        self.dir.irCasa()
        print("Responsable evalua las materias y las habilita segun criterio impuesto")
        self.res.habilitarMaterias(1, 0)
        print("Las materias habilitadas son las siguientes:", self.res.materiasHabilitadas)
        print("Los estudiantes habilitados segun su codigo  son los siguientes:", self.res.estudianteHabilitados)

  def crearEstudiantesDatosAleatorios(self):
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
        try:
          est.materias.index(materia)
        except:
          est.materias.append(materia)
          m = m - 1
      estudiantes.append(est)
    return estudiantes


if __name__ == '__main__':
  buzzleApp = BuzzleApp()
  buzzleApp.run()
