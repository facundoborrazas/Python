frutas = ["Banana", "Naranja", "Granada", "Sandía", "Pera", "Manzana"]

for fruta in frutas:
    if fruta == "Granada":
        print(f"No me gusta la {fruta}")
        continue #La sentencia continue se salta ese loop y sigue con el siguiente
    
    elif fruta == "Pera":
        print(f"La {fruta} me cayó mal")
        break #La sentencia break termina el bucle pormas de que este a mitad de este
    
    """
    Si ponemos un else luego de un break, si este ultimo se cumple, 
    el else no se va a ejecutar por lo que no nos sirve poner uno luego de un break 
    """
    print(f"Me voy a comer una {fruta}")
    
cadena = "Peñarol"

#Así se recorre una cadena de texto
for letra in cadena:
    print(letra)
    
numeros = [2,4,6,8,10]
#For en un sola linea de codigo
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)