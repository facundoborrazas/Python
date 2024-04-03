diccionario = {
    "Nombre":"Facundo",
    "Apellido":"Borrazás",
    "Sueldo":30.500
}

"""
Para iterar un diccionario utilizaremos el metodo .items()
"""
for item in diccionario.items():
    print(item)
    #Esta forma nos dará todos los items Clave y valor Separado por tuplas
    
    print(f"La clave es {item[0]}")
    #Esto nos daría solo la clave
    
    print(f"El valor es {item[1]}")
    #Esto nos daría solo el valor
    
"""
Si iteramos sin el .items() deberiamos hacer lo siguiente
"""
for key in diccionario:
    """
    key en este caso podriamos ponerle de cualquier forma incluso
    value pero al imprimrlo siempre nos daría la clave.
    Ya que key en esta iteracion seria el nombre que le ponemos 
    a los elementos que toman la posicion de la clave del 
    diccionario. Pero tranquilamente podria ser "Pedrito"
    """
    print(f"La clave es {key}")
    #Esto nos daría solo la clave