import kivy.app
import kivy.uix.gridlayout
import kivy.uix.boxlayout
import kivy.uix.button
import kivy.uix.textinput
import kivy.uix.label
import numpy
from MapaUmss import MapaUmss
from agentes.Cajero import Cajero
from agentes.Director import Director
from agentes.Estudiante import Estudiante
from agentes.Responsable import Responsable


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
    self.mapa = MapaUmss()
    self.mapa.setPosEstudiante(0, 4)
    self.mapa.setPosOficinasMatriculas(4, 0)
    self.mapa.setPosCajero(8, 4)
    self.mapa.setPosResponsable(4, 8)
    self.est = Estudiante("Ing.Informatica")
    self.dir = Director()
    self.caj = Cajero()
    self.res = Responsable()

    boxLayout = kivy.uix.boxlayout.BoxLayout(orientation="vertical")

    gridLayout = kivy.uix.gridlayout.GridLayout(rows=10, size_hint_y=9)
    boxLayout_buttons = kivy.uix.boxlayout.BoxLayout(orientation="horizontal")

    boxLayout.add_widget(gridLayout)
    boxLayout.add_widget(boxLayout_buttons)

    self.all_widgets = numpy.zeros(shape=(10, 10), dtype="O")

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

  def correrMatriz(self, *args):
    print('---- Iteracion inicial ----')
    print(self.mapa.matriz)
    print('\n', 'Estudiante:', self.est.getEstado(), '\n'
          , 'Director:', self.dir.getEstado(), '\n'
          , 'Cajero:', self.caj.getEstado(), '\n'
          , 'Responsable:', self.res.getEstado())

    g = 1

    while self.est.getMaterias() > 0:
      if self.est.pagar_a(self.caj):
        self.est.setEstado(2)
        self.caj.setEstado(2)
        print('---- Iteracion ', g, ' ----')
        print(self.mapa.matriz)
        print('\n', 'Estudiante:', self.est.getEstado(), '\n'
              , 'Director:', self.dir.getEstado(), '\n'
              , 'Cajero:', self.caj.getEstado(), '\n'
              , 'Responsable:', self.res.getEstado())
      self.est.resMaterias()


if __name__ == '__main__':
  buzzleApp = BuzzleApp()
  buzzleApp.run()
