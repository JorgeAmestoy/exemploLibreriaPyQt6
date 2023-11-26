<p align="center"><b><font size="7">PROPIEDADES PYQT6</font></b></p>

----------------------------------

# INICIO
[WIDGETS](#widgets)<br>
[LAYOUTS](#layouts)<br>
[MÉTODOS](#metodos)<br>
[PERSONALIZAR](#personalizar)<br>
[OTROS](#otros)<br>

----------------------------------

## WIDGETS

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
En **checkBox** puedes activar y desactivar pulsando en este mismo. Sin embargo, en radioButton, para
desactivar, por ejemplo, el A, tienes que pulsar el B.
```
self.checkBox = QCheckBox ("Boton 1")
self.checkBox.toggled.connect(self.on_chkBoton1_toggled)
```
--------------------------
**RADIO BUTTON**<br>
El *containerV2* simplemente hace referencia al layout en el que está metido. No tiene una función más allá que esa.
```
self.radioButton = QRadioButton("Opción 1", containerV2)
self.radioButton.toggled.connect (self.on_radioButton_toggled)
```
--------------------------

**COMBOBOX**<br>
Es el desplegable. Se considera Widget:<br>
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
Si pusiese `listaTareas =[]` no me saldría nada. Con `[None]`, al añadir una nueva tarea, me la pone como segunda, es decir, cuantifica como elemento vacío.
```
listaTareas = [(True,"Primera tarea"),(False,"Segunda tarea")]# Creo ejemplo de lista siguiendo el modelo que quiero que siga dicha lista creado en el Data
modelo = ModeloLista(listaTareas)  # Creo objeto QAbstractListModel con el ejemplo creado anteriormente. Lo guardo en una variable.
lista = QListView()# Creo objeto QListView
lista.setModel(modelo)# Añado el modelo al objeto QListView
cajaV1.addWidget(lista)# Añado el widget recién creado a la caja vertical
```

``listaTareas = [(True,"Primera tarea"),(False,"Segunda tarea")]``: Cada elemento de la lista será una tupla que contiene dos elementos(Booleano y String). Podría haberlo dejado vacío pero de esta manera saldrán estas dos tareas de forma predeterminada.<br>
Uso **lista.setModel(modelo)** para añadir el modelo que quiero usar en la lista.

----------------------------

#### QFRAME <br>
El frame se considera **Widget**:

```
frame = QFrame() # Creo marco
frame.setFrameStyle(QFrame.Shape.Box) # Establezco la forma del marco en rectángulo
frame.setLayout(caixa5) # Añado el layout horizontal (caixa5) al marco
frame.setWindowTitle("Opcións de reproducción") # Pongo supuesto título del marco
caixaH2.addWidget(frame) # Añado a otro layout el marco con la caja dentro
```

------------------------------

#### QGROUPBOX<br>
El groupBox es como el **Frame** pero puedes añadir un título.<br>
También se considera **Widget**.
```
groupBox = QGroupBox("Opcion de reproduccion")# Creo QGroupBox
cajaH2.addWidget(groupBox)# Lo añado a la caja horizontal
grid2 = QGridLayout()# Creo layout (en este caso, grid) para añadirlo al groupBox
groupBox.setLayout(grid2)# Añado el layout al groupBox
self.checkBoton2 = QCheckBox("Asincrono")# Creo botón (widget)
grid2.addWidget(self.checkBoton2,0,0,1,1)# Añado el widget al grid
```

----------------------------

#### QTABWIDGET
Los tabs son las pestañas. Para añadirlas usamos: `.addTab()`.<br>
Así, en la firma del método (o en el error al ejecutar), me pone que es obligatorio pasar como parámetros
un widget y un String de forma **Optional**, por lo que en caso de no usarlo debemos escribir
**None**. Este String es el nombre que aparecerá en cada pestaña en la interfaz.
```
tabs = QTabWidget()
tabs.setTabPosition(QTabWidget.TabPosition.South)# Las coloca en la parte inferior
tabs.setMovable(True)# Para que el usuario pueda cambiar el orden de las pestañas arrastrándolas en la propia interfaz.

miTupla = ("red", "green", "blue", "yellow")
for color in miTupla:
   tabs.addTab(CajaColor(color), color) # Agrega pestaña al QTabWidget con el contenido de CajaColor(Color), un widget, y el texto que aparecerá.
```
Al final de todo no haría falta meterlo en un container, porque esta ya es en sí un widget. Sería:
```
self.setCentralWidget(tabs)
self.show()
```
------------------------------

#### CONTENEDOR PRINCIPAL
La QMainWindow se considera Widget. Así, cuando hago el `self.setCentralWidget(container)` añado el contenedor(Widget), que es el conjunto de cajas/layouts ordenados, en el widget de la
QMainWindow.
```
container = QWidget() # Creo contenedor
container.setLayout(cajaVertical) # Añado un layout al contenedor
self.setCentralWidget(container) # Añado el contenedor (widget) con todos los layouts ordenados al widget de la Main para mostrar
```

-------------------------------------

## LAYOUTS

[Volver arriba](#inicio)</sup>

---------------------
**QVBOXLAYOUT**<br>
Añado los widgets creados (etiquetas, botones..) a un layout (distribuidor de widgets). En este caso, uno que me los ordena de forma vertical, unos debajo de otros.
```
cajaV = QVBoxLayout()
cajaV.addWidget(etiqueta) 
cajaV.addWidget(etiqueta2) 
cajaV.addWidget(boton)
cajaV.addWidget(self.txtCaja)
# PONER EL SELF SI LO VOY A USAR EN LA FUNCIÓN!!!
```
---------------------------
**QHBOXLAYOUT**<br>
Añado los widgets creados (etiquetas, botones..) a un layout (distribuidor de widgets). En este caso, uno que me los ordena de forma horizontal, unos debajo de otros.
```
cajaH = QHBoxLayout()
cajaH.addWidget(etiqueta) 
cajaH.addWidget(etiqueta2) 
cajaH.addWidget(boton)
cajaH.addWidget(self.txtCaja) 
# PONER EL SELF SI LO VOY A USAR EL BOTÓN, CAJA DE ENTRADA... EN LA FUNCIÓN!!!
```
---------------------------

**QGRIDLAYOUT** (ejemploGridLayout)
```
grid = QGridLayout()
grid.addWidget(etiqueta)
grid.addWidget(etiqueta2,0,0,2,3)
grid.addWidget(boton,2,0,1,2)
```
------------------------------------

**QSTACKEDLAYOUT**(ejemploQStackedLayout)<br>
La tarjeta es lo que va a cambiar dependiendo del botón al que pulse.<br>
Se consideran Layouts.
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
Primero creas el obeto tipo QWidget. Añades la caja horizontal (HBoxModificado()), lleva
los **paréntesis ()** porque estoy llamando a una clase/método que me devuelve dicha
caja horizontal, sino iría sin paréntesis, como siempre.
Por último, añades dicho widget(el cual contiene la caja horizontal)a la tarjeta.
```
self.tarjetas.setCurrentIndex(0)
```

El `self.tarjetas.setCurrentIndex(0)`indica la referencia de la tarjeta. Esta referencia se obtiene
del índice de cada una. Este índice se asocia a la tarjeta según el orden de escritura del código tras añadir
los widgets a la tarjeta (`self.tarjetas.addWidget(widgetBox)`).
------------------------------------


## PERSONALIZAR

[Volver arriba](#inicio)</sup>

--------------------------------
#### ESTABLECER EL NOMBRE DE LA VENTANA PRINCIPAL
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
## METODOS

[Volver arriba](#inicio)</sup>

---------------------------------------

### MÉTODO INIT DE CAJACOLOR
```
class CajaColor(QWidget):
    def __init__(self,color):# Inicializo con un constructor que recibirá por parámetro un color
        super().__init__()
        self.setAutoFillBackground(True) # Rellenar el fondo de un color
        paleta = self.palette() # Obtiene la paleta de colores actual asociada al widget QWidget(QMinWindow es un Widget también).
        paleta.setColor(QPalette.ColorRole.Window, QColor(color))# Establezco el color de fondo de la ventana
        self.setPalette(paleta)#  Aplica la paleta de colores actualizada al widget, lo que incluye el nuevo color de fondo configurado.
```
`cajaV.addWidget(CajaColor("red"))`. Estoy utilizando
la clase CajaColor como si fuese un widget, ya que al CajaColor hereda de la súper clase
**QWidget** y al crear una instancia, estoy obteniendo un objeto que se comporta como un widget.
Luego, en `paleta.setColor(QPalette.ColorRole.Window, QColor(color))` digo que el color que voy añadir en la paleta
será en que escriba en la instancia del objeto de esta clase, pues en el constructor puse como parámetros
el self y el color. Entonces, cuando llame a dicha clase tengo que escribir el color: (`CajaColor("blue")`).
-----------------------------------

### MÉTODO DATA DE EJEMPLOQLISTVIEW
Obligatorio usar el `def rowCount(self,indice)` aunque no lo utilice. En caso contrario, no funciona.
```
def data(self, indice, rol):

    if (rol == Qt.ItemDataRole.DisplayRole):# En caso de que el rol sea el de visualización del ítem, en este caso, un texto visible...:
        _, texto = self.tareas[indice.row()] # Accede al elemento de la lista (self.tareas) correspondiente a la posición indicada por el índice de fila (indice.row()). Se asume que cada elemento es una tupla con al menos dos elementos: un estado y un texto. Recogemos una fila y nos da el estado y el texto, y solo nos interesa el texto. ASi data nos devuelve el texto que metamos en tarefas.
        return texto # Devuelve el texto de la tarea

    if (rol ==Qt.ItemDataRole.DecorationRole): # Verifica si es una imagen: En caso de que lo sea..:
        estado,_ = self.tareas[indice.row()] # EL guion significa que no le ponemos nombre a la variable. Aqui solo pondremos el estado aunque trabajemos en una tupla de dos. LO mismo en el de arriba.
        #Barrabaja es porque decimos que vamos a trabajar con una tupla de dos elementos pero que solo vamos a trabajar con uno, en este caso, el estado.
        if estado:# es como decir if estado is True:
           return tickImage

# SI NO LO PONGO NO FUNCIONA LA LISTA          
def rowCount(self, indice):
     return len(self.tareas)
```

`def data(self, indice, rol):` : Es un metodo que heredo de la clase padre QAbstractListModel, la cual recibe por parámetros un indice y un rol.
<br> El **indice** representa la posición de un item(empieza desde cero)
y el **rol** indica el tipo de datos que se está solicitando para el item en el índice dado:
- Texto Visible: *Qt.ItemDataRole.DisplayRole*
- Icono: *Qt.ItemDataRole.DecorationRole*
- Texto para edición: *Qt.ItemDataRole.EditRole* (este iría dentro de un método distinto, el **setData**)
<br>

` if (rol == Qt.ItemDataRole.DisplayRole):`: En caso de que el rol
sea del tipo texto visible haz lo siguiente:

`estado, texto = self.tareas[indice.row()]:` Accede al elemento de la lista (self.tareas) correspondiente a la posición indicada por el índice de fila (indice.row()). 
Se asume que cada elemento es una tupla con al menos dos elementos: un estado y un texto.<br>

`return texto:` Devuelve el texto de la tarea. En este contexto, significa que cuando se solicita el dato para la visualización de un ítem, se proporciona el texto asociado con ese ítem.

---------------------------------
### MÉTODO ROWCOUNT()
```
def rowCount(self, indice):
    return len(self.tareas)
```
Es **OBLIGATORIO**. Nos dice el número total de filas, es decir, de items(en este caso, tareas).
Es un método abstracto e interno, es decir, aunque yo no lo use como tal, cuando uso el 
QListView() para llamar al modelo, se utiliza para que sepa con qué trabajar y cómo hacerlo. En este caso, necesita
contar las filas. Si en vez de una lista estuviese trabajando con una base de datos, usaría otra función.

----------------------------------------------

## OTROS

[Volver arriba](#inicio)</sup>

**LAYOUTS Y CONTAINERS** (ejemploCheckBoxRadio)
```
cajaV2 = QVBoxLayout()# Creo caja vertical2
containerV2 = QWidget()# Creo contenedor
containerV2.setLayout(cajaV2)# Añado la caja vertical 2 al contenedor
cajaV1.addWidget(containerV2)#Añado el contenedor con la cajaV2 a la caja vertical 1

cajaV3 = QVBoxLayout()
cajaV1.addLayout(cajaV3)
```
**Los contenedores son considerados widgets**. Así: <br>
Añadir layout/caja al contenedor: `containerV2.setLayout(cajaV2)`<br>
Añadir contenedor al layout/caja: `cajaV1.addWidget(containerV2)`<br>
Añadir layout/caja al layout/caja: `cajaV1.addLayout(cajaV3)`