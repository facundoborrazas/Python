#A el modulo de pandas se le suele poner el nombre de pd como convenio
import pandas as pd

#df significa data frame. Que siginfica que es una esctructura de datos bidimensionales similares a una hoja de calculo
df = pd.read_csv("Archivos//datos.csv")
#Ejemplo para usar con el concat
df2 = pd.read_csv("Archivos//datos.csv")

#Así se obtiene todo lo que tiene el archivo
#print(df)

#Así se obtiene solo una columna del archivo
#print(df["Nombre"])

#Ordenando de menor a mayor el dataframe
df_ordenado = df.sort_values("Edad")
#print(df_ordenado)

#Ordenando de mayor a menor el dataframe
df_ordenado_mayor_a_menor = df.sort_values("Edad",ascending=False)
#print(df_ordenado_mayor_a_menor)

#Concatenar dataframes
df_concatenado = pd.concat([df,df2])
#print(df_concatenado)

#Accediendo a las primeras 3 filas con head()
df_head = df.head(3)
#print(df_head)

#Accediendo a las ultimas 3 filas con tail()
df_tail = df.tail(3)
#print(df_tail)

#Accediendo a la cantidad de filas y columnas totales
#Primero muestra las filas y luego las columnas
filas_y_columnas = df.shape
print(filas_y_columnas)
#Accediendo a la cantidad de filas y columnas por separado
filas,columnas = df.shape
print(filas)
print(columnas)

#Obteniendo data estadisitca de del daraframe
df_info = df.describe()
print(df_info)

#Obteniendo datos de elementos especificos con loc
elemento_especifico_loc = df.loc[2,"Edad"]
print(elemento_especifico_loc)

#Obteniendo datos de elementos especificos con iloc
elemento_especifico_iloc = df.iloc[2,2]
print(elemento_especifico_iloc)

#Obteniendo todos los datos de una columna con slice(:) y iloc
apellidos_iloc = df.iloc[:,1]
print(apellidos_iloc)

#Obteniendo todos los datos de una columna con slice(:) y iloc
apellidos_loc = df.loc[:,"Nombre"]
print(apellidos_loc)

#Obteniendo todos los datos de una columna con slice(:) y iloc
obteniendo_mayores30 = df.loc[df["Edad"]<30,:] #De las filas que la edad sea mayor a 30 dame todas las columnas
print(obteniendo_mayores30)