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

  def update_board_UI(self, *args):
    limitX = self.mapa.matriz[0].size
    limitY = self.mapa.matriz[0].size
    print(self.mapa.matriz[0][4])
    for x in range(limitX):
      for y in range(limitY):
        if (self.mapa.matriz[x][y] == 1):
          self.all_widgets[x, y].text = "[color=22ff22]Estudiante[/color]"
          with self.all_widgets[x, y].canvas.before:
            kivy.graphics.Color(0, 1, 0, 1)  # green; colors range from 0-1 not 0-255
            self.rect = kivy.graphics.Rectangle(size=self.all_widgets[x, y].size,
                                                pos=self.all_widgets[x, y].pos)
        if (self.mapa.matriz[x][y] == 2):
          self.all_widgets[x, y].text = "[color=22ff22]Oficina[/color]"
          with self.all_widgets[x, y].canvas.before:
            kivy.graphics.Color(0, 1, 0, 1)  # green; colors range from 0-1 not 0-255
            self.rect = kivy.graphics.Rectangle(size=self.all_widgets[x, y].size,
                                                pos=self.all_widgets[x, y].pos)
        if (self.mapa.matriz[x][y] == 3):
          self.all_widgets[x, y].text = "[color=22ff22]Cajero[/color]"
          with self.all_widgets[x, y].canvas.before:
            kivy.graphics.Color(0, 1, 0, 1)  # green; colors range from 0-1 not 0-255
            self.rect = kivy.graphics.Rectangle(size=self.all_widgets[x, y].size,
                                                pos=self.all_widgets[x, y].pos)
        if (self.mapa.matriz[x][y] == 4):
          self.all_widgets[x, y].text = "[color=22ff22]Responsable[/color]"
          with self.all_widgets[x, y].canvas.before:
            kivy.graphics.Color(0, 1, 0, 1)  # green; colors range from 0-1 not 0-255
            self.rect = kivy.graphics.Rectangle(size=self.all_widgets[x, y].size,
                                                pos=self.all_widgets[x, y].pos)

  def build(self):
    self.mapa = MapaUmss()
    self.mapa.setPosEstudiante(0, 4)
    self.mapa.setPosOficinas(4, 0)
    self.mapa.setPosCajero(8, 4)
    self.mapa.setPosResponsable(4, 8)
    self.est = Estudiante()
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
                                                                    font_size=25)
        self.all_widgets[row_idx, col_idx].markup = True
        gridLayout.add_widget(self.all_widgets[row_idx, col_idx])

    ga_solution_button = kivy.uix.button.Button(text="Poner datos", font_size=15, size_hint_x=1)
    ga_solution_button.bind(on_press=self.update_board_UI)
    # agrega el boton
    boxLayout_buttons.add_widget(ga_solution_button)

    return boxLayout


if __name__ == '__main__':
  buzzleApp = BuzzleApp()
  buzzleApp.run()
