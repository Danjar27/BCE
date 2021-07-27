
# bce

Este páquete cuenta con varios módulos los cuales puedes usar para descargar los archivos xmls de la página del banco central
a través de tablas de Pandas.

## ::documentation::

Para comenzar a usarlo deberás escribir 

from getBCE.menu import *

El código tiene dos vías para que puedas llegar la información de los indicadores del Banco Central. En el caso de conocer
cuál es el número de índice de los indicadores, se puede usar **la forma rápida**, de lo contrario debería usarse la forma 
**la forma larga** 

### Forma rápida

Dentro de BCE.menu existe la clase _getBCE_, la cual tiene un sólo parámetro, que debe ser un diccionario

```python
from getBCE.menu import *

example = getBCE(dict)
```

El diccionario entregado como argumento, deberá tener las siguientes keys:

```python
from BCE.menu import *

example = getBCE({
    'year': a,
    'month': b,
    'indicator': c,
})
```
Los valores de a, b, c deben entregarse en forma de String. 

**a** debe escribirse:  '2020', '2019', '2018', ...

**b** debe escribirse: 'enero', 'febrero', ...

**c** debe escribirse '002', '004', '006' , ...

### Forma larga

En el caso de no conocer los índices de los indicadores, se pueden visualizar de la siguiente forma:

```python
from BCE.menu import *

example = setDate({
    'year': '2020',
    'month': 'enero',
    'show': False,
})

example2 = index({
    'date': example.getPage(),
    "head": 10,
    'previous': 30,
    'show': True,
})

example2.select('038')
```
Primero, se crea un nuevo objeto de la clase setDate({})  recibe los parámetros de año, mes y show. Si show es _false_, no se imprimirán
los valores de la fecha.

Después, se crea un objeto de la clase index({}), el cual recibe los parametros, **date, head, previous y show**. Al igual que la clase
setDate({}), en caso de que show = False, no se imprimirán en consola los valores del índice de los indicadores. 




