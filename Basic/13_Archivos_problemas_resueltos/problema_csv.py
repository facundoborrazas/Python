import pandas as pd

df = pd.read_csv("Archivos_problemas_resueltos//datos.csv")

#Muestra el tipo de dato antes de cambiarle el tipo
print(f"Antes de cambiarle el tipo de dato es del tipo: {type(df["Edad"][0])}")

#Convierte el tipo de dato de toda una columna 
df["Edad"] = df["Edad"].astype(str)

#Mestra el tipo de dato luego de cambiarle el tipo
print(f"Luego de cambiarle el tipo de dato pasó a ser del tipo: {type(df["Edad"][0])}")
#############################################################################################################################################################################################################################

#Remplaza el valor de una celda por otro
#Esta es la forma que dijo dalto, al parecer ya no esta del todo bien hacerlo así:
#df["Nombre"].replace("Facundo","BadHonga",inplace=True)
df.replace({"Facundo":"BadHonga"},inplace=True)
print(df["Nombre"])
#############################################################################################################################################################################################################################

#Eliminando las filas con alguna columna vacia
#Antes de eliminar esa fila
print(df)

#Luego de eliminar esa fila
df = df.dropna() #Si queremos eliminar las columnas con parametros faltantes, debemos poner como argumento en dropna(axis=1)

print(df)
#############################################################################################################################################################################################################################

#Eliminando las filas duplicadas

#Antes de eliminar los duplicados
print(df)

#Luego de eliminar los duplicados
df = df.drop_duplicates()

print(df)
#############################################################################################################################################################################################################################

#Creando un csv con el df resultante (Limpio)
df.to_csv("Archivos_problemas_resueltos//datos_limpios.csv")