from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *



import sys

class ModeloLista(QModelIndex):

    def __init__(self, info=None):
        super().__init__()
        self.info = info or []

    def data(self, indice, rol):
        if (rol == Qt.ItemDataRole.DisplayRole):  # En caso de que el rol sea el de visualización del ítem, en este caso, un texto visible...:
            nome, apellido, numero = self.info[indice.row()]  # Accede al elemento de la lista (self.tareas) correspondiente a la posición indicada por el índice de fila (indice.row()). Se asume que cada elemento es una tupla con al menos dos elementos: un estado y un texto. Recogemos una fila y nos da el estado y el texto, y solo nos interesa el texto. ASi data nos devuelve el texto que metamos en tarefas.
            return nome, apellido, numero


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Examen 12-12-2022")

        cajaV1 = QVBoxLayout()
        grid1 = QGridLayout()
        cajaV1.addLayout(grid1)
        etiquetaNome = QLabel("Nome")
        grid1.addWidget(etiquetaNome)
        self.txtCaja1 = QLineEdit()
        grid1.addWidget(self.txtCaja1,0,1,1,1)
        etiquetaTratamento = QLabel("Tratamento")
        grid1.addWidget(etiquetaTratamento,1,0,1,1)
        self.txtCaja2 = QLineEdit()
        grid1.addWidget(self.txtCaja2,1,1,1,1)
        etiquetaApellido = QLabel("Apellido")
        grid1.addWidget(etiquetaApellido,0,2,1,1)
        self.txtCaja3 = QLineEdit()
        grid1.addWidget(self.txtCaja3, 0,3,1,1) # CAJA APELLIDO
        etiquetaTelefono = QLabel("Telefono")
        grid1.addWidget(etiquetaTelefono,1,2,1,1)
        self.txtCaja4 = QLineEdit()
        grid1.addWidget(self.txtCaja4,1,3,1,1)
        etiquetaFormato = QLabel("Formato")
        grid1.addWidget(etiquetaFormato,2,0,1,1)
        comboBox = QComboBox()
        grid1.addWidget(comboBox,2,1,1,4)

       # CAJA HORIZONTAL 1
        cajaH1 = QHBoxLayout()
        cajaV1.addLayout(cajaH1)
        self.lista = QListWidget()# CREO LISTA
        cajaH1.addWidget(self.lista)

        # CAJA VERTICAL 2
        cajaV2 = QVBoxLayout()
        cajaV2.setAlignment(Qt.AlignmentFlag.AlignTop)
        cajaH1.addLayout(cajaV2)
        etiquetaCorreo = QLabel("Formato de correo:")
        cajaV2.addWidget(etiquetaCorreo)
        self.radioButton1 = QRadioButton("HTML")# RADIO BUTTON HTML
        self.radioButton1.toggled.connect(self.on_radioButton1_toggled)
        cajaV2.addWidget(self.radioButton1)
        self.radioButton2 = QRadioButton("Texto Plato")# RADIO BUTTON TEXTO PLATO
        self.radioButton2.toggled.connect(self.on_radioButton2_toggled)
        cajaV2.addWidget(self.radioButton2)
        self.radioButton3 = QRadioButton("Personalizado") # RADIO BUTTON PERSONALIZADO
        self.radioButton3.toggled.connect(self.on_radioButton3_toggled)
        cajaV2.addWidget(self.radioButton3)


        # CAJA HORIZONTAL 2
        cajaH2 = QHBoxLayout()
        cajaV1.addLayout(cajaH2)
        etiquetaDireccion = QLabel("Direccion de correo")
        cajaH2.addWidget(etiquetaDireccion)
        txtCaja5 = QLineEdit()
        cajaH2.setContentsMargins(0,0,100,0)
        cajaH2.addWidget(txtCaja5)
        cajaH2.setAlignment(Qt.AlignmentFlag.AlignLeft)

        # GRID 2
        grid2 = QGridLayout()
        cajaV1.addLayout(grid2)
        botonEngadir = QPushButton("Engadir")
        botonEngadir.clicked.connect(self.on_botonEngadir_clicked)
        grid2.addWidget(botonEngadir)
        botonEditar = QPushButton("Editar")
        botonEditar.clicked.connect(self.on_botonEditar_clicked)
        grid2.addWidget(botonEditar,0,1,1,1)
        botonBorrar = QPushButton("Borrar")
        grid2.addWidget(botonBorrar,0,2,1,1)
        botonDefecto = QPushButton("Por defecto")
        grid2.addWidget(botonDefecto,0,3,1,1)
        botonCancelar = QPushButton("Cancelar")
        botonCancelar.clicked.connect(self.on_botonCancelar_clicked)
        grid2.addWidget(botonCancelar,1,3,1,1)
        botonAceptar = QPushButton("Aceptar")
        grid2.addWidget(botonAceptar,1,4,1,1)


        container = QWidget()
        container.setLayout(cajaV1)  # Añadir layout principal
        self.setCentralWidget(container)
        self.setFixedSize(400,400)
        self.show()

    def on_botonCancelar_clicked(self):
        self.close()

    def on_radioButton1_toggled(self):
        if self.radioButton1.isChecked():
            print("RadioButton seleccionado: ", self.radioButton1.text())



    def on_radioButton2_toggled(self):
        if self.radioButton2.isChecked():
            print("RadioButton seleccionado: ", self.radioButton2.text())


    def on_radioButton3_toggled(self):
        if self.radioButton3.isChecked():
            print("RadioButton seleccionado: ", self.radioButton3.text())


    def on_botonEngadir_clicked(self):
        self.textoNome = self.txtCaja1.text()
        self.textoApellido = self.txtCaja3.text()
        self.textoNumero = self.txtCaja4.text()
        self.textoCompleto = self.textoNome +" "+ self.textoApellido +" "+ self.textoNumero

        self.lista.addItems([self.textoCompleto])
        self.txtCaja1.setText("")
        self.txtCaja3.setText("")
        self.txtCaja4.setText("")


    def on_botonEditar_clicked(self):
        item_seleccionado = self.lista.selectedItems()
        if item_seleccionado:
            for item in item_seleccionado:
                index = self.lista.row(item)
                if index ==0:
                    nomee = self.lista.currentItem().text()
                    self.txtCaja1.setText(nomee)
                elif index ==1:
                    apellido = self.lista.currentItem().text()
                    self.txtCaja3.setText(apellido)
                elif index == 2:
                    numero = self.lista.currentItem().text()
                    self.txtCaja4.setText(str(numero))








if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    aplicacion.exec()