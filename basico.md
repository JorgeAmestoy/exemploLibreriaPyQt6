<p align="center"><b><font size="7">EXPLICACIONES BÁSICAS PYTHON</font></b></p>

--------------------------
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

### MÉTODO SHOW<br>
Puedo llamar al método *show()* o bien, dentro del
constructor de la ventana principal con `self.show()`,
o fuera de la clase con el objeto/variable llamado *ventana*, en la que creo una instancia de dicha clase
y al heredar de QMainWindow puedo usar el método *show()*.

---------------------------
### FIRMAS DE MÉTODOS
Posicionando el cursor sobre métodos heredados de otras clases nos enseña detalles sobre este. Por ejemplo:<br>

Aquí digo que el método va a recibir obligatoriamente una variable de tipo String.

```
def __init__(self, nombre: [str]):
```
-------------------------------
<br>
Aquí digo que va a recibir de manera opcional el parámetro. Si no lo uso, cuando haga la instancia tengo que escribir None.

```
def __init__(self, nombre: Optional[str]):
     self.nombre = nombre
     
objeto_con_nombre = Ejemplo(nombre="Alice")
objeto_con_nombre.saludar()
     
objeto_sin_nombre = Ejemplo(nombre=None)
objeto_sin_nombre.saludar()
```

-------------------------
<br>
Aquí pido por parámetro una variable de cualquier tipo y de uso opcional:

```
def ejemploMetodo(self, variable: Any = None) -> int:
    # Implementación del método
    # ...
    return numero
```
Por lo tanto, este método va a recibir como parámetro una variable.<br>
**Any** signfica que la variable *indice* puede ser de cualquier tipo.<br>
**None** significa que el uso de este parámetro es opcional. <br>
**-> int:** significa que dicho método nos va a devolver un int.<br>
Así, aunque al trabajar en el método nos lo use, hay que escribirlos en la definición de este.<br> <br>
-------------------------
<br>

El término iterable en este contexto se utiliza para indicar que se espera cualquier tipo de objeto que sea iterable. Con la barra indico que las siguientes palabras serán **palabras clave**. Key será opcional
y el reverse si no se especifica que va a ser True, será False por defecto.
```
sorted(iterable, /, *, key=None, reverse=False)
```
Ejemplo usando la key y el reverse False:
```
# Ordenar una lista de cadenas por longitud en orden ascendente
palabras = ["manzana", "banana", "uva", "kiwi"]
palabras_ordenadas = sorted(palabras, key=len)
print(palabras_ordenadas)
# Salida: ['uva', 'kiwi', 'banana', 'manzana']

```
Por lo tanto, **key=len** especifica que la longitud de cada cadena (len) debe usarse como criterio para la ordenación. **Reverse** no se proporciona, por lo que la ordenación es en orden ascendente (longitudes más cortas primero).

---------------------------------

## TUPLAS
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
Así, en las listas puedo añadir(append), eliminar(remove).. después de haberla creado, mientras que en la tupla, una vez que haya sido creada,
no puedo modificar su contenido.

----------------------------------

#### ENUMERATE
Es una función que itera sobre una lista/tupla y nos retorna una tupla con el índice y el valor de los elementos
```
frutas = ['manzana', 'plátano', 'uva']# Creo una lista

# Usando enumerate para obtener índice y valor al mismo tiempo
for indice, fruta in enumerate(frutas): # Itero en la lista
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
       
# Código fuera del bucle
print("Fin del procesamiento")

```
Va itereando por todos los elementos de la lista indices y va guardando lo que encuentra en la variable indice.

----------------------------------
