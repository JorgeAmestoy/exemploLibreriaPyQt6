import sys

from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

from cajaColor import *

class VentanaPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejemplo Grid Layout con Qt")

        red = QGridLayout()


        red.addWidget(CajaColor("red"))
        red.addWidget(CajaColor("blue"),0,1,1,2)
        red.addWidget(CajaColor("green"),1,0,2,1)
        red.addWidget(CajaColor("pink"),1,1,1,2)
        red.addWidget(CajaColor("orange"),2,1,1,1)
        red.addWidget(CajaColor("yellow"),2,2,1,1)



        container = QWidget()
        container.setLayout(red)
        self.setCentralWidget(container)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.setFixedSize(400,400)
    app.exec()
