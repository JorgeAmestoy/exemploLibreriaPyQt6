import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QGridLayout, QLabel, QMainWindow, QWidget, QStackedLayout, QVBoxLayout, \
    QHBoxLayout, QPushButton

from cajaColor import CajaColor #cajaColor es la clase y CajaColor es el metodo

#Clase que hereda de la super clase QGridLayout y que me devuelve un grid con widgets que solo son colores.
#Trabajo con el self porque ya estoy trabajando directamente con un objeto de tipo QGridLayout.
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

        self.setWindowTitle("Ejemplo QStacked Layout con Qt")

        cajaV1 = QVBoxLayout()



        # Creo caja horizontal 1
        cajaH1 = QHBoxLayout()
        boton1 = QPushButton("Rojo")
        boton1.clicked.connect(self.on_btnRojo_pressed)
        cajaH1.addWidget(boton1)
        boton2 = QPushButton("Azul")
        boton2.clicked.connect(self.on_btnAzul_pressed)
        cajaH1.addWidget(boton2)
        boton3 = QPushButton("Grid")
        boton3.clicked.connect(self.on_btnMalla_pressed)
        cajaH1.addWidget(boton3)
        boton4 = QPushButton("Box Horizontal Colores")
        boton4.clicked.connect(self.on_btnModificado_pressed)
        cajaH1.addWidget(boton4)
        cajaV1.addLayout(cajaH1)# Añado la cajaH1 a la cajaV1

        # Creo tarjetas
        self.tarjetas = QStackedLayout()
        cajaV1.addLayout(self.tarjetas)# Añado la tarjeta a la cajaV1

        #Añado el contenido a las tarjetas
        self.tarjetas.addWidget(CajaColor("red"))# Añado contenido a la tarjeta [0]
        self.tarjetas.addWidget(CajaColor("blue"))# Añado contenido a la tarjeta [1]

        # Creo widget en el que añado el grid, el cual será el contenido de la tarjeta [2]
        widgetGrid = QWidget()
        widgetGrid.setLayout(GridConContenido())
        self.tarjetas.addWidget(widgetGrid)

        # Creo widget en el que añado la caja horizontal de colores, la cual será el contenido de la tarjeta [3]
        widgetCajaH = QWidget()
        widgetCajaH.setLayout(boxHorizontalColores())
        self.tarjetas.addWidget(widgetCajaH)


        container = QWidget()
        container.setLayout(cajaV1)
        self.setCentralWidget(container)
        self.show()

    def on_btnRojo_pressed(self):
        self.tarjetas.setCurrentIndex(0)

    def on_btnAzul_pressed(self):
        self.tarjetas.setCurrentIndex(1)

    def on_btnMalla_pressed(self):
        self.tarjetas.setCurrentIndex(2)

    def on_btnModificado_pressed(self):
        self.tarjetas.setCurrentIndex(3)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    app.exec()
