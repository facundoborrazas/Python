Animales = ["Perro","Gato","Loro","Conejo"]
Numeros = [12,43214,5643,1231,6432,2,5457,12,7456,234,0,543,32]

"""
En este ejemplo "Animal" vendria a ser una variable que va tomando valores
distintos segun en que ronda del bucle este. Y solo se puede utilizar dentro de este bucle.
Animales es el elemento que queremos iterar. En este caso es una lista
"""
for Animal in Animales:
    print(f"Ahora la variable 'Animal' tiene el valor: {Animal}")
    
###########################################################################################################    
print("###########################################################################################################")
###########################################################################################################    

for Numero in Numeros:
    """
    No es necesario tantos parentesis en el redondeo
    """
    resultado = round((Numero * 0.00212654009),2)
    print(f"Ahora la variable 'Numero' tiene el valor: {resultado}")
    
###########################################################################################################    
print("###########################################################################################################")
###########################################################################################################  

Cuadros = ["Peñarol","Boca","Nacional","River"]
Puntos = [72,70,68,56]

#Iterando mas de una lista (Deben ser del mismo tamaño, pero puden ser mas de dos listas)
for Cuadro,Pts in zip(Cuadros,Puntos):
    print(f"{Cuadro} tiene {Pts} puntos")
    
###########################################################################################################    
print("###########################################################################################################")
###########################################################################################################  

"""
range() toma el primer valor inlusive y va hasta el siguiente valor que le demos sin incluirlo 
si agregamos un argumento mas podemos hacer que vaya de 2 en 2 o del valor que queramos en el valor que queramos
"""
#Utilizando la funcion range()
for num in range(0,10):
    print(num)

###########################################################################################################    
print("###########################################################################################################")
###########################################################################################################  
"""
Esta funcion nos dara el indice y su valor en forma de tupla de una lista. Se puede separar para
que no lo muestre en forma de tupla
"""
#Utilizando la funcion Enumerate()
for indice,num in enumerate(Numeros):
    print(f"El indice {indice} tiene el valor {num}")

###########################################################################################################    
print("######################################################################################################################################################################################################################")
########################################################################################################### 

#Utilizando el else en un bucle
for Numero in Numeros:
    print(f"La variable tiene el valor de {Numero}")
else:
    """
    El else se va a ejecutar al final SIEMPRE
    """
    print("###########################################################################################################")
    print("El bucle terminó")
    print("###########################################################################################################")
    
#Todo esto sirve para listas, tuplas y conjuntos