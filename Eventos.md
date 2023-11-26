<p align="center"><b><font size="7">EVENTOS DE BOTONES</font></b></p>



-----------------------------
# INICIO

[CLICKED](#clicked)<br>
[RETURN_PRESSED(caja de texto)](#return-pressed)<br>
[TOGGLED(radioButton/checkBox)](#toggled)<br>
[PRESSED(listas)](#pressed)<br>
[VALUE_CHANGED(sliders)](#value-changed)<br>
[ACTIVATED](#activated)<br>
[OTROS](#otros)

-----------------------------

## CLICKED

-------------------------------

### MÉTODO QUE AL HACER CLICK EN BOTÓN APARECE UN TEXTO EN UNA ETIQUETA
(PrimeraVentana.py)
```
#EN LA LLAMADA AL MÉTODO NO SE PONEN PARÉNTESIS
#PONER SELF
botonSaludo = QPushButton("Saludo")
botonSaludo.clicked.connect(self.on_botonSaludo_clicked)

#MÉTODO 
def on_botonSaludo_clicked(self):
    self.lblEtiqueta1.setText("Hola companheros!!!")
```

---------------------------------------

### MÉTODO QUE AL HACER CLICK EN BOTÓN ESCRIBE EL TEXTO DE LA CAJA DE TEXTO EN UNA ETIQUETA
(SegundaVentana.py)
```
#EN LA LLAMADA AL MÉTODO NO SE PONEN PARÉNTESIS
#PONER SELF

self.txtCaja.clicked.connect(self.on_boton_clicked)
# Otra forma
#self.txtCaja.editingFinished.connect(self.on_boton_clicked)

def on_boton_clicked(self):
    saludo = self.txtCaja.text()
    self.lblEtiqueta1.setText(saludo)
```

---------------------------------------
## RETURN PRESSED
[Volver arriba](#inicio)</sup>

--------------------------------------

### MÉTODO QUE AL PUSAR ENTER EN LA CAJA DE TEXTO ESCRIBE TEXTO EN UNA ETIQUETA
(SegundaVentana.py)
```
#EN LA LLAMADA AL MÉTODO NO SE PONEN PARÉNTESIS
#PONER SELF

self.txtCaja.returnPressed.connect(self.on_txtCaja_enter)
# Otra forma
#self.txtSaludo.editingFinished.connect(self.on_txtCaja_enter)

def on_txtCaja_enter(self):
    saludo = self.txtCaja.text()
    self.lblEtiqueta1.setText(saludo)
```
--------------------------------------------

## TOGGLED
[Volver arriba](#inicio)</sup>

---------------------------------------------
### MÉTODO QUE AL PULSAR CHECK_BOX IMPRIME POR PANTALLA QUÉ BOTÓN SE HA SELECCIONADO Y DESELECCIONADO<br>
(ejemploCheckboxRadio.py)<br>
Aquí usamos el método **isChecked()** del checkBox para realizar algo en caso de que se haya seleccionado dicho botón
```
#EN LA LLAMADA AL MÉTODO NO SE PONEN PARÉNTESIS
#PONER SELF 

self.checkBox = QCheckBox ("Boton 1")
Self.checkBox.toggled.connect(self.on_checkBox_toggled)

 def on_checkBox_toggled(self):
      if self.checkBox.isChecked():
          print ("Boton check seleccionado: ", self.checkBox.text())
      else:
          print("Boton check deseleccionado: ", self.checkBox.text())
```

--------------------------------------
### MÉTODO QUE AÑADE A LA LISTA UNA TAREA AL SELECCIONAR UN CHECK_BOX
(examenFormulario.py)
```
def on_anadirLista_toggled(self):
    if self.checkBox.isChecked():
       texto = self.checkBox2.text()
       if texto:
          self.modelo.musica.append(texto)
          self.modelo.layoutChanged.emit()
```

-----------------------------------------------

### MÉTODO QUE AL PULSAR RADIO_BUTTON IMPRIME POR PANTALLA QUÉ BOTÓN SE HA SELECCIONADO Y DESELECCIONADO<br>
(ejemploCheckboxRadio.py)
Igual que en el **CheckBox** aquí usamos el método **isChecked()** del radioButton para realizar algo en caso de que se haya seleccionado dicho botón

```
#EN LA LLAMADA AL MÉTODO NO SE PONEN PARÉNTESIS
#PONER SELF 

self.rbtRadioButton1 = QRadioButton("Opción 1", containerV2)
self.rbtRadioButton1.toggled.connect (self.on_rbtRadioButton1_toggled)

def on_radioButton_toggled(self):
    if self.radioButton.isChecked():
        print ("Boton check seleccionado: ", self.radioButton.text())
    else:
        print("Boton check deseleccionado: ", self.radioButton.text())
```

------------------------------

## PRESSED

[Volver arriba](#inicio)</sup><br><br>
La diferencia entre **pressed** y **clicked** es que el primero se activa tan pronto como se presiona el botón, mientras que **clicked** requiere tanto la presión como la liberación del botón para activarse.



----------------------------
### MÉTODO QUE ME USA EL ÍNDICE DE CADA TARJETA DEL QSTACKEDLAYOUT<br>
(ejemploQStackedLayout.py)<br>
Así, cuando pulse el botón me aparecerá el contenido de la tarjeta[0]
```
def on_btnRojo_pressed(self):
     self.tarjetas.setCurrentIndex(0)
```

-----------------------------------------------

### MÉTODO QUE AÑADE UNA TAREA A UNA QLISTVIEW DESDE UNA CAJA DE TEXTO
(ejemploQListView2)
```
def on_btnAgregarTarea_pressed(self):
    texto = self.txtTarea.text().strip() # Obtener el texto de la entrada y eliminar espacios (strip) al inicio y al final.
    if texto: Verifica si la lista "texto" está vacía o no con un True o False. 
        self.modelo.tareas.append((False, texto)) # Agrega una nueva tarea al modelo con una marca de no completado (False) y el texto ingresado (la tupla). Append añade elemento(s) al final de la lista. Agrega una nueva tarea al modelo (que es la lista de tareas) y la manda como no completado (FALSE) y el texto ingresado. ESte eñ meotodo def data.
        self.modelo.layoutChanged.emit() # Emitir la señal para indicar cambios en el diseño del modelo. Le decimos al control que como hay datos nuevos, tiene que actualizarse.
        self.txtTarea.setText("") # Limpiar el campo de entrada de la tarea después de agregarla
```
Para empezar, **modelo** es un objeto que he creado de tipo QAbstractListModel, por lo que tiene métodos, señales... asociados a los que puedo llamar por herencia.<br><br>
`texto = self.txtTarea.text().strip()`: Obtengo el texto escrito en la caja de texto y lo guardo en la variable texto. Con el **strip()** elimino posibles espacios en blanco
que el user puede escribir al principio y al final y evitar errores.<br><br>
`if texto`: si guardo algo en la variable texto haz lo siguiente:<br><br>
`self.modelo.tareas.append((False, texto))`: uso el objeto *modelo* que instancié de QAbstractListModel, que contiene el modelo/la forma en la que va estructurada esta lista. Desde este objeto
llamo al atributo *tareas*(método init) con el que accedo a *append* para añadir elementos al final de la lista siguiendo el modelo de creación de dicha lista que hice en el método *data* de la clase *TareasModelo(QAbstractListModel)*, poniendo que "por defecto" va a ser
False y que el texto es lo que obtengo de la caja de texto.<br><br>
`self.modelo.layoutChanged.emit()`: Para actualizar la presentación de la lista y reflejar los cambios (añadir tarea, eliminar..)<br><br>
`self.txtTarea.setText("")`: Limpiar el campo de entrada de la tarea después de agregarla

----------------------------------------

### MÉTODO QUE AÑADE UNA TAREA A UNA QLISTVIEW AL SELECCIONAR UN CHECK_BOX
(examenFormulario.py)
```
def on_anadirLista_toggled(self):
    if self.checkBox2.isChecked():
       texto = self.checkBox2.text()
       if texto:
          self.modelo.musica.append(texto)
          self.modelo.layoutChanged.emit()
```

-------------------------------------
### METODO QUE BORRA TAREA(S) DE LA QLISTVIEW 
(ejemploQListView2)
```
   def on_btnBorrar_pressed(self):
       indices = self.lstTareas.selectedIndexes()# Obtenemos los elementos que el user ha marcado (devuelve una lista de objetos, no el índice)
       if indices: # Verifica si la lista "indices" está vacía o no con un True o False.
           for indice in sorted(indices, reverse=True): # Recorremos los indices en sentido inverso para evitar problemas al eliminar elementos. Así la va reccoriendo y guardando en índice el índice.
                del self.modelo.tareas[indice.row()]# Borramos el elemento correspondiente al indice
           self.modelo.layoutChanged.emit()# Para actualizar la vista
           self.lstTareas.clearSelection() # Para evitar que queden elementos seleccionados
```
`indices = self.lstTareas.selectedIndexes()`: Obtenemos los indices de los elementos que el usuario haya marcado.<br><br>
`if indices:`: Si encuentra algo en la variable indices haz lo siguiente:<br><br>
`for indice in sorted(indices, reverse=True):`: Esto crea una nueva lista ordenada a partir de la lista original indices. El argumento **reverse=True** indica que la ordenación se realizará en orden descendente. Esto significa que los elementos se ordenarán de mayor a menor. Esto
se hace para evitar problemas a la hora de eliminar un elemento de la lista. Así, la va recorriendo y guardando lo que en encuentra en la variable **índice**.<br><br>
` del self.modelo.tareas[indice.row()]`: Elimina el elemento correspondiente al índice de la lista tareas del modelo. **indice.row()** devuelve la fila del índice, y eso se utiliza para eliminar el elemento específico de la lista. <br><br>
`self.modelo.layoutChanged.emit()`: Para actualizar la presentación de la lista y reflejar los cambios (añadir tarea, eliminar..)<br><br>
`self.lstTareas.clearSelection()`: Para evitar que queden elementos seleccionados


-----------------------------------------

### MÉTODO QUE EDITA EL TEXTO DE UNA TAREA
(ejemploQListView2)

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

-------------------------------------------------


### MÉTODO QUE DICE SI TAREA SE HA HECHO O NO
(ejemploQListView2)
```
def on_btnHecho_pressed(self):
    indices = self.lstTareas.selectedIndexes()# Obtenemos los indices de los elementos seleccionados
    if indices: # Verifica si la lista indices está vacía o no con un True o False.
       for indice in indices: # Recorro los indices y los voy guardando en la varibale indice
           estado,texto = self.modelo.tareas[indice.row()]# En cada índice, guarda el contenido en estado y texto
           self.modelo.tareas[indice.row()] = (True, texto) # Cambio el estado a true
           # self.modelo.tareas[indice.row()] = (True, self.modelo.tareas[indice.row()][1]). Otra forma de escribir las dos lineas de arriba
           self.modelo.dataChanged.emit(indice, indice) # Para actualizar la vista de cambios específicos en evz de algo más genérico
           self.lstTareas.clearSelection() # Para evitar que queden elementos seleccionados
```
`if indices:`: Si encuentra algo en la variable indices haz lo siguiente:<br><br>
`for indice in indices:`: recorre dicha variable y ve guardando los índices en la variable indice<br><br>
`estado,texto = self.modelo.tareas[indice.row()]`: Guardamos el contenido de la lista de cada índice, en este caso, el estado(true/false) y el texto<br><br>
`del self.modelo.tareas[indice.row()]`: Elimina el elemento correspondiente al índice de la lista tareas del modelo. indice.row() devuelve la fila del índice, y eso se utiliza para eliminar el elemento específico de la lista. <br><br>
`self.modelo.tareas[indice.row()] = (True, texto)`: Según el índice que se vaya encontrando durante el for, cambio el estado a True.<br><br>
`self.modelo.dataChanged.emit(indice, indice)`: Actualizo usando el *dataChanged* para notificar cambios específicos. El layout es para cambiar toda la lista, este en cambio, una parte de la lista.<br><br>
`self.lstTareas.clearSelection()`:Para evitar que queden elementos seleccionados

--------------------------------------------

## VALUE CHANGED

[Volver arriba](#inicio)</sup>

---------------------------------------------

### MÉTODO QUE DEVUELVE EL VALOR DEL SLIDER AL MOVERLO
(examenFormulario.py)
```
sliderVolumen.valueChanged.connect(self.on_mostrarVolumen_slider)

def on_mostrarVolumen_slider(self,valor):
    print("Valor del QSlider"+str(valor))
```
Cuando el valor del QSlider cambia, se emitirá la señal **valueChanged**, y esta señal está conectada al método **on_mostrarVolumen_slider**. Como resultado, cada vez que el usuario mueva el control deslizante del volumen, se llamará automáticamente al método **on_mostrarVolumen_slider** con el nuevo valor del deslizador como argumento.

-----------------------------------------------

## ACTIVATED

[Volver arriba](#inicio)</sup>

-------------------------------------------------
### MÉTODO QUE IMPRIME LO QUE SELECCIONO EN EL COMBOBOX<br>
(examenFormulario.py)<br>
En PyQt, la **señal activated** se emite cuando el usuario selecciona un elemento en el combo box.
```
self.combo1 = QComboBox()
self.combo1.addItems(["Britney","Lana","La Beyonsebe"])# Añado items al ComboBox
self.combo1.activated.connect(self.on_mostrarComboBox_activated)# Añado evento ACTIVATED a ComboBOX

def on_mostrarComboBox_activated(self, index):
     cantante_seleccionada = self.combo1.currentText()
     opcion_escogida = self.combo1.currentIndex()

     print("Cantante seleccionada: "+cantante_seleccionada)
     print(f"Formato seleccionado: {cantante_seleccionada}")
     print("Opción escogida "+str(opcion_escogida))
     print(f"Opcion escogida: {opcion_escogida}")
```
La línea `self.combo1.activated.connect(self.on_mostrarComboBox_activated)` establece una conexión entre la señal **activated** del objeto **combo1** (un QComboBox) y el método `on_mostrarComboBox_activated` de la instancia actual de la clase. Al conectar esta señal a un método, en este caso `on_mostrarComboBox_activated`, estás configurando la lógica que se ejecutará cuando el usuario marque una opción del combo.

-------------------------------
## OTROS

[Volver arriba](#inicio)</sup>

-------------------------------

#### CLASE CON MÉTODOS PARA SUBIR Y BAJAR ELEMENTOS EN UNA LISTA DE TIPO QLISTWIDGET
```
from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidget, QPushButton, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Crear instancias de los elementos de la interfaz
        self.listaMusica = QListWidget(self)
        self.btnSubir = QPushButton('Subir na lista', self)
        self.btnBaixar = QPushButton('Baixar na lista', self)

        # Crear el widget central
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Configurar el diseño de la ventana
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.listaMusica)
        layout.addWidget(self.btnSubir)
        layout.addWidget(self.btnBaixar)

        # Conectar botones a funciones correspondientes
        self.btnSubir.clicked.connect(self.subirItem)
        self.btnBaixar.clicked.connect(self.baixarItem)

        # Agregar algunos elementos de ejemplo a la lista
        self.listaMusica.addItems(['Canción 1', 'Canción 2', 'Canción 3'])

    def subirItem(self):
        # Obtener elementos seleccionados en la lista
        item_seleccionado = self.listaMusica.selectedItems()
        if item_seleccionado:
            for item in item_seleccionado:
                # Obtener el índice del elemento actual
                index = self.listaMusica.row(item)
                if index > 0:
                    # Tomar y mover el elemento hacia arriba
                    current_item = self.listaMusica.takeItem(index)
                    self.listaMusica.insertItem(index - 1, current_item.text())
                    self.listaMusica.setCurrentItem(current_item)
                    # Emitir señal y deseleccionar
                    self.modelo.layoutChanged.emit()
                    self.listaMusica.clearSelection()

    def baixarItem(self):
        # Obtener elementos seleccionados en la lista
        item_seleccionado = self.listaMusica.selectedItems()
        if item_seleccionado:
            for item in reversed(item_seleccionado):
                # Obtener el índice del elemento actual
                index = self.listaMusica.row(item)
                if index < self.listaMusica.count() - 1:
                    # Tomar y mover el elemento hacia abajo
                    current_item = self.listaMusica.takeItem(index)
                    self.listaMusica.insertItem(index + 1, current_item.text())
                    self.listaMusica.setCurrentItem(current_item)
                    # Emitir señal y deseleccionar
                    self.modelo.layoutChanged.emit()
                    self.listaMusica.clearSelection()

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

```