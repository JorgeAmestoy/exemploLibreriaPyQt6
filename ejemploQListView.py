import sys
import typing


from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout,
                            QWidget, QListView, QHBoxLayout, QLineEdit)
from PyQt6.QtCore import Qt, QAbstractListModel




# Clase TareasModelo que hereda propiedades de QAbstractListModel. Hereda funcionalidades para trabajar con una lista
class TareasModelo(QAbstractListModel):


   # Constructor de TareasModelo que recibe parámetro OPCIONAL tareas e inicializa la clase Padre QAbstractListModel
   def __init__(self, tareas=None):
       super().__init__()
       self.tareas = tareas or [] # Asigno a self.tareas (atributo llamado tareas de la instancia clase, al ser Python este atributo no se declara) una tarea que escriba luego o ninguna si no escribo nada o ninguna si escribo None sin ""


   # Método que heredo de la clase Padre QAbstractListModel que tiene indice del item y el tipo de dato. HAy varios tipos de rol. Usamods displayRole, el cual renderiza lo que le devuelve la funcion como un texto. DecotarionRole, lo rendereiza pero como una IMAgen. EDitRole.
   def data(self, indice, rol):

       if (rol == Qt.ItemDataRole.DisplayRole):# En caso de que el rol sea el de visualización del ítem, en este caso, un texto visible...:
           estado, texto = self.tareas[indice.row()] # Accede al elemento de la lista (self.tareas) correspondiente a la posición indicada por el índice de fila (indice.row()). Se asume que cada elemento es una tupla con al menos dos elementos: un estado y un texto. Recogemos una fila y nos da el estado y el texto, y solo nos interesa el texto. ASi data nos devuelve el texto que metamos en tarefas.
           return texto # Devuelve el texto de la tarea


   # Método que también heredo de la clase Padre QAbstractListModel que me da el número total de filas(items)
   def rowCount(self, indice):
       return len(self.tareas) # Devuelve la cantidad de tareas en el modelo. La definicion del metodo pone que necesita un indice por eso lo ponemos obloigaotirmanete, aunque luego no lo usemos como se puede ver. Poniendo curso encima de rowCount aparecen los parametros obligatorios.


class VentanaPrincipal(QMainWindow):
   # Constructor de la clase e inicio clase Padre y esta misma
   def __init__(self):
       super().__init__()


       # Titulo de la ventana
       self.setWindowTitle("Ejemplo QListView con Qt")


       # Inicialización de la lista de tareas y el modelo
       listaTareas = [(False, 'Primera tarea'), (False, 'Segunda tarea')]# El false es el estado, lo otro es el texto. Podria haberlo dejaod vacio, estas van a salir siempre, añado una tarea nueva o no
       # Hago una instancia llamada modelo, de la clase TareasModelo, la cual tiene una lista cuyos elementos están formados por una tupla que me dice el estado y el texto
       self.modelo = TareasModelo(listaTareas)


       # Creo un layout de tipo Vertical
       cajaV = QVBoxLayout()


       # Configuración de la vista de lista y asignación del modelo
       self.lstTareas = QListView()# LE PONGO EL SELF PORQUE LO USO EN EL METODO DE ABAJO DE BTNBORRAR
       self.lstTareas.setModel(self.modelo)# Añado el modelo (instancia de la clase TareasModelo) al QListView
       cajaV.addWidget(self.lstTareas)# Añado el QListView al layout vertical


       # Configuración del diseño horizontal para botones
       cajaH = QHBoxLayout()
       btnBorrar = QPushButton("Borrar")
       btnBorrar.pressed.connect(self.on_btnBorrar_pressed)
       btnHecho = QPushButton("Hecho")
       cajaH.addWidget(btnBorrar)
       cajaH.addWidget(btnHecho)


       # Agrega el diseño horizontal al diseño vertical principal
       cajaV.addLayout(cajaH)


       # Configuración de la entrada de texto para agregar tareas
       self.txtTarea = QLineEdit()
       cajaV.addWidget(self.txtTarea)


       # Configuración del botón para agregar tareas y conexión al evento
       btnAgregarTarea = QPushButton("Añadir Tarea")
       btnAgregarTarea.pressed.connect(self.on_btnAgregarTarea_pressed)
       cajaV.addWidget(btnAgregarTarea)# Añado el boton al layout vertical


       # Configuración del contenedor principal y asignación como widget central
       container = QWidget()
       container.setLayout(cajaV)
       self.setCentralWidget(container)


       # Configuración del tamaño fijo de la ventana y visualización
       self.setFixedSize(400, 400)
       self.show()


   def on_btnAgregarTarea_pressed(self):
       texto = self.txtTarea.text().strip() # Obtener el texto de la entrada y eliminar espacios (strip) al inicio y al final.
       if texto: # Si obtengo algo de la caja de texto..:
           self.modelo.tareas.append((False, texto)) # Agrega una nueva tarea al modelo con una marca de no completado (False) y el texto ingresado (la tupla). Append añade elemento(s) al final de la lista. Agrega una nueva tarea al modelo (que es la lista de tareas) y la manda como no completado (FALSE) y el texto ingresado. ESte eñ meotodo def data.
           self.modelo.layoutChanged.emit() # Emitir la señal para indicar cambios en el diseño del modelo. Le decimos al control que como hay datos nuevos, tiene que actualizarse.
           self.txtTarea.setText("") # Limpiar el campo de entrada de la tarea después de agregarla


   def on_btnBorrar_pressed(self):
       indices = self.lstTareas.selectedIndexes()# COnseguimos a lista de los elementos seleccionados. Nos da uno o varios indices.
       if indices:
           for indice in indices: # Recorremos los indices en caso de haber encontrado varios.
               del self.modelo.tareas[indice.row()]# Borramos
           self.modelo.layoutChanged.emit()# Para actualizar la vista
           self.lstTareas.clearSelection() # Para cuando marques tarea que quieres eliminar, no quede seleccionado.


if __name__ == "__main__":
   aplicacion = QApplication(sys.argv)
   ventana = VentanaPrincipal()
   aplicacion.exec()
