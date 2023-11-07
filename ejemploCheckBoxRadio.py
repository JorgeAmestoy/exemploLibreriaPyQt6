import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QCheckBox
from PyQt6.QtGui import QPixmap

class ejemploCheckBoxRadio(QMainWindow):#clase que hereda las propiedades de QMainWindowss
    def __init__(self):#Lo primero que hacemos es llamar al inicializador(constructor) de la super clase
        super().__init__()

        self.setWindowTitle("Ejemplo con QCheckBox")

        cajaVertical = QVBoxLayout()

        #Al poner varios funciones, pongo el self antes de los checkBotones para diferenciarlos¿?
        self.checkBoton1 = QCheckBox("Boton 1")
        self.checkBoton1.toggled.connect(self.on_checkBoton1_toggled)
        cajaVertical.addWidget(self.checkBoton1)

        self.checkBoton2 = QCheckBox("Boton 2")
        self.checkBoton2.toggled.connect(self.on_checkBoton2_toggled)
        cajaVertical.addWidget(self.checkBoton2)


        container = QWidget()
        container.setLayout(cajaVertical)
        self.setCentralWidget(container)

        self.setFixedSize(400,300)
        self.show()

    def on_checkBoton1_toggled(self):
        if self.checkBoton1.isChecked():
            print("Boton check seleccionado: ", self.checkBoton1.text())
        else:
            print("Boton check deseleccionado ", self.checkBoton1.text())

    def on_checkBoton2_toggled(self):
        if self.checkBoton2.isChecked():
            print("Boton check seleccionado: ",self.checkBoton2.text())
        else:
            print("Boton check deseleccionado ",self.checkBoton2.text())



    def on_botonSaludo_clicked(self):#Tiene que llamarse igual que como lo declaraste en el clicked.connect.
        self.lblEtiqueta1.setText("Hola companheros!!!")




if __name__ =="__main__":
    aplicacion = QApplication(sys.argv)
    ventana = ejemploCheckBoxRadio()#creamos instancia de nuestra primera ventana. Como en JAVA, llamamos a la clase.
    aplicacion.exec()