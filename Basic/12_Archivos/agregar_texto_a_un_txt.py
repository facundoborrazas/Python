with open("Archivos//archivo.txt","a",encoding="UTF-8") as archivo:
    """
    El permiso "a", nos permite escribir el archivo, agregando al final de este
    lo que querramos, si no lo especificamos el permiso se abre para poder leerse solamente. 
    Cada vez que ejecutamos este codigo, se va a agregar al final del archivo lo que le 
    pedimos 
    """
    archivo.write("\n")
    #Agrega al final de las lineas del archivo con esto:
    archivo.write("Este año si, como escuchaste Pa\n")

    #Agregar lineas con un for
    for i in range(5):archivo.write(f"Copa Libertadores numero {i+1}\n")
    