from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *



import sys
class ModeloLista(QAbstractListModel):
    def __init__(self,musica = None):
        super().__init__()
        self.musica = musica or []


    def data(self, indice, rol):
        if (rol == Qt.ItemDataRole.DisplayRole):# En caso de que el rol sea el de visualización del ítem, en este caso, un texto visible...:
            texto = self.musica[indice.row()] # Accede al elemento de la lista (self.tareas) correspondiente a la posición indicada por el índice de fila (indice.row()). Se asume que cada elemento es una tupla con al menos dos elementos: un estado y un texto. Recogemos una fila y nos da el estado y el texto, y solo nos interesa el texto. ASi data nos devuelve el texto que metamos en tarefas.
            return texto # Devuelve el texto de la tarea

    def rowCount(self, indice):
        return len(self.musica)


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("EXAMEN FORMULARIO")

        #Creo caja Vertical Principal y añado las dos cajas horizontales que actuan como filas
        cajaV1 = QVBoxLayout()
        cajaH1 = QHBoxLayout()
        cajaV1.addLayout(cajaH1)
        cajaH2 = QHBoxLayout()
        cajaV1.addLayout(cajaH2)

        #Añado contenido a la caja horizontal 1
        cajaV2 = QVBoxLayout()# Creo caja vertical para meter la etiqueta del cd y el checkbox
        cajaH1.addLayout(cajaV2)
        lblFoto = QLabel()
        lblFoto.setPixmap(QPixmap("cd.png"))
        cajaV2.addWidget(lblFoto)
        checkBoton = QCheckBox("Animado")
        cajaV2.addWidget(checkBoton)
        cajaV2.setAlignment(Qt.AlignmentFlag.AlignTop)

        ejemploLista = []
        self.modelo = ModeloLista(ejemploLista)
        self.listaMusica = QListView()
        self.listaMusica.setModel(self.modelo)
        self.listaMusica.setFixedSize(300,250)


        cajaH1.addWidget(self.listaMusica)
        cajaV3 = QVBoxLayout()
        cajaH1.addLayout(cajaV3)
        boton1 = QPushButton("Engadir a pista a reproducir")
        cajaV3.addWidget(boton1)
        boton2 = QPushButton("Subir na lista")
        cajaV3.addWidget(boton2)
        boton3 = QPushButton("Baixa na lista")
        cajaV3.addWidget(boton3)
        cajaH3 = QHBoxLayout()
        cajaV3.addLayout(cajaH3)
        boton4 = QPushButton("Saltar")
        cajaH3.addWidget(boton4)
        self.combo1 = QComboBox()
        self.combo1.addItems(["Britney","Lana","La Beyonsebe"])# Añado items al ComboBox
        self.combo1.activated.connect(self.on_mostrarComboBox_activated)# Añado evento ACTIVATED a ComboBOX
        cajaH3.addWidget(self.combo1)
        boton5 = QPushButton("Abrir ficheiro...")
        cajaV3.addWidget(boton5)
        boton6 = QPushButton("Reproducir ficheiro...")
        cajaV3.addWidget(boton6)
        boton7 = QPushButton("Gardar como...")
        cajaV3.addWidget(boton7)
        boton8 = QPushButton("Eliminar pista...")
        cajaV3.addWidget(boton8)

        # Añado contenido a la caja horizontal 2
        grid1 = QGridLayout()
        cajaH2.addLayout(grid1)
        lbl1 = QLabel("Son:")
        grid1.addWidget(lbl1,0,0,1,1)
        lbl2 = QLabel("Ritmo:")
        grid1.addWidget(lbl2,1,0,1,1)
        lbl3 = QLabel("Volumen:")
        grid1.addWidget(lbl3,2,0,1,1)
        lbl4 = QLabel("Formato:")
        grid1.addWidget(lbl4,3,0,1,1)
        lbl5 = QLabel("Salida del audio:")
        grid1.addWidget(lbl5,4,0,1,1)
        comboS = QComboBox()
        grid1.addWidget(comboS, 0, 1, 1, 2)
        sliderRitmo = QSlider(Qt.Orientation.Horizontal)
        grid1.addWidget(sliderRitmo, 1,1,1,2)
        sliderVolumen = QSlider(Qt.Orientation.Horizontal)
        grid1.addWidget(sliderVolumen, 2, 1, 1, 2)
        sliderVolumen.valueChanged.connect(self.on_mostrarVolumen_slider)# Añado evento VALUE_CHANGED a SliderVolumen
        comboF = QComboBox()
        grid1.addWidget(comboF,3,1,1,2)
        comboSa = QComboBox()
        grid1.addWidget(comboSa, 4, 1, 1, 2)

        #Añado marco a la caja horizontal 2
        groupBox = QGroupBox("Opcion de reproduccion")
        cajaH2.addWidget(groupBox)
        grid2 = QGridLayout()
        groupBox.setLayout(grid2)
        self.checkBoton2 = QCheckBox("Asincrono")
        self.checkBoton2.toggled.connect(self.on_anadirLista_toggled)# Añado evento TOGGLED a CHECKBOTTON2
        grid2.addWidget(self.checkBoton2,0,0,1,1)
        checkBoton3 = QCheckBox("Es nome de ficheiro")
        grid2.addWidget(checkBoton3,1,0,1,1)
        checkBoton4 = QCheckBox("XML persistente")
        grid2.addWidget(checkBoton4,2,0,1,1)
        checkBoton5 = QCheckBox("Filtrar antes de reporducir")
        grid2.addWidget(checkBoton5,0,1,1,1)
        checkBoton6 = QCheckBox("Es XML")
        grid2.addWidget(checkBoton6,1,1,1,1)
        checkBoton7 = QCheckBox("Reproduccion NPL")
        grid2.addWidget(checkBoton7,2,1,1,1)


        container = QWidget()
        container.setLayout(cajaV1)
        self.setCentralWidget(container)
        self.setFixedSize(800,400)
        self.show()

    def on_mostrarVolumen_slider(self,valor):
        print("Valor del QSlider"+str(valor))

    def on_mostrarComboBox_activated(self, index):
        cantante_seleccionada = self.combo1.currentText()# Guarda el texto del comboBox seleccionado
        opcion_escogida = self.combo1.currentIndex() # Guarda el índice del combobox seleccionado

        print("Cantante seleccionada: "+cantante_seleccionada)
        print(f"Formato seleccionado: {cantante_seleccionada}")
        print("Opción escogida "+str(opcion_escogida))
        print(f"Opcion escogida: {opcion_escogida}")


    def on_anadirLista_toggled(self):
        if self.checkBoton2.isChecked():
            texto = self.checkBoton2.text()
            if texto:
                self.modelo.musica.append(texto)
                self.modelo.layoutChanged.emit()



if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    aplicacion.exec()