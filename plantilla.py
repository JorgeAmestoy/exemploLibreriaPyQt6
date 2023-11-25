from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *



import sys

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mi primera aplicacion")






        container = QWidget()
        container.setLayout()  # Añadir layout principal
        self.setCentralWidget(container)
        #self.setFixedSize(400,400)
        self.show()




if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    aplicacion.exec()