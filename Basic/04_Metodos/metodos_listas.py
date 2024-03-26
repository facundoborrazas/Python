#Creando una lista con list()
lista = list(["Hola",123,"papa",5234,True,324324.433]) #Al crear una lista de esta forma debemos poner los elementos en forma de lista
 
#Contar la cantidad de elementos
cantidad_elementos = len(lista)

#Agregando un elemento a la lista
lista.append("JAJAJAJA")

#Agregando un elemento a la lista en un indice especifico
lista.insert(2,"Peñarol")

#Agregando varios elementos a la lista
lista.extend(["Eeeaaaa", 21322.34, False]) #Al agregar mas de un elemento debemos poner los elementos en forma de lista

#Elimina un elemento de la lista (Por su indice)
lista.pop(3) #-1 para eliminar el ultimo, -2 para eliminar el anteultimo, y asi sucesivamente

#Removiendo un elemento de la lista por su valor
lista.remove(123)

#Eliminando todos los elementos de la lista
lista.clear()

###########################################################33
lista = [12,4123,123.22,64345,True,False,1232122]

#Ordenando la lista de forma asendente (si le ponemos el argumento reverse=True, los ordena al reves)
lista.sort() #Para que sort funcione la lista solo debe tener numeros o Trues o Falses

#Invierte los elementos de la lista, no importa si estan previamente ordenados o no
lista.reverse()

#Verificando si un elemento se encuentra en la lista
elemento_encontrado = lista.index(12) #Esto busca si esta el elemento completo si encontrara 1212 no lo va a tomar como 12, porque para que tome como 12 tiene que ser precisamente ese valor

