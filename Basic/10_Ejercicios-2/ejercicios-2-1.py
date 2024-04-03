#Falto el profe a clase y los pibes van a armar la propia suya

#Pedir el nombre y la edad de los compañeros que vinieron hoy a clase

def obtener_compañeros(cantidad):
    compañeros = []
    for i in range(cantidad):
        nombre = input("Cual es el nombre del compañero?: ")
        edad = int(input("Cual es la edad del compañero?: "))
        compañero = (nombre,edad)
        compañeros.append(compañero)
    
    #Esto ordena la lista por el segundo valor de cada elemento (Tupla)
    compañeros.sort(key= lambda x:x[1])
    profesor = compañeros[cantidad-1]
    ayudante = compañeros[0]
    
    print("Los compañeros ordenados por edad de menor a mayor son los siguientes:")
    for compañero in compañeros:
        print(f"{compañero[0]} que tiene {compañero[1]} años")
    
    print(f"El que hará de profesor será {profesor[0]} que tiene {profesor[1]} años y el ayudante será {ayudante[0]} que tiene {ayudante[1]} años")

obtener_compañeros(3)