# WIDGETS

<br>

-------------------------

**TITULO DE LA VENTANA PRINCIPAL**
```
self.setWindowTitle("Mi primera aplicacion")
```
----------------
**ETIQUETA NORMAL**
```
 etiqueta = QLabel("Esto es increíble!!")
```
-------------------
**ETIQUETA CON FOTO**
```
etiqueta2 = QLabel()
etiqueta2.setPixmap(QPixmap("fotoluci2.jpg"))
```
--------------------------
**CAJA DE TEXTO**<br>
Área de entrada de texto donde usuario puede escribir o editar texto.
```
txtCaja = QLineEdit()
```
--------------------------
**BOTÓN**
```
boton = QPushButton("Pulsa")
boton.clicked.connect(self.on_btnSaludar_clicked)
# control - señal - connect: siendo control el botón, caja de text..
# la señal el evento (clciked, pressed..) y connect para el método
```
--------------------------
**CHECK BOX**
```
self.chkBoton1 = QCheckBox ("Boton 1")
self.chkBoton1.toggled.connect(self.on_chkBoton1_toggled)
```
--------------------------
**RADIO BUTTON**
```
self.rbtRadioButton1 = QRadioButton("Opción 1", containerV2)
self.rbtRadioButton1.toggled.connect (self.on_rbtRadioButton1_toggled)
```
--------------------------

**LISTA**
```
lstTareas = QListView() # Creo una lista para el front
lstTareas.setModel(self.modelo)
cajaV.addWidget(lstTareas)# Añado el QListView al layout vertical
```
----------------------------
**CAJA/BOX VERTICAL**<br>
Añado los widgets creados (etiquetas, botones..) a un layout (distribuidor de widgets). En este caso, uno que me los ordena de forma vertical, unos debajo de otros.
```
# SI AÑADO A LA UN CONTENEDOR .addWidget, si añado una caja .addLayout
cajaVertical = QVBoxLayout() #Creo caja vertical
cajaVertical.addWidget(etiqueta) # Añado etiqueta a la caja
cajaVertical.addWidget(etiqueta2) # Añado otra etiqueta a la caja
cajaVertical.addWidget(boton) # Añado botón a la caja
cajaVertical.addWidget(self.txtCaja) # Añado botón a la caja
# PONER EL SELF SI LO VOY A USAR EN LA FUNCIÓN!!!
```
---------------------------
**CAJA/BOX HORIZONTAL**<br>
Añado los widgets creados (etiquetas, botones..) a un layout (distribuidor de widgets). En este caso, uno que me los ordena de forma vertical, unos debajo de otros.
```
cajaHorizontal = QHBoxLayout() #Creo caja Horizontal
cajaHorizontal.addWidget(etiqueta) # Añado etiqueta a la caja
cajaHorizontal.addWidget(etiqueta2) # Añado otra etiqueta a la caja
cajaHorizontal.addWidget(boton) # Añado botón a la caja
cajaHorizontal.addWidget(self.txtCaja) # Añado botón a la caja
# PONER EL SELF SI LO VOY A USAR EL BOTÓN, CAJA DE ENTRADA... EN LA FUNCIÓN!!!
```
---------------------------
**CONTENEDOR**<br>
Añado el layout(cajaVertical) al contenedor final, es decir, al Widget base de la ventana, sobre el que va a estar todo el contenido(layouts, botones..)
```
container = QWidget() # Creo contenedor
container.setLayout(cajaVertical) # Añado un layout al contenedor
self.setCentralWidget(container) # Mostrar el contenedor y su contenido en el área central de la ventana
```
Sin el `self.setCentralWidget(container)` no se vería en la ventana todo lo que he metido en ella al ejecutar.

----------------------------
**ESTABLECER EL TAMAÑO FIJO DE LA VENTANA**
Siendo width (anchura, eje x, horizontal) y height(altura, eje y, vertical)
```
self.setFixedSize(400, 400)
```

**CAMBIAR TAMAÑO DE LA LETRA**
```
fuente = self.lblEtiqueta1.font()
fuente.setPointSize(30)
self.etiqueta.setFont(fuente)
```
------------------------------------

```

```
-------------------------------------

# EVENTOS

---------------------------------------

**USAR INTRO EN LA CAJA DE TEXTO**
```
self.txtCaja.returnPressed.connect(self.on_btnSaludar_clicked)
```
El returnPressed nos sirve para hacer algo cuando presionamos intro, en este caso,
llamamos a la función `self.on_btnSaludar_clicked`, la cuál nos sirve
para cambiar el contenido de la etiqueta según lo que escribamos en la caja de texto.

-------------------------------------

# FUNCIONES

---------------------------------------

**CAMBIAR EL CONTENIDO DE LA ETIQUETA POR LO QUE ESCRIBAMOS EN LA CAJA DE TEXTO**
```
def on_botonSaludo_clicked(self):
     saludo = self.txtSaludo.text() # Guardamos el contenido de la caja de texto en una variable
     self.lblEtiqueta1.setText(saludo) # Añadimos dicho contenido de la variable en la etiqueta
```

```


```

```