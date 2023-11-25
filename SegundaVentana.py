import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QLineEdit
from PyQt6.QtGui import QPixmap

class SegundaVentana(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mi segunda ventana con Qt")

        self.txtCaja = QLineEdit()
        #self.txtCaja.editingFinished.connect(self.on_txtCaja_enter)#Para que cuando pulsemos enter se cambie solo el texto sin ncesidad de darle click con el ratón
        self.txtCaja.returnPressed.connect(self.on_txtCaja_enter)

        self.lblEtiqueta1 = QLabel("Hola, qué tal?")
        fuente = self.lblEtiqueta1.font()
        fuente.setPointSize(30)
        self.lblEtiqueta1.setFont(fuente)
        self.lblEtiqueta1.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)#Para alinear la etiqueta a la derecha

        boton = QPushButton("Saludo")
        boton.clicked.connect(self.on_txtCaja_enter)


        cajaVertical = QVBoxLayout()
        cajaVertical.addWidget(self.lblEtiqueta1)
        cajaVertical.addWidget(self.txtCaja)
        cajaVertical.addWidget(boton)

        container = QWidget()
        container.setLayout(cajaVertical)
        self.setCentralWidget(container)

        self.setFixedSize(400,400)
        self.show()

    def on_txtCaja_enter(self):
        saludo = self.txtCaja.text()
        self.lblEtiqueta1.setText(saludo)


if __name__ =="__main__":
    aplicacion = QApplication(sys.argv)
    ventana = SegundaVentana()
    aplicacion.exec()
