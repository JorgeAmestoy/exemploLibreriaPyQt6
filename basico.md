```
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys
```
Se importan los módulos necesarios de PyQt6 y el módulo sys.

```
class MainWindow(QMainWindow):
    pass
```
Para empezar, en Python las clases y sus miembros son **públcos** por defecto.
<br>Así, aquí se define una nueva clase llamada **MainWindow** que hereda de **QMainWindow**. En este ejemplo, la clase está vacía (pass), lo que significa que no tiene ningún contenido adicional.
<br>La ventana predeterminada que se abre sin añadir ningún widget es por esta herencia.
```
window.show()
```
**IMPORTANTE**: Este método es para mostrar la ventana principal. Si no lo usamos **no** se ve nada.

-----------------------
**DEFINICIÓN DE CLASE**

```
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Crear una instancia de Persona
persona1 = Persona("Juan", 25)

```
En programación, un constructor es un método especial dentro de una clase que se llama automáticamente cuando se crea un objeto (una instancia) de esa clase. <br>En Python el constructor es así:  ```def __init__(self):``` .<br> Su propósito principal es realizar cualquier inicialización necesaria para el objeto.<br> 
Sería como darle la forma inicial y a seguir a la Persona con su nombre y edad.

El objeto es persona1. En la programación orientada a objetos, un objeto es una instancia de una clase. La clase Persona es como un "molde" que define la estructura y el comportamiento que tendrán las instancias de la clase Persona.<br>
La línea *persona1 = Persona("Juan", 25)* crea una instancia de la clase Persona y la asigna a la variable persona1.

Creo una clase Persona, es decir el molde de lo que será una persona.<br>
Todas las personas que vaya a crear tendrán obligatoriamente un nombre y una edad.<br>
Esto lo hago con el constructor, pues doy los valores iniciales y principales que va a tener la persona.<br>
Así, *persona1* sería un tipo de Persona con su nombre y su edad.
```
class Persona:
    def __init__(self, nombre, edad=None):
        self.nombre = nombre
        self.edad = edad
        
persona2 = Persona("María")
```
En este caso la **edad** es opcional, si creo una instancia de Persona sin la edad no daría error.

---------------------
**CONSTRUCTOR DE LA CLASE Y SÚPER CLASE DE LA MAIN**
```
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
```
Defino el método especial `__init__`, que es el constructor de la clase y
dentro de él llamo con `super()` al constructor de la clase Padre (QMainWindow)
que me da la ventana predeterminada de PyQt, a la que puedo añadirle widgets, etc.<br>
Si me fijo en los códigos, **todo lo que añado a la ventana lo hago dentro
del constructor.**

-----------------------
**MÉTODO SHOW**<br>
Puedo llamar al método *show()* o bien, dentro del
constructor de la ventana principal con `self.show()`,
o fuera de la clase con el objeto/variable llamado *ventana*, en la que creo una instancia de dicha clase
y al heredar de QMainWindow puedo usar el método *show()*.

---------------------------
**SELF**<br>
El self en Python se refiere a la instancia actual de la clase. Puedes pensar en él como una forma de referirte a sí mismo dentro de los métodos de una clase.

Cuando defines una clase en Python y creas un objeto (una instancia) de esa clase, el self se refiere a ese objeto específico. Dentro de los métodos de la clase, puedes usar self para acceder a los atributos y métodos de esa instancia particular.
```
class Persona:
    def __init__(self, edad):
        self.edad = edad

    def imprimir_edad(self):
        print(self.edad)

# Crear una instancia de la clase Persona
persona1 = Persona(25)

# Llamar a un método de la instancia
persona1.imprimir_edad()

```
Así, en el `self.edad = edad` del constructor `__init__`, estás asignando el valor que pasas al constructor (edad) al atributo edad (en Python no hace falta declararlos previamente) de la instancia de la clase (self.edad). Cada instancia de la clase Persona puede tener un valor diferente para edad.<br>
En resumen, digo que la edad que pase luego como argumento, sea la edad de la instancia en sí, es decir, que sea la edad de la clase Persona. Luego imprimo dicha "variable" con el `def imprimir_edad(self):
        print(self.edad)` .

