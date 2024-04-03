#Lugar de donde voy a sacar los valores de las variables
lista = ["Facundo", "Borrazás", 21]
tupla = ("Facundo", "Borrazás", 21)

#Desempaquetado
"""
Para desempaquetar datos debemos tener la misma cantidad de variables que de 
datos que tiene la lista o tupla de donde queremos sacarla 
"""
nombre,apellido,edad = lista
print(f"El nombre es {nombre} el apellido {apellido} y la edad es {edad}")
nombre,apellido,edad = tupla
print(f"El nombre es {nombre} el apellido {apellido} y la edad es {edad}")
