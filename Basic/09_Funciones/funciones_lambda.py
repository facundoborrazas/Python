numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

"""
lambda es una funcion anonima, es una funcion que usamos par un momento 
tan en especial que ni suqiera tenemos que crearla 
"""
#Creando una funcion lambda para multiplicar por 2
multiplicar_x_dos = lambda x:x*2

#Creando una funcion para saber si es par o no
def es_par(num):
    if (num%2==0):
        return True
    
"""
Filter ejecuta todos los elemntos de un iterable en la funcion que le pasemos
""" 
#Usando filter que es una funcion comun del lenguaje de Python
numeros_pares = filter(es_par,numeros)
print(list(numeros_pares))

#Creando lo mismo pero con lambda. Sustituimos la funcion es_par por la funcion lambda
numeros_pares = filter(lambda x:x%2==0,numeros)
print(list(numeros_pares))
