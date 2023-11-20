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
**BOTÓN**
```
boton = QPushButton("Pulsa")
```
--------------------------
**CAJA/BOX VERTICAL**<br>
Añado los widgets creados (etiquetas, botones..) a un layout (distribuidor de widgets). En este caso, uno que me los ordena de forma vertical, unos debajo de otros.
```
cajaVertical = QVBoxLayout() #Creo caja vertical
cajaVertical.addWidget(etiqueta) # Añado etiqueta a la caja
cajaVertical.addWidget(etiqueta2) # Añado otra etiqueta a la caja
cajaVertical.addWidget(boton) # Añado botón a la caja
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
**CAJA DE TEXTO**<br>
Área de entrada de texto donde usuario puede escribir o editar texto.
```
txtCaja = QLineEdit()
```
**LISTA**
```
lstTareas = QListView() # Creo una lista para el front
lstTareas.setModel(self.modelo)
cajaV.addWidget(lstTareas)# Añado el QListView al layout vertical
```

```

```

```

```



```

```


```

```