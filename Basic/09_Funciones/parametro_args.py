#Forma no optima de sumar valores
def suma1(lista):
    numeros_sumados = 0;
    for numero in lista:
        numeros_sumados = numeros_sumados + numero
        
    return numeros_sumados

#Utilizando el parametro *args
"""
El parametro *args lo que hace es tomar una lista de elemntos 
y tomarlos como valores por separados. Podemos poner como parametro
*args o *cualquier_cosa, mientras este el * al principio.
Pero es mejor si dejamos el nombre *args.
Si queremos que tome mas parametros, tenemos que ponerlos 
antes de el parametro *args
"""
def suma2(nombre,*args):
    suma = sum(args)
    return f"{nombre}, el valor de la suma es: {suma}"

suma = suma2("Facundo",2,1,4,2,11,5,9,1,2)
print(suma)