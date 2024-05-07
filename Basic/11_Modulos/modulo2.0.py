#Así se importa si el modulo esta en una carpeta dentro de la misma carpeta en la que estamos
import Funciones_buenas.modulo_saludar_function

#Así se importa si el modulo esta en otra carpeta
#Primero se importa el modulo de Python sys
import sys
#print(sys.path)

#Luego imprimios el metodo path para saber tomar la ruta de la carpeta y editarla y agregarla a la listas de paths
sys.path.append("c:\\Users\\herna\\OneDrive\\Escritorio\\Python\\Ejercicios-2")
#print(sys.path)

#Despues importamos la funcion del archivo que querramos
from fibonacci import Fibonacci 
print(Fibonacci(23))

print(Funciones_buenas.modulo_saludar_function.saludar("Facundo"))