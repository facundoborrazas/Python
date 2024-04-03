#Creando un diccionario con dict()
diccionarios = dict(nombre="Facundo",apellido="Borrazás")

print(diccionarios)

#Las listas no pueden ser claves y usamos frozenset para meter conjuntos o listas
diccionarios = {frozenset(["nombre", "apellido"]): "jasjasj"}

print(diccionarios)

#Diccionario con fromkeys() el primer valor sirve de iterable el segundo como valor de cada iteracion
diccionarios = dict.fromkeys("nombre", "apellido")

print(diccionarios)

#Otro ejemplo:
#Diccionario con fromkeys() valor por defecto: none (Es un metodo de los diccionarios)
diccionarios = dict.fromkeys(["nombre", "apellido"])

print(diccionarios)

#Diccionario con fromkeys() valor por defecto: "No sé" (Es un metodo de los diccionarios)
diccionarios = dict.fromkeys(["nombre", "apellido"], "No sé")

print(diccionarios)