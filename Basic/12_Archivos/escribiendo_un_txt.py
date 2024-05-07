with open("Archivos//archivo.txt","w",encoding="UTF-8") as archivo:
    """
    El permiso "w", nos permite escribir el archivo, si no lo especificamos 
    el permiso se abre para poder leerse solamente. 
    El Permiso "w" siempre va a sobre escribir lo que haya en el archivo.
    Y si no encuentra archivo con ese nombre, lo crea
    """
    #Sobre escribir las lineas del archivo por esto:
    #archivo.write("Peñarol siempre va a ser el mas grande del Mundo Pa")
    
    #Escribr mas de una linea
    """
    Para poder escribir mas de una linea le tenemos que dar un elemento iterable 
    """
    archivo.writelines(["Peñarol siempre va a ser el mas grande del Mundo Pa\n","Y ademas Peñarol va a ser campeon de la Libertadores nuevamente en el 2024\n"])
    
    