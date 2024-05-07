import modulo_saludar 
"""
Para utilizar una funcion de otro metodo
debemos utilizar lo que importamos como 
si fuese un metodo. Podemos asignarle otro
valor a el modulo que importamos para no tener que 
escribirlo siempre tan largo. Con as le asignamos
otro valor. Esto tambien sirve para las funciones
"""
import modulo_saludar as m_saludar
#Tambien podemos importar solo una funcion o varias pero no todo el modulo
from modulo_saludar import saludar

saludo0 = modulo_saludar.saludar("BadHonga")
print(saludo0)


saludo1 = m_saludar.saludar("Facundo")
print(saludo1)


saludo2 = saludar("Hernan")
print(saludo2)