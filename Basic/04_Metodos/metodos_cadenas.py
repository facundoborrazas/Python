cadena1 = "Holas soy Facundo"
cadena2 = "Peñarol Peñarol"

#############################################################################
"""
FUNCIONES
"""
#############################################################################

"""
dir() nos sirve para saber todos los metodos que tiene un objeto.
Como dir es algo que se ejecuta y lo deja ahí, debemos imprimirlo en pantalla
para saber su valor
"""
#Es un metodo, por eso se usa de la siguiente manera:
print(dir(cadena1))

"""
len() nos sirve para saber cuantos caracteres tiene una cadena de texto
"""
#Es un metodo, por eso se usa de la siguiente manera:
print(len(cadena1))

#############################################################################
"""
METODOS
"""
#############################################################################

"""
upper() nos permite poner en mayuscula todo el string
"""
#Como es un metodo lo debemos poner de la siguiente manera:
print(cadena1.upper())

"""
lower() nos permite poner en minuscula todo el string
"""
#Como es un metodo lo debemos poner de la siguiente manera:
print(cadena1.lower())

"""
capitalize() nos permite poner la primera letra en mayuscula
"""
#Como es un metodo lo debemos poner de la siguiente manera:
print(cadena1.capitalize())

"""
find() nos permite una cadena dentro de otra
"""
#Es key sensitive. Cuando no encuentra valor, retorna -1
print(cadena1.find("F"))

"""
index() nos permite una cadena dentro de otra
"""
#Es key sensitive. Cuando no encuentra valor, lanza una excepcion
print(cadena1.index("F"))

"""
isnumeric() nos permite saber si una cadena son numeros. Por mas que sea un texto
"""
#Devuelve True si lo es False si no lo es
print(cadena1.isnumeric())

"""
isalpha() nos permite si la cadena es alfa numerico. Los caracteres especiales y el espacio nos daran como resultado false
"""
#Devuelve True si lo es False si no lo es
print(cadena1.isalpha())

"""
count() Nos permite saber cuantas veces se encuetra un caracter en una cadenma
"""
#Devuelve un valor segun cuantas veces lo encuentre. Si no encuentra, nos devuelve 0
print(cadena1.count("F"))

"""
startswith() Nos permite saber si una cadena de texto comienza con un caracter o cadena de caracteres
"""
#Devuelve True si lo es False si no lo es
print(cadena1.startswith("F"))

"""
endswith() Nos permite saber si una cadena de texto comienza con un caracter o cadena de caracteres
"""
#Devuelve True si lo es False si no lo es
print(cadena1.endswith("F"))

"""
replace() Nos permite remplazar ciertos caracteres por otros 
"""
#Si encuentra el valor que queremos remplazar, lo remplaza. Si no nos devolverá la cadena sin cambios
print(cadena1.replace("F", "W"))

"""
split() Nos permite separar la cadena en cadenas 
"""
#Nos devolverá una lista, matriz y/o array con cada palabra separada. Si no le pasamos nada como atributo, nos separa por espacios. Si le pasamos un caracter nos separá por ese caracter
print(cadena1.split())
