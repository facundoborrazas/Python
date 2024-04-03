#Creando una funcion de 3 parametros
"""
def frase(nombre,apellido,adjetivo):
    return f"Hola {nombre} {apellido}, sos muy {adjetivo}"
    
#Utilizando keywords arguments
frase_a_imprimir = frase(adjetivo="Genio", nombre="Facundo", apellido="Borrazás")
print(frase_a_imprimir)

#El keywords arguments nos permite poder poner el valor de los parametros en el orden que querramos mientras que especifiquemos que parametro tiene cada valor
"""

#Tambien podemos setearle un valor predefinido a un parametro y si el usuario no lo edita este quedará así. Ya que es un parametro opcional
def frase(nombre,apellido,adjetivo="Tonto"):
    return f"Hola {nombre} {apellido}, sos muy {adjetivo}"
    
#Utilizando keywords arguments
frase_a_imprimir = frase(adjetivo="Genio", nombre="Facundo", apellido="Borrazás")
print(frase_a_imprimir)