----------------------

**TUPLAS**
```
# Definir una tupla
mi_tupla = (1, 'Hola', 3.14)

# Acceder a elementos de la tupla
primer_elemento = mi_tupla[0]  # 1
segundo_elemento = mi_tupla[1]  # 'Hola'
tercer_elemento = mi_tupla[2]  # 3.14

# Imprimir la tupla y algunos elementos
print("Tupla completa:", mi_tupla)
print("Primer elemento:", primer_elemento)
print("Segundo elemento:", segundo_elemento)
print("Tercer elemento:", tercer_elemento)

#Imprimir la tupla con for in
for elemento in mi_tupla:
    print(elemento)

```

**LISTA vs TUPLA**
```
mi_tupla = (1, 'dos', 3.0)

mi_lista = [1, 'dos', 3.0]
```

----------------------------------

#### ENUMERATE
```
frutas = ['manzana', 'plátano', 'uva']

# Usando enumerate para obtener índice y valor al mismo tiempo
for indice, fruta in enumerate(frutas):
    print(f"Índice: {indice}, Fruta: {fruta}")

DANDO COMO SALIDA:
Índice: 0, Fruta: manzana
Índice: 1, Fruta: plátano
Índice: 2, Fruta: uva

```
--------------------------------

**FOR IN**<br>
```
if indices:
    for indice in indices:
        print(f"Procesando el índice {indice.row()}")  # Imprime el número de fila del índice actual
        # Puedes realizar otras operaciones relacionadas con el índice aquí

# Código fuera del bucle
print("Fin del procesamiento")

```
Va itereando por todos los elementos de la lista indices y va guardando lo que encuentra en la variable indice.

----------------------------------
## EJEMPLOQLISTVIEW

-------------------------------

### MÉTODO DATA
```
 def data(self, indice, rol):
     # Verifica si el rol es el de visualización del ítem, en este caso, verifica si es texto
        if (rol == Qt.ItemDataRole.DisplayRole):
            # Obtiene el estado y el texto de la tarea en la posición dada por el índice
            estado, texto = self.tareas[indice.row()]
            return texto # Devuelve el texto de la tarea
```

`def data(self, indice, rol):` : Es un metodo que heredo de la clase padre QAbstractListModel, la cual recibe por parámetros un indice y un rol.
<br> El *indice* representa la posición de un item(empieza desde cero)
y el *rol* indica el tipo de datos que se está solicitando para el item en el índice dado:
- Texto Visible: *Qt.ItemDataRole.DisplayRole*
- Texto para edición: *Qt.ItemDataRole.EditRole*
- Icono: *Qt.ItemDataRole.DecorationRole*
<br>

` if (rol == Qt.ItemDataRole.DisplayRole):`: En caso de que el rol
sea del tipo texto visible haz lo siguiente:

`estado, texto = self.tareas[indice.row()]:` Accede al elemento de la lista (self.tareas) correspondiente a la posición indicada por el índice de fila (indice.row()). 
Se asume que cada elemento es una tupla con al menos dos elementos: un estado y un texto.<br>

`return texto:` Devuelve el texto de la tarea. En este contexto, significa que cuando se solicita el dato para la visualización de un ítem, se proporciona el texto asociado con ese ítem.

```
   def rowCount(self, indice):
       return len(self.tareas)
```
Este método nos dice el número total de filas, es decir, de items(en este caso, tareas).
Es un método abstracto e interno, es decir, aunque yo no lo use como tal, cuando uso el 
QListView() para llamar al modelo, sepa con qué trabaja y cómo hacerlo. EN este caso, necesita
contar las filas. Si en vez de una lista estuviese trabajando con una base de datos, usaría otra
función.