#Creando una lista (Se pueden modificar)
lista = ["Facundo Borrazás","Soy Facundo",True,1.70, "Soy Facundo"]

#Creando una tupla (No se puede modificar)
tupla = ("Facundo Borrazás", "Soy Facundo", True, 1.70, "Soy Facundo")

#Esto es valido
lista[3] = "Peñarol"

#Esto no es valido
#tupla[3] = "Peñarol"

#Creando un conjunto (set) (No se accede a elementos por indice, no almacena datos duplicados)
conjunto = {"Facundo Borrazás", "Soy Facundo", True, 1.70, "Soy Facundo"}

#print(conjunto[3]) -> No puede acceder al elemento

#Creando un diccionario (dict) (la estructura es key: value y separados con comas)
diccionario = {
    "nombre":"Facundo Borrazás",
    "trabajo": "Asignet", 
    "esta_emocionado": True,
    "altura": 1.70
}

print(diccionario["altura"])
