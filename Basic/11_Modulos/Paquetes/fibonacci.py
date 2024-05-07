#Crear una funcion que nos de el valor del calculo de la regla de Fibonacci 

def Fibonacci(num):
    """
    Primero tomamos dos variables a y b y les asignamos 
    el valor 0 y 1 respectivamente
    """
    a,b = 0,1
    #Luego creamos la lista de numeros de fibonacci solo con el numero 0 dentro
    Fibonacci_lista = [0]
    """
    Luego hacemos un bucle por una lista de numeros que vaya 
    desde 0 hasta el numero que le dimos. en cada vuelta se pregunta
    si la variable b es mas grande que el numero que le igresamos. 
    Si lo es, retorna la lista. Si no lo es, agrega el numero b
    y re asigna su valor, a pasa a tener el valor de b y b el de a+b.
    Basicamente a pasa a tener el valor de b y b el de b mas el numero anterior
    """
    for i in range(num):
        if b>num: return Fibonacci_lista
        else:
            Fibonacci_lista.append(b)
            a,b = b,a+b
    
    return Fibonacci_lista

#Lista = Fibonacci(20)
#print(Lista)