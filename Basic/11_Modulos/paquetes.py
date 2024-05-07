"""
Utilizar un paquete es como utiilizar muchos modulos en una misma ruta.
Por ejemplo, si en una carpeta tenemos muchos modulos, y queremos utilizar todos
en vez de importar cada modulo por separado, importamos la carpeta entera.
Para esto, debemos hacer que Python se de cuenta que la carpeta donde se 
encuentran todos estos modulos es un paquete y no un modulo. 
Entonces debemos crear un archivo con el nombre "__init__.py" sin nada dentro.
"""

import Paquetes.fibonacci

print(Paquetes.fibonacci.Fibonacci(40))

import Paquetes.saludar

print(Paquetes.saludar.saludar("Facundo"))