import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QPixmap

class PrimeraVentana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mi primera ventana con Qt")#LLamo a un método de la clase para poner el titulo de la ventana

        self.lblEtiqueta1 = QLabel("Hola, qué tal?")
        lblEtiqueta2 = QLabel()
        lblEtiqueta2.setPixmap(QPixmap("fotoluci2.jpg"))
        botonSaludo = QPushButton("Saludo")
        botonSaludo.clicked.connect(self.on_botonSaludo_clicked)

        cajaVertical = QVBoxLayout()
        cajaVertical.setAlignment(Qt.AlignmentFlag.AlignRight)
        cajaVertical.addWidget(self.lblEtiqueta1)
        cajaVertical.addWidget(lblEtiqueta2)
        cajaVertical.addWidget(botonSaludo)

        container = QWidget()
        container.setLayout(cajaVertical)
        self.setCentralWidget(container)

        self.setFixedSize(400,400)
        self.show()

    def on_botonSaludo_clicked(self):
        self.lblEtiqueta1.setText("Hola companheros!!!")


if __name__ =="__main__":
    aplicacion = QApplication(sys.argv)
    ventana = PrimeraVentana()
    aplicacion.exec()
