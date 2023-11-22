import sys

from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *


class CajaColor(QWidget):
    def __init__(self,color):
        super().__init__()
        self.setAutoFillBackground(True)
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(paleta)

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("EJemplo con Box")
        cajaHorizontalBase= QHBoxLayout()
        caja2 = QVBoxLayout()


        caja2.addWidget(CajaColor("red"))
        caja2.addWidget(CajaColor("yellow"))
        caja2.addWidget(CajaColor("blue"))

        cajaHorizontalBase.addLayout(caja2)

        cajaHorizontalBase.addWidget(CajaColor("green"))

        caja3 = QVBoxLayout()
        caja3.addWidget(CajaColor("blue"))
        caja3.addWidget(CajaColor("orange"))
        cajaHorizontalBase.addLayout(caja3)

        caja4 = QHBoxLayout()
        caja4.addWidget(CajaColor("pink"))
        caja4.addWidget(CajaColor("black"))
        caja4.addWidget(CajaColor("white"))
        cajaHorizontalBase.addLayout(caja4)

        cajaHorizontalBase.addWidget(CajaColor("pink"))



        container = QWidget()
        container.setLayout(cajaHorizontalBase)
        self.setCentralWidget(container)


if __name__ == "__main__":
    app =QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    ventana.setFixedSize(400, 400)
    sys.exit(app.exec())

