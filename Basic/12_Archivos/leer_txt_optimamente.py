with open("Archivos//archivo.txt",encoding="UTF-8") as archivo:    
    """
    Esta forma nos permite abir el archivo y cerrarlo una vez se ejecuten 
    todas las instrucciones. Para poder utilizar el archivo abierto, debemos 
    utilizar as y cambiarle el nombre para poder hacer lo que querramos con 
    él
    """
    print(archivo.read())
    print("Esto quiere decir que el archivo se abrio y se cerro correctamente")