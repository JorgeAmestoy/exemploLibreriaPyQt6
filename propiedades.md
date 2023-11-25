# WIDGETS

<br>

-------------------------

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
**PERSONALIZAR ETIQUETA**
```
etiqueta = QLabel("Soy una etiqueta")
etiqueta.setFixedSize(100,50)
etiqueta.setStyleSheet("background-color: yellow; color: black;")
```
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
**CHECK BOX**<br>
En checkBox puedes activar y desactivar en este mismo, en cambio en radioButton, para
desactivar, por ejemplo, el A, tienes que pulsar el B.
```
self.checkBox = QCheckBox ("Boton 1")
self.checkBox.toggled.connect(self.on_chkBoton1_toggled)
```
--------------------------
**RADIO BUTTON**
```
self.rbtRadioButton1 = QRadioButton("Opción 1", containerV2)
self.rbtRadioButton1.toggled.connect (self.on_rbtRadioButton1_toggled)
```
--------------------------

**COMBOBOX**<br>
El combo box se considera Widget:<br>
```
combo = QComboBox() # Creo QComboBox
grid.addWidget(combo,0,1,1,2)# Digo que el combo se va a añadir en la fila [0], columna[1], ocupando una fila y dos columnas
```
--------------------------

**QSLIDER**<br>
```
sliderVolumen= QSlider(Qt.Orientation.Horizontal)
grid2.addWidget(sliderVolumen, 1, 1, 1, 2)
```
--------------------------

**LISTA**

CAMBIAR TAMAÑO DE LA LISTA:
```
lswLista.setFixedSize(300,200)
```
CREAR LISTA: 
```
lstTareas = QListView() # Creo una lista
lstTareas.setModel(self.modelo) # Añado instancia de la clase Modelo para trabajar con la lista
cajaV.addWidget(lstTareas)# Añado el QListView al layout vertical # Añado la lista al layout
```
----------------------------


## LAYOUTS

---------------------
**QVBOXLAYOUT**<br>
Añado los widgets creados (etiquetas, botones..) a un layout (distribuidor de widgets). En este caso, uno que me los ordena de forma vertical, unos debajo de otros.
```
# SI AÑADO A LA CAJA UN CONTENEDOR .addWidget, si añado una caja .addLayout
cajaVertical = QVBoxLayout() #Creo caja vertical
cajaVertical.addWidget(etiqueta) # Añado etiqueta a la caja
cajaVertical.addWidget(etiqueta2) # Añado otra etiqueta a la caja
cajaVertical.addWidget(boton) # Añado botón a la caja
cajaVertical.addWidget(self.txtCaja) # Añado botón a la caja
# PONER EL SELF SI LO VOY A USAR EN LA FUNCIÓN!!!
```
---------------------------
**QHBOXLAYOUT**<br>
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

#### QGROUPBOX<br>
El groupBox se considera Widget:
```
frame = QGroupBox("Opcións de reproducción") # Creo marcon con titulo
frame.setLayout(caixa5) # Añado el layout (caixa5) al marco
caixaH2.addWidget(frame) # Añado a otro layout el marco con la caja dentro
```

----------------------------

#### QFRAME <br>
El frame se considera Widget:

```
frame = QFrame() # Creo marco
frame.setFrameStyle(QFrame.Shape.Box) # Establezco la forma del marco en rectángulo
frame.setLayout(caixa5) # Añado el layout horizontal (caixa5) al marco
frame.setWindowTitle("Opcións de reproducción") # Pongo supuesto título del marco
caixaH2.addWidget(frame) # Añado a otro layout el marco con la caja dentro
```
**QGRIDLAYOUT** (ejemploGridLayout)
```
grid = QGridLayout()
grid.addWidget(etiqueta)
grid.addWidget(etiqueta2,0,0,2,3)
grid.addWidget(boton,2,0,1,2)
```
------------------------------------

**QSTACKEDLAYOUT**(ejemploQStackedLayout)<br>
La tarjeta es lo que va a cambiar dependiendo del botón al que pulse.
```
self.tarjetas = QStackedLayout()
cajaVertical.addLayout(self.tarjetas)
```

A las tarjetas les añades widgets, por eso, si quieres como widget una caja horizontal tienes que:
```
widgetBox = QWidget()
widgetBox.setLayout(HBoxModificado())
self.tarjetas.addWidget(widgetBox)
```
Primero creas el obeto tipo QWidget. Añades la caja horizontal (HBoxModificado()), llevas
los **paréntesis ()** porque estoy llamando ana clase/método que me devuelve dicha
caja horizontal, sino iría sin paréntesis, como siempre.
Por último, añades dicho widget(el cual contiene la caja horizontal)a la tarjeta.
```
self.tarjetas.setCurrentIndex(0)
```

