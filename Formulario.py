import sys

from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel,QCheckBox,
                             QVBoxLayout, QHBoxLayout, QWidget, QListView, QLineEdit,
                             QComboBox, QGridLayout, QSlider, QFrame)
from PyQt6.QtCore import Qt, QAbstractListModel
from PyQt6.QtGui import QPixmap



import sys

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("FORMULARIO")


        cajaVPrincipal = QVBoxLayout()

        cajaHorizontal1 = QHBoxLayout()
        cajaVPrincipal.addLayout(cajaHorizontal1)


        cajaVertical1 = QVBoxLayout()
        cajaVertical1.setAlignment(Qt.AlignmentFlag.AlignTop)# Para que me alinie toddo para arriba (que suba el disco y el check para arriba)
        cajaHorizontal1.addLayout(cajaVertical1)# Añado la caja vertical1 en la primera horizontal
        etiqueta = QLabel()
        etiqueta.setPixmap(QPixmap("cd.png"))
        cajaVertical1.addWidget(etiqueta)
        checkAnimado = QCheckBox("Animado")
        cajaVertical1.addWidget(checkAnimado)

        lista = QListView()
        cajaHorizontal1.addWidget(lista)# Añade la lista en la cala horizontal1 directamente

        cajaVertical2 = QVBoxLayout()
        cajaHorizontal1.addLayout(cajaVertical2)# Añado la caja vertical2 a la horizontal1

        #Añado botones a la caja vertical2
        botonEngadirLista = QPushButton("Engadir pista a reproducir")
        cajaVertical2.addWidget(botonEngadirLista)
        botonSubirLista = QPushButton("Subir na lista")
        cajaVertical2.addWidget(botonSubirLista)
        botonBajarLista = QPushButton("Baixar na lista")
        cajaVertical2.addWidget(botonBajarLista)
        grid = QGridLayout()
        botonSaltar = QPushButton("Saltar")
        grid.addWidget(botonSaltar)
        comboSaltar = QComboBox()
        grid.addWidget(comboSaltar,0,1,1,1)
        cajaVertical2.addLayout(grid)
        botonAbrirFichero = QPushButton("Abrir fichero")
        cajaVertical2.addWidget(botonAbrirFichero)
        botonReproducirFichero = QPushButton("Reproducir fichero")
        cajaVertical2.addWidget(botonReproducirFichero)
        botonGardarComo = QPushButton("Gardar como..")
        cajaVertical2.addWidget(botonGardarComo)
        botonEliminarPista = QPushButton("Eliminar pista")
        cajaVertical2.addWidget(botonEliminarPista)

        cajaHorizontal2 = QHBoxLayout()# Creo caja horizontal2
        grid2 = QGridLayout()
        cajaHorizontal2.addLayout(grid2)
        lblSon = QLabel("Son: ")
        lblRitmo = QLabel("Ritmo: ")
        lblVolume = QLabel("Volume: ")
        lblFormato = QLabel("Formato")
        lblSalida = QLabel("Salida de audio")
        comboSon = QComboBox()
        grid.addWidget(comboSon,0,1,1,2)
        grid2.addWidget(lblSon,0,0,1,1)
        grid2.addWidget(lblRitmo, 1, 0, 1, 1)
        grid2.addWidget(lblVolume, 2, 0, 1, 1)
        grid2.addWidget(lblFormato, 3, 0, 1, 1)
        grid2.addWidget(lblSalida, 4, 0, 1, 1)



        cajaHorizontalFrame = QHBoxLayout()# Creo caja horizontal del ftrame
        frameReproduccion = QFrame()# Creo el frame
        frameReproduccion.setFrameStyle(QFrame.Shape.Box)
        frameReproduccion.setLayout(cajaHorizontalFrame)# Añado la caja horizontal del frame al frame
        frameReproduccion.setWindowTitle("Opcions de reproduccion")
        cajaHorizontal2.addWidget(frameReproduccion)# Añado el frame con la caja a la caja horizontal
        cajaVIzquierda = QVBoxLayout() #caja vertical
        chkFiltrar = QCheckBox("Filtrar antes de reproducir")
        chkEXml = QCheckBox("É XML")
        chkReproduccion = QCheckBox("Reproducción NPL")
        cajaVIzquierda.addWidget(chkFiltrar)
        cajaVIzquierda.addWidget(chkEXml)
        cajaVIzquierda.addWidget(chkReproduccion)
        cajaVDerecha = QVBoxLayout()
        cajaHorizontalFrame.addLayout(cajaVIzquierda)
        cajaHorizontalFrame.addLayout(cajaVDerecha)
        checkBoxAsincrono = QCheckBox("Sincrono")
        checkBoxNome = QCheckBox()
        checkBoxXML = QCheckBox()
        cajaVDerecha.addWidget(checkBoxAsincrono)
        cajaVDerecha.addWidget(checkBoxNome)
        cajaVDerecha.addWidget(checkBoxXML)



        cajaVPrincipal.addLayout(cajaHorizontal2)









        container = QWidget()
        container.setLayout(cajaVPrincipal)#Añadir layout principal
        self.setCentralWidget(container)
        self.setFixedSize(800,500)
        self.show()



if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    aplicacion.exec()