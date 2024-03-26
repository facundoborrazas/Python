#Pedirle un dato al usuario
numero = input("Cual es tu numero: ")
"""
Al pedirle que el usuario ingrese un dato por mas
que nos ingrese un dato de tipo int o cualquiera distinto
a string. El programa nos lo va a guardar como un string
"""

#Mostrar el numero
print(f"Tu numero es {numero}")

"""
Pero si queremos utilizar el numero para hacer calculos
debemos transformar ese valor a un entero o flotante
"""

#Hacer multiplicacion
numero = int(numero)
multiplicacion = numero * 32

print(multiplicacion)


#Hacer multiplicacion con float
numero = float(numero)
multiplicacion = numero * 32.0120232341053608

print(multiplicacion)