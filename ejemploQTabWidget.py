import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QGridLayout, QLabel, QMainWindow, QWidget, QTabWidget, QHBoxLayout, QVBoxLayout

from cajaColor import CajaColor #cajaColor es la clase y CajaColor es el metodo


class GridConContenido(QGridLayout):
    def __init__(self):
        super().__init__()

        #Añado al layout
        self.addWidget(CajaColor("red"))
        self.addWidget(CajaColor("blue"), 0, 1, 1, 2)
        self.addWidget(CajaColor("green"), 1, 0, 2, 1)
        self.addWidget(CajaColor("pink"), 1, 1, 1, 2)
        self.addWidget(CajaColor("orange"), 2, 1, 1, 1)
        self.addWidget(CajaColor("yellow"), 2, 2, 1, 1)

#Clase que hereda de la super clase QHBoxLayout y que me devuelve un grid con widgets que solo son colores.
#Trabajo con el self porque ya estoy trabajando directamente con un objeto de tipo QHBoxLayout.
class boxHorizontalColores(QHBoxLayout):
    def __init__(self):
        super().__init__()

        # Creo cajas verticales
        caja2 = QVBoxLayout()
        caja3 = QVBoxLayout()

        # Añado el contenido (widgets) a la caja vertical 2
        caja2.addWidget(CajaColor("red"))
        caja2.addWidget(CajaColor("yellow"))
        caja2.addWidget(CajaColor("purple"))
        self.addLayout(caja2)# Como estamos heredando de QHboxLayout, el cual nos devuelve un objeto de tipo Caja Horizontal, el self hace referencia a esta misma caja horizontal. Así, añado la caja vertical al self caja horizontal

        # Añado el contenido (widgets) a la caja vertical 3
        caja3.addWidget(CajaColor ("blue"))
        caja3.addWidget(CajaColor ("orange"))
        self.addLayout(caja3)

        self.addWidget(CajaColor("green"))

class VentanaPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejemplo QTabWidget")

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.TabPosition.South)
        tabs.setMovable(True)

        # AÑADO 3 PESTAÑAS
        miTupla = ("red", "green", "blue")
        #Recorro tupla para no tener que añadir color a color
        for color in miTupla:
          tabs.addTab(CajaColor(color), color)

        # AÑADO 4º PESTAÑA SIN NOMBRE
        widgetGrid = QWidget()
        widgetGrid.setLayout(GridConContenido())
        tabs.addTab(widgetGrid, None)

        # AÑADO 5º PESTAÑA
        widgetHorizontal = QWidget()
        widgetHorizontal.setLayout(boxHorizontalColores())
        tabs.addTab(widgetHorizontal, "Box Horizontal")


        self.setCentralWidget(tabs)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    app.exec()
