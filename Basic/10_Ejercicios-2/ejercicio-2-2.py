#Crear una funcion que nos de los numeros primos que hay entre el 2 hasta ese numero

#Funcion que verifia si el numero es primo
def es_par(num):
    """
    El for lopeea por una lista de numeros desde el 2 hasta el numero que le damos sin incluirlo.
    Luego por cada vuelta preguntamos si el resto de la division entre el numero que pasamos y 
    el valor de la variable i, que va aumentando por cada loop, es 0. Si esto es cierto esto quiere 
    decir que no es primo, ya que este numero es divisible entre 1 el mismo numero y minimo un 
    numero mas entre medio de estos dos. Mientras que si en ningun loopeo da 0 como resto de la division, 
    esto quiere decir que es primo retornando True.
    """
    for i in range(2,num):
        if num%i==0: return False
        else:
            return True
        
def listado_numeros_pares(num):
    """
    Crea una lista de todos los numeros desde el 0 hasta el numero que le pasamos incluyendolo.
    Luego con un for vamos loopeando por cada numero de la lista. Cada uno de estos pasa por la funcion
    anterior. Si retorna True, este numero será agragado a una lista de numeros distinta, sino sigue de largo.
    Luego de dar todas las vueltas, retorna la lista con los numeros que son pares.
    """
    numeros_sin_filtrar = list(range(num+1))
    numeros_filtrados = []
    
    for numero in numeros_sin_filtrar:
        if es_par(numero) == True:
            numeros_filtrados.append(numero)
            
    return numeros_filtrados

numeros_pares = listado_numeros_pares(7)
print(numeros_pares)
                     
