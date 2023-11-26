import sys

from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

# Clase que hereda de QWidget y nos devuelve un Widget
class CajaColor(QWidget):
    def __init__(self,color):# Inicializo con un constructor que recibirá por parámetro un color
        super().__init__()
        self.setAutoFillBackground(True) # Rellenar el fondo de un color
        paleta = self.palette() # Obtiene la paleta de colores actual asociada al widget (QWidget en este caso(QMinWindow es un Widget también).
        paleta.setColor(QPalette.ColorRole.Window, QColor(color))# Establezco el color de fondo de la ventana
        self.setPalette(paleta)#  Aplica la paleta de colores actualizada al widget, lo que incluye el nuevo color de fondo configurado.

class GridClase(QGridLayout):
    def __init__(self):
        super().__init__()
        self.addWidget(CajaColor("red"))
        self.addWidget(CajaColor("green"),1,0,2,1)
        self.addWidget(CajaColor("blue"),0,1,1,2)
        self.addWidget(CajaColor("pink"),1,1,1,2)
        self.addWidget(CajaColor("orange"),2,1,1,1)
        self.addWidget(CajaColor("yellow"),2,2,1,1)


class BoxHorizontalColores(QHBoxLayout):
    def __init__(self):
        super().__init__()

        caja2 = QVBoxLayout()
        caja3 = QVBoxLayout()

        caja2.addWidget(CajaColor("red"))
        caja2.addWidget(CajaColor("yellow"))
        caja2.addWidget(CajaColor("purple"))
        self.addLayout(caja2)

        caja3.addWidget(CajaColor("blue"))
        caja3.addWidget(CajaColor("orange"))
        self.addLayout(caja3)

        self.addWidget(CajaColor("green"))



class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mi primera aplicacion")






        container = QWidget()
        container.setLayout()  # Añadir layout principal
        self.setCentralWidget(container)
        self.show()



if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    aplicacion.exec()