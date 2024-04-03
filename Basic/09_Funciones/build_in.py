"""
Las funciones build in son las funciones que ya vienen 
pre definidas e integradas dentro de Python o el lenguaje de 
programacion en cuestion
"""

numeros = [1,543,456,44,2,34,78]

#Eligiendo el numero mas alto de la lista o conjunto iterable 
numero_mas_alto = max(numeros)
print(numero_mas_alto)

#Eligiendo el numero mas chico de la lista o conjunto iterable 
numero_mas_chico = min(numeros)
print(numero_mas_chico)

#Redondeando un decimal
numero_redondeado = round(12.432523,3)
print(numero_redondeado)

#Funcion Bool retorna False si: el argumento es vacio, Falso, no le pasamos dato alguno o 0
booleano = bool()
print(booleano)

"""Funcion all comprueba todos si todos los elementos del iterable son o no verdaderos
retorna False si: el argumento es vacio, Falso, no le pasamos dato alguno o 0"""
funcion_all = all([2,43,[False,"True"],0,32432.344,"HHHHHHHHH"])
print(funcion_all)

#Funcion para sumar numeros. Solo funciona si son todos los elementos numeros
suma = sum(numeros)
print(suma)