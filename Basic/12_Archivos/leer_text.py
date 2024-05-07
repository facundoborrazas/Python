"""
Para abrir un archivo .txt debemos abrir el archivo dandole una ruta 
y guardar su valor en una variable, para luego poder leerlo
"""
#El encoding es para que al leer el archivo podamos leer bien todos los caracteres
archivo = open("Archivos//archivo.txt",encoding="UTF-8")

#Leer archivo completo
#print(archivo.read())

#Leer linea por linea
"""
Esto va a darnos un arreglo separados por lineas de texto
"""
#lineas = archivo.readlines()
#print(lineas)

#Leer linea
"""
Esto siempre va a leer la primera linea, si le ponemos algun numero de 
atributo, esto nos dará la cantiad de caracteres que le demos como atributo 
de la primera linea
"""
linea = archivo.readline()
print(linea)

#Cerrar archivo
"""
Luego de haber trabajado con el archivo siempre se debe cerrar el archivo
"""
archivo.close()

