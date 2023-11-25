import sys
import typing


from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout,
                            QWidget, QListView, QHBoxLayout, QLineEdit)
from PyQt6.QtCore import Qt, QAbstractListModel
from PyQt6.QtGui import QImage

tickImage = QImage('cheque.png')


# Clase que nos devuelve el modelo de una lista, es decir, cómo va a ser esta lista.
class TareasModelo(QAbstractListModel):


   # Constructor de TareasModelo que recibe parámetro OPCIONAL tareas e inicializa la clase Padre QAbstractListModel
   def __init__(self, tareas=None):
       super().__init__()
       self.tareas = tareas or [] # Asigno a self.tareas (atributo llamado tareas de la instancia clase, al ser Python este atributo no se declara) una tarea que escriba luego, ninguna si no escribo nada o también ninguna si escribo None sin "".


   # Método que heredo de la clase Padre QAbstractListModel que tiene indice del item y el tipo de dato. HAy varios tipos de rol. Usamods displayRole, el cual renderiza lo que le devuelve la funcion como un texto. DecotarionRole, lo rendereiza pero como una IMAgen. EDitRole.
   def data(self, indice, rol):

       if (rol == Qt.ItemDataRole.DisplayRole):# En caso de que el rol sea el de visualización del ítem, en este caso, un texto visible...:
           _, texto = self.tareas[indice.row()] # Accede al elemento de la lista (self.tareas) correspondiente a la posición indicada por el índice de fila (indice.row()). Se asume que cada elemento es una tupla con al menos dos elementos. Así, el barrabaja es porque decimos que vamos a trabajar con una tupla de dos elementos pero que solo vamos a trabajar con uno, en este caso, el texto.
           return texto # Devuelve el texto de la tarea

       if (rol ==Qt.ItemDataRole.DecorationRole): # Verifica si es una imagen: En caso de que lo sea..:
           estado,_ = self.tareas[indice.row()] #Barrabaja es porque decimos que vamos a trabajar con una tupla de dos elementos pero que solo vamos a trabajar con uno, en este caso, el estado.
           if estado:# es como decir if estado is True:
               return tickImage


   # Método que también heredo de la clase Padre QAbstractListModel que me da el número total de filas(items)
   def rowCount(self, indice): # La definicion del metodo pone que necesita un indice por eso lo ponemos obloigaotirmanete, aunque luego no lo usemos.
       return len(self.tareas) # Devuelve la cantidad de tareas en el modelo.
    # Metodo interno. Para que el modelo sepa con qué trabaja y cómo saber cuantas filas tiene.

class VentanaPrincipal(QMainWindow):
   # Constructor de la clase e inicio clase Padre y esta misma
   def __init__(self):
       super().__init__()


       # Titulo de la ventana
       self.setWindowTitle("Ejemplo QListView con Qt")


       # Creo una instancia de TareasModelo. Es como si dijese: int numero = 2; Y luego llamo a la clase y meto el numero.
       listaTareas = [(True, 'Primera tarea'), (False, 'Segunda tarea')]# El false es el estado, lo otro es el texto. Podria haberlo dejaod vacio, estas van a salir siempre, añado una tarea nueva o no
       # Hago una instancia llamada modelo, de la clase TareasModelo, la cual tiene una lista cuyos elementos están formados por una tupla que me dice el estado y el texto
       self.modelo = TareasModelo(listaTareas)#


       # Creo un layout de tipo Vertical
       cajaV = QVBoxLayout()


       # Configuración de la vista de lista y asignación del modelo
       self.lstTareas = QListView()# LE PONGO EL SELF PORQUE LO USO EN EL METODO DE ABAJO DE BTNBORRAR
       self.lstTareas.setModel(self.modelo)# Añado el modelo para que la QListView sepa cómo va a ser esta, qué datos mostrar..
       self.lstTareas.setSelectionMode(QListView.SelectionMode.MultiSelection) # Para poder seleccionar varias tareas (items). Hay que seleccionar en orden de abarjo para arriba.
       cajaV.addWidget(self.lstTareas)# Añado el QListView al layout vertical



       # Configuración del diseño horizontal para botones
       cajaH = QHBoxLayout()
       btnBorrar = QPushButton("Borrar")
       btnBorrar.pressed.connect(self.on_btnBorrar_pressed)
       btnHecho = QPushButton("Hecho")
       btnHecho.pressed.connect(self.on_btnHecho_pressed)
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
           self.modelo.tareas.append((False, texto)) # Agrega una nueva tarea al modelo con una marca de no completado (False) y el texto ingresado. Append añade elementos al final de la lista.
           self.modelo.layoutChanged.emit() # Para actualizar la presentación de la lista y reflejar los cambios (añadir tarea, eliminar..)
           self.txtTarea.setText("") # Limpiar el campo de entrada de la tarea después de agregarla


   def on_btnBorrar_pressed(self):
       indices = self.lstTareas.selectedIndexes()# Obtenemos los elementos que el user ha marcado
       if indices: # Si encuentra un indice..:
           for indice in sorted(indices, reverse=True): # Recorremos los indices en sentido inverso para evitar problemas al eliminar elementos. Así la va reccoriendo y guardando en índice el índice.
                del self.modelo.tareas[indice.row()]# Borramos el elemento correspondiente al indice
           self.modelo.layoutChanged.emit()# Para actualizar la vista
           self.lstTareas.clearSelection() # Para evitar que queden elementos seleccionados


   def on_btnHecho_pressed(self):
       indices = self.lstTareas.selectedIndexes()# Obtenemos los indices de los elementos seleccionados
       if indices:
           for indice in indices: # Recorro los indices y los voy guardando en la varibale indice
               estado,texto = self.modelo.tareas[indice.row()]# En cada índice, guarda el contenido en estado y texto
               self.modelo.tareas[indice.row()] = (True, texto) # Cambio el estado a true
              # self.modelo.tareas[indice.row()] = (True, self.modelo.tareas[indice.row()][1]). Otra forma de escribir las dos lineas de arriba
           self.modelo.dataChanged.emit(indice, indice) # Para actualizar la vista de cambios específicos en evz de algo más genérico
           self.lstTareas.clearSelection() # Para evitar que queden elementos seleccionados




#DIFERENCIA ENTRE PONER EL METODO () O SIN ()?
if __name__ == "__main__":
   aplicacion = QApplication(sys.argv)
   ventana = VentanaPrincipal()
   aplicacion.exec()
