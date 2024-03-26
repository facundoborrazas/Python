diccionario = {
    "nombre":"Facundo",
    "apellido":"Borrazas",
    "Ocupacion":"Analista de datos"
}

#Sirve para mostrarnos las keys de cada elemento en el diccionario
#Tambien sirve para iterar
claves = diccionario.keys()
print(claves)

#Sirve para extraer un valor de un elemento del diccionario 
#Si no encuentra nada el programa continua, porque no lanza una exepcion 
get = diccionario.get("apellido")
print(get)

#Sirve si queremos eliminar solo un elemento de la lista
#Debemos poner el nombre de la key a eliminar 
pop = diccionario.pop("nombre")
print(pop)

#Obteniendo un elemento dict_item iterable 
item = diccionario.items()
print(item)

#Sirve para limpiar en su totalidad el diccionario
clear = diccionario.clear()
print(clear)

