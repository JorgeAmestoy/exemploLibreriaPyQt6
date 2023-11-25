# EVENTOS BOTONES

-----------------------------

### MÉTODO QUE AL HACER CLICK EN BOTÓN APARECE UN TEXTO EN UNA ETIQUETA(PrimeraVentana.py)
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

### MÉTODO QUE AL HACER CLICK EN BOTÓN ESCRIBE EL TEXTO DE LA CAJA DE TEXTO EN UNA ETIQUETA(SegundaVentana.py)
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

### MÉTODO QUE AL PUSAR ENTER EN LA CAJA DE TEXTO ESCRIBE TEXTO EN UNA ETIQUETA(SegundaVentana.py)
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

### MÉTODO QUE AL PULSAR CHECK_BOX IMPRIME POR PANTALLA QUE BOTÓN SE HA SELECCIONADO Y DESELECCIONADO(ejemploCheckboxRadio.py)<br>
Aquí usamos el método isChecked() del checkBox para realizar algo en caso de que se haya seleccionado dicho botón
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

-----------------------------------------------

### MÉTODO QUE AL PULSAR RADIO_BUTTON IMPRIME POR PANTALLA QUE BOTÓN SE HA SELECCIONADO Y DESELECCIONADO(ejemploCheckboxRadio.py)<br>
Aquí usamos el método isChecked() del checkBox para realizar algo en caso de que se haya seleccionado dicho botón

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

-----------------------------------------------

### MÉTODO QUE ME DEVUELVE EL ÍNDICE DE CADA TARJETA DEL QSTACKEDLAYOUT<br>
Así, cuando pulse el botón me aparecerá el contenido de la tarjet[0]
```
def on_btnRojo_pressed(self):
     self.tarjetas.setCurrentIndex(0)
```