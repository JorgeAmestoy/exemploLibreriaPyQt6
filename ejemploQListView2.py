import sys

from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

tickImage = QImage('cheque.png')

class ModeloLista(QAbstractListModel):

    def __init__(self, tareas=None):
        super().__init__()
        self.tareas = tareas or []

    def data(self, indice, rol):
        if(rol==Qt.ItemDataRole.DisplayRole):
            _, texto = self.tareas[indice.row()]
            return texto

        if(rol==Qt.ItemDataRole.DecorationRole):
            estado,_ = self.tareas[indice.row()]
            if estado:
                return tickImage

    def setData(self, indice, valor, rol=Qt.ItemDataRole.EditRole):
        if rol == Qt.ItemDataRole.EditRole:
            # Aquí manejas la lógica para editar los datos.
            # Por ejemplo, puedes actualizar el valor de la tarea.
            _, texto_actual = self.tareas[indice.row()]
            self.tareas[indice.row()] = (False, valor)

            # Notificas a las vistas que los datos han cambiado.
            self.dataChanged.emit(indice, indice)
            return True

        return False

    def rowCount(self, indice):
        return len(self.tareas)


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mi primera aplicacion")

        cajaV1 = QVBoxLayout()



        listaTareas = [(True,"Primera tarea"),(False,"Segunda tarea")]# Creo ejemplo de lista siguiendo el modelo creado en el Data
        self.modelo = ModeloLista(listaTareas)  # Creo objeto QAbstractListModel con el ejemplo anterior. Establezco el modelo que va a tomar la lista.
        self.lista = QListView()# Creo objeto QListView
        self.lista.setModel(self.modelo)# Añado el modelo que va a tener la lista al objeto QListView
        self.lista.setSelectionMode(QListView.SelectionMode.MultiSelection)
        cajaV1.addWidget(self.lista)# Añado el widget recién creado a la caja vertical

        cajaH1 = QHBoxLayout()
        cajaV1.addLayout(cajaH1)
        botonBorrar = QPushButton("Borrar")
        botonBorrar.pressed.connect(self.on_botonBorrar_pressed)
        cajaH1.addWidget(botonBorrar)
        botonHecho = QPushButton("Hecho")
        botonHecho.pressed.connect(self.on_botonHecho_pressed)
        cajaH1.addWidget(botonHecho)

        self.txtCaja = QLineEdit()
        cajaV1.addWidget(self.txtCaja)

        botonAnadir = QPushButton("Añadir Tarea")
        botonAnadir.pressed.connect(self.on_botonAnadir_pressed)
        cajaV1.addWidget(botonAnadir)

        botonEditar = QPushButton("Editar tarea")
        botonEditar.clicked.connect(self.on_editarLista_clicked)
        cajaV1.addWidget(botonEditar)


        container = QWidget()
        container.setLayout(cajaV1)  # Añadir layout principal
        self.setFixedSize(400,400)
        self.setCentralWidget(container)
        self.show()

    def on_botonAnadir_pressed(self):
        texto = self.txtCaja.text().strip()  # Obtener el texto de la entrada y eliminar espacios (strip) al inicio y al final.
        if texto:  # Si obtengo algo de la caja de texto..:
            self.modelo.tareas.append((False,texto))  # Agrega una nueva tarea al final. Append añade elementos al final de la lista.
            self.modelo.layoutChanged.emit()  # Para actualizar la presentación de la lista y reflejar los cambios (añadir tarea, eliminar..)
            self.txtCaja.setText("")  # Limpiar el campo de entrada de la tarea después de agregarla

    def on_botonBorrar_pressed(self):
        indices = self.lista.selectedIndexes()
        if indices:
            for indice in sorted(indices,reverse=True):
                del self.modelo.tareas[indice.row()]
            self.modelo.layoutChanged.emit()
            self.lista.clearSelection()

    def on_botonHecho_pressed(self):
        indices = self.lista.selectedIndexes()  # Obtenemos los indices de los elementos seleccionados
        if indices:
            for indice in indices:  # Recorro los indices y los voy guardando en la varibale indice
                estado, texto = self.modelo.tareas[indice.row()]  # En cada índice, guarda el contenido en estado y texto
                self.modelo.tareas[indice.row()] = (True, texto)  # Cambio el estado a true
            # self.modelo.tareas[indice.row()] = (True, self.modelo.tareas[indice.row()][1]). Otra forma de escribir las dos lineas de arriba
            self.modelo.dataChanged.emit(indice, indice)  # Para actualizar la vista de cambios específicos en evz de algo más genérico
            self.lista.clearSelection()  # Para evitar que queden elementos seleccionados

    def on_editarLista_clicked(self):
        texto = self.txtCaja.text().strip()
        indices = self.lista.selectedIndexes()
        if indices:
            for indice in indices:
                ##estado, texto = self.modelo.tareas[indice.row()]
                self.modelo.tareas[indice.row()] = (False, texto)
                self.modelo.dataChanged.emit(indice,indice)
                self.lista.clearSelection()
                self.txtCaja.setText("")


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    aplicacion.exec()