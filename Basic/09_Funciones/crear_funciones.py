#Funciones con parametros
def saludar(nombre,genero):
    genero = genero.lower()
    if genero == "hombre":
        print(f"Hola {nombre} rey, como andas?")
    elif genero == "mujer":
        print(f"Hola {nombre} reina, como andas?")
    else:
        print(f"Hola {nombre} amor, como andas?")

saludar("Facundo", "hombre")
saludar("Julieta", "MuJeR")
saludar("Fran", "No binario")

#Crear una funcion que nos retorne valores 
def crear_contraseña_random(num):
    chars = "abcdefghij"
    primer_numero = str(num)
    num = int(primer_numero[0])
    c1 = num - 3
    c2 = num + 1
    c3 = num
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num-23}"
    return contraseña

"""
Return lo que hace es retornar el valor para que pueda ser guardado en una variable
es como que la funcion empieza a tomar ese valor. Si no se lo asignamos a una variable
y luego la imprimimos, este valor no va a aparecer en la consola
"""
contraseña = crear_contraseña_random(4121231222)
print(contraseña)    

"""
El return puede retornar mas de un valor. Por ejemplo:

def crear_contraseña_random(num):
    chars = "abcdefghij"
    primer_numero = str(num)
    num = int(primer_numero[0])
    c1 = num - 3
    c2 = num + 1
    c3 = num
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num-23}"
    #Acá estamos retornando una tupla
    return contraseña,num


contraseña, primer_numero = crear_contraseña_random(4121231222)
print(f"Tu nueva contraseña es {contraseña} y el numero utilizado para crearla es {num}")
    
"""