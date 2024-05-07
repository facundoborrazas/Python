import re

texto = """Peñarol va a ser campeon de america en el 2024.
Vamos a ganar todos los clasicos.
Y las gallinas no van a poder creerlo.
"""

#Buscando todas las veces que aparece ese caracter o palabra en el texto
resultado = re.findall("a", texto)
print(resultado)
#Buscando la primera vez que aparece ese caracter o palabra en el texto
resultado = re.search("a", texto)
print(resultado)

#\d --> Busca digitos numericos del 0 al 9 
resultado = re.search(r"\d",texto)
print(resultado)
resultado = re.findall(r"\d",texto)
print(resultado)

#\D --> Busca TODO MENOS digitos numericos del 0 al 9 
resultado = re.search(r"\D",texto)
print(resultado)
resultado = re.findall(r"\D",texto)
print(resultado)

#\w --> Busca caracteres alfanumericos [a-z A-Z 0-9 _ ] 
resultado = re.search(r"\w",texto)
print(resultado)
resultado = re.findall(r"\w",texto)
print(resultado)

#\W --> Busca TODO MENOS caracteres alfanumericos [a-z A-Z 0-9 _ ] 
resultado = re.search(r"\W",texto)
print(resultado)
resultado = re.findall(r"\W",texto)
print(resultado)

#\s --> Busca espacios en blanco, tabs y saltos de linea 
resultado = re.search(r"\s",texto)
print(resultado)
resultado = re.findall(r"\s",texto)
print(resultado)

#\S --> Busca TODO MENOS espacios en blanco, tabs y saltos de linea 
resultado = re.search(r"\S",texto)
print(resultado)
resultado = re.findall(r"\S",texto)
print(resultado)

#. --> Busca TODO MENOS saltos de linea
resultado = re.search(r".",texto)
print(resultado)
resultado = re.findall(r".",texto)

#\n --> Busca saltos de linea
resultado = re.search("\n",texto)
print(resultado)
resultado = re.findall("\n",texto)
print(resultado)

#\ --> Sirve para cancelar caracteres especiales (Sirve para cualquier caracter no alfanumerico)
resultado = re.search("\.",texto)
print(resultado)
resultado = re.findall("\.",texto)
print(resultado)

#Extrayendo una cadena del texto donde diga "2024.
#Vamos a ganar"
resultado = re.search("\d{4}\.\n.{13}",texto)
print(resultado)
resultado = re.findall("\d{4}\.\n.{13}",texto)
print(resultado)