El `self.tarjetas.setCurrentIndex(0)`indica la referencia de la tarjeta. Esta referencia se obtiene
del índice de cada una. Este índice se asocia a la tarjeta según el órden de escritura del código tras añadir
los widgets a la tarjeta (`self.tarjetas.addWidget(widgetBox)`).
------------------------------------

#### QTABWIDGET
```
tabs = QTabWidget()
tabs.setTabPosition(QTabWidget.TabPosition.South)# Las coloca en la parte inferior
tabs.setMovable(True)# Para que el usuario pueda cambiar el orden de las pestañas arrastrándolas en la propia interfaz.
for color in miTupla:
   tabs.addTab(CajaColor(color), color) # Agrega pestaña al QTabWidget con el contenido de cajaColor(Color)
```
Al final de todo no haría falta meterlo en un container, porque esta ya es en sí,
un widget. Sería:
```
self.setCentralWidget(tabs)
self.show()
```
------------------------------

**CONTENEDOR**<br>
Añado el layout(cajaVertical) al contenedor final, es decir, al Widget base de la ventana, sobre el que va a estar todo el contenido(layouts, botones..)
```
container = QWidget() # Creo contenedor
container.setLayout(cajaVertical) # Añado un layout al contenedor
self.setCentralWidget(container) # Mostrar el contenedor y su contenido en el área central de la ventana
```
Sin el `self.setCentralWidget(container)` no se vería en la ventana todo lo que he metido en ella al ejecutar.
El contenedor es de tipo Widget.

-------------------------------------

# PERSONALIZAR

--------------------------------
ESTABLECER EL NOMBRE DE LA VENTANA PRINCIPAL
```
self.setWindowTitle("Mi primera aplicacion")
```
----------------
**ESTABLECER EL TAMAÑO FIJO DE LA VENTANA**<br>
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

#### ALINEAR EN LA PARTE SUPERIOR
```
caixa3.setAlignment(Qt.AlignmentFlag.AlignTop)
```
-------------------------------------
#### ALINEAR EN EL CENTRO
```
self.lblEtiqueta1.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
```
------------------------------------
#### HACER DESPLAZABLES LOS TABS
```
tabs.setMovable(True)
```
----------------------------
#### ESTABLECER LA POSICIÓN DE LOS TABS
```
tabs.setTabPosition(QTabWidget.TabPosition.South)
```

-------------------------------
# MÉTODOS

---------------------------------------

**MÉTODO INIT DE CAJACOLOR**
```
class CajaColor(QWidget):
    def __init__(self,color):
        super().__init__()
        self.setAutoFillBackground(True) # Rellenar el fondo de un color
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(paleta)
```
En esta clase, creo en el método init una función para poder colorear
los layouts(QVBox, GridLayout...).
Para usarlo lo hago así: `cajaV.addWidget(CajaColor("red"))`. Estoy utilizando
la clase CajaColor como si fuese un widget, ya que al CajaColor heredar de la súper clase
**QWidget** y al crear una instancia, estoy obteniendo un objeto que se comporta como un widget.
Luego, en `paleta.setColor(QPalette.ColorRole.Window, QColor(color))` digo que el color que voy añadir en la paleta
será en que escriba en la instancia del objeto de esta clase, pues en el constructor puse como parámetros
el self y el color. Entonces, cuando llame a dicha clase tengo que escribir el color: (`CajaColor("blue")`).
-----------------------------------
## OTROS
**LAYOUTS Y CONTAINERS** (ejemploCheckBoxRadio)
```
cajaV2 = QVBoxLayout()# Creo caja vertical2
containerV2 = QWidget()# Creo contenedor
containerV2.setLayout(cajaV2)# Añado la caja vertical 2 al contenedor
cajaV1.addWidget(containerV2)#Añado el contenedor con la cajaV2 a la caja vertical 1

cajaV3 = QVBoxLayout()
cajaV1.addLayout(cajaV3)
```
**Los contenedores son consideras widgets**. Así: <br>
Añadir layout/caja al contenedor: `containerV2.setLayout(cajaV2)`<br>
Añadir contenedor al layout/caja: `cajaV1.addWidget(containerV2)`<br>
Añadir layout/caja al layout/caja: `cajaV1.addLayout(cajaV3)`