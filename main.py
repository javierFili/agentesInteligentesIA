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
          self.all_widgets[x, y].text = "[color=FFFFF]Cajero[/color]"
          self.all_widgets[x, y].background_normal = 'imagenes/matriculas.jpg'
          self.all_widgets[x, y].background_down = 'imagenes/matriculas.jgp'
          with self.all_widgets[x, y].canvas.before:
            kivy.graphics.Color(0, 1, 0, 1)  # green; colors range from 0-1 not 0-255
            self.rect = kivy.graphics.Rectangle(size=self.all_widgets[x, y].size,
                                                pos=self.all_widgets[x, y].pos)
        if (self.mapa.matriz[x][y] == 3):
          self.all_widgets[x, y].text = "[color=FFFFF]Director[/color]"
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
    # para estudiante, cajero, director,responsable, en orden estara.
    vectorD = np.random.rand(4) * 10
    vectorD = vectorD.astype(np.uint8)

    self.mapa = MapaUmss()
    self.mapa.setPosEstudiante(1, vectorD[0])
    self.mapa.setPosOficinasMatriculas(4, vectorD[1])
    self.mapa.setPosOficinaDirector(6, vectorD[2])
    self.mapa.setPosOficinaResponsable(9, vectorD[3])
    self.est = Estudiante("", 0)
    self.dir = Director()
    self.caj = Cajero()
    self.res = Responsable()

    boxLayout = kivy.uix.boxlayout.BoxLayout(orientation="vertical")

    gridLayout = kivy.uix.gridlayout.GridLayout(rows=10, size_hint_y=10)
    boxLayout_buttons = kivy.uix.boxlayout.BoxLayout(orientation="horizontal")

    boxLayout.add_widget(gridLayout)
    boxLayout.add_widget(boxLayout_buttons)

    self.all_widgets = np.zeros(shape=(10, 10), dtype="O")

    for row_idx in range(self.all_widgets.shape[0]):
      for col_idx in range(self.all_widgets.shape[1]):
        self.all_widgets[row_idx, col_idx] = kivy.uix.button.Button(text=str("Vacio"),
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
    return valor

  # la estudiante=1, caja=2, director=3, responsable=4
  def correrMatriz(self, *args):
    estudiantes = self.crearEstudiantesDatosAleatorios()
    print("[---- Inicio ----]")
    for estudiante in estudiantes:
      self.est = estudiante
      self.est.setTiempoEmpleado(self.caj.tiempoTotal)
      ubicacionOfCajero = self.buscarOficina(2)

      # Interaccion estudiante - cajero
      print("\n--- El estudiante", self.est.codEstudiante, "inicia transaccion con el cajero ---"
            , "\n- Estudiante se dirige a la oficina de Cajero, ubicada en :", ubicacionOfCajero[0],
            ubicacionOfCajero[1])
      cobrarMatricula = self.caj.cobrarMatricula(self.est.codEstudiante)
      comprarMatricula = self.est.pagarMatricula(self.caj)
      self.caj.setTiempoTotal(cobrarMatricula[1])

      if (cobrarMatricula[0] and comprarMatricula and self.est.estado):

        print("- El estudiante", self.est.codEstudiante, "compro matricula")
        self.est.setTiempoEmpleado(cobrarMatricula[1])
        self.caj.darMatricula(self.est)

        print("Tiempo empleado de est:", self.est.tiempoEmpleado, "Y codMatricula:", self.est.codMatricula,
              "\n- Estudiante debe avanzar ala siguiente oficina: Director ")
        ubicacionOfDirector = self.buscarOficina(3)

        # Interaccion estudiante - director
        print("\n--- El estudiante", self.est.codEstudiante, "inicia transaccion con el Director ---",
              "\n- La oficina del director esta en ", ubicacionOfDirector[0], ubicacionOfDirector[1],
              "\n- Estudiante se dirige a esa oficina",
              "\n- Estudiante muestra la matricula al director",
              "\n- Director la registra y valida la matricula")

        registro = self.dir.registrarMatricula(self.est.mostrarMatricula())
        self.est.setTiempoEmpleado(registro[1])  # se agrega mas tiempo al estudiante
        if (registro and self.est.estado):
          print("- Estudiante entrega la lista de materias que desea inscribirse",
                "\n- Director registra estas materias y las guarda en una lista")

          registroMat = self.dir.registrarMaterias(self.est.darListaMaterias())
          self.est.setTiempoEmpleado(registroMat[1])

          print("\n--- El estudiante", self.est.codEstudiante, "se va a casa ---"
                , "\nEstudiante invirtio un tiempo de "
                , self.est.tiempoEmpleado
                , "\n\n{--- Se atiende al siguiente estudiante en la cola ---}")

          self.est.irCasa()
        else:
          print("x--- El estudiante", self.est.codEstudiante, "no tiene tiempo disponible ---x"
                , "\n\n{--- Se atiende al siguiente estudiante en la cola ---}")
      else:
        print("X El estudiante", self.est.codEstudiante,
              "no tiene el dinero suficiente o tampoco cuenta con tiempo disponible"
              , "\n\n{--- Se atiende al siguiente estudiante en la cola ---}")

    # Interaccion director - responsable
    print("\n--- El Director inicia transaccion con el Responsable ---",
          "\n- Director busca la oficina de Responsable, para entregarle la lista de codigos y materias ",
          "\n- Director tiene la siguiente lista de codigos y materias:")
    for materia in self.dir.listaMateriasCod:
      print(materia)
    ubicacionOfResponsable = self.buscarOficina(4)
    print("- La oficina del Responsable esta en ", ubicacionOfResponsable[0], ubicacionOfResponsable[1])
    self.res.registrarCodigosMaterias(self.dir.entregarListaCodigosMaterias())
    print("- Director entrega lista y se marcha")
    self.dir.irCasa()

    # Actividad solo del responsable
    print("\n--- El Responsable inicia el proceso de habilitacion ---",
          "\n- Responsable evalua las materias y las habilita segun criterio impuesto")
    # se habilita materias con un minimo de 3 inscritos
    self.res.habilitarMaterias(2)
    print("- Las materias habilitadas son las siguientes:", "\n", self.res.materiasHabilitadas,
          "\n- Los estudiantes habilitados segun su codigo son los siguientes:", self.res.estudianteHabilitados)

  def crearEstudiantesDatosAleatorios(self):
    estudiantes = []
    n = 10
    matExistentes = MateriasExistentes()
    while (n > 0):
      n = n - 1
      est = Estudiante("Ing.Sistemas", n)
      dineroAsignado = np.random.rand(1) * 30  # modificable para el dinero que tendra el estudiante
      dineroAsignado = dineroAsignado.astype(np.uint8)
      est.setDinero(dineroAsignado)
      tiempoAsignado = np.random.rand(1) * 50  # modificable para el tiempo que se le dio a estudiante
      tiempoAsignado = tiempoAsignado.astype(np.uint8)
      est.setTiempoAsignado(tiempoAsignado)
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
