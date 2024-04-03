#Creando un conjunto con set()
conjunto = set(["Facundo", "Borrazás"])

#Metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset({"Facundo", "Borrazas"})
conjunto2 = {"Peñarol", conjunto1}

"""
La unica forma de que podamos poner un conjunto dentro de otro es utilizando la funcion
frozenset() que conjela un conjunto mutable y lo deja inmutable para que pueda estar dentro
de uno inmutable
"""
print(conjunto2)

#Teoria de conjuntos
conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

#issubset() es un metodo que nos da un valor booleano. Si un conjunto es subconjunto de otro
resultado = conjunto2.issubset(conjunto1)
print(resultado)
#Otra forma para verificar esto es 
resultado = conjunto2 <= conjunto1
print(resultado)

#issuperset() es un metodo que nos da un valor booleano. Si un conjunto es superconjunto de otro
resultado = conjunto2.issuperset(conjunto1)
print(resultado)
#Otra forma para verificar esto es 
resultado = conjunto2 > conjunto1
print(resultado)

#Verificar si un conjunto tiene al menos un elemnto igual al otro
#Nos da True si no tienen ninguno en comun y False si tiene algun elemento en comun
resultado = conjunto2.isdisjoint(conjunto1)
print(resultado)