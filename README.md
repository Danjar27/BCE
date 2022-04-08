
# bce

Este páquete cuenta con varios módulos los cuales puedes usar para descargar los archivos xmls de la página del banco central
a través de tablas de Pandas.

## ::documentation::

Para comenzar a usarlo deberás instalar el paquete (o clonar el repositorio) e importarlo de la siguiente forma

```python

pip install getBCE

from getBCE.menu import *
```

El código tiene dos vías para que puedas llegar la información de los indicadores del Banco Central. En el caso de conocer
cuál es el número de índice de los indicadores, se puede usar **la forma rápida**, de lo contrario debería usarse la forma 
**la forma larga** 

### Forma rápida

Dentro de BCE.menu existe la clase _getBCE_, 

```python
from getBCE.menu import *

example = getBCE(dict)
```
Los argumentos entregados a esta clase deberán tener la siguiente forma

```python
from getBCE.menu import *

example = getBCE(
    year= a:str,
    month= b:str,
    indicator = c:str,
)
```
Los valores de a, b, c deben entregarse en forma de String. 

**a** debe escribirse:  '2020', '2019', '2018', ...

**b** debe escribirse: 'enero', 'febrero', ...

**c** debe escribirse '002', '004', '006' , ...

A modo de ejemplo:

```python
from getBCE.menu import *

balanza_de_pagos = getBCE(
    year: '2021',
    month: 'junio',
    indicator: '063',
)
```

para integrar la información obtenida con la libería Pandas, se emplea el método **read_excel()** y el módulo de getBCE **getHref()**

```python
import pandas as pd

data_frame = pd.read_excel(balanza_de_pagos.getHref())
```


### Forma larga

En el caso de no conocer los índices de los indicadores, se pueden visualizar creando objetos para las clases **setDate()** e **index()**:

```python
from getBCE.menu import *

fecha = SetDate(
    year='2020',
    month='enero',
)

indice = index(
    date=example.getDate(),
    head=10,
    previous=30,
    show=True,
)

indice.select('038')
```
Primero, se crea un nuevo objeto de la clase setDate({}) , la cual recibe los parámetros de **'year'** y **'month'** en un diccionario. 

Después, se crea un objeto de la clase index({}), la cual recibe los parametros, **date, head, previous** y **show**.

Para fijar la fecha, se debe utilizar el valor que regresa la clase setDate, para lo cual se utiliza su método **getDate()**, como valor de 'date' en el diccionario del objeto de la clase index({}).

El valor que se le asigne a **'head'** será el número de elementos que se imprimirán en consola (siempre que show sea True). En la mayoría de años el total de indicadores es 93, por lo que para ver todos se puede escribir:

```python
indice = index(
    date= example.getDate(),
    head= 93,
    previous= 0,
    show= True,
)
```
aunque hay años en los que hay más o menos indicadores, por lo cual queda a discresión de cada usuario.

El valor de **'previous'** sirve para navegar entre los indicadores para cualquier valor de 'head'. Si 'previous' es igual a 10, se imprimiran en consola los 'head' indicadores que estén después del indicador '010'

Si show es _false_, no se imprimirá el índice en consola. Conviene ponerlo de esta manera una vez que ya se conoce la key del indiciador deseado, para que no moleste en consola.

Finalmente, para obtener el enlace del índice seleccionado se emplea el método **.select( indicador, imprimir)** de la clase index. El valor default de imprimir es cero, pero en caso de que se necesite descargar el archivo xlsx, puede cambiarse a True, con lo cual se imprimirá en consola el enlace de descarga.

De esta manera, se integraría a pandas de la siguiente forma:

```python
from getBCE.menu import *

fecha = SetDate(
    year='2020',
    month='enero',
)

indice = index(
    date=example.getDate(),
    head=10,
    previous=30,
    show=False,
)

seleccion = indice.select('038')

import pandas as pd

data_frame = pd.read_excel(seleccion)
```
