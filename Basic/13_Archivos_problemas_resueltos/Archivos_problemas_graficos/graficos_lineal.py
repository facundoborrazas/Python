import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Archivos_problemas_resueltos//Archivos_problemas_graficos//goles.csv")

#Utilizando seaborn 
sns.lineplot(x="fecha",y="goles",data=df)

#Utilizando matplotlib
#Calculando cual fue el dia que mas metió goles
maxima_cant_goles = []
for i in df["goles"]:
    maxima_cant_goles.append(i)

#Guardamos enuna variable la fila en la que mas goles hizo en el dia
mejor_dia = df.loc[df["goles"]==max(maxima_cant_goles),:]

# Esto es el valor de la fecha que hizo mas goles. Y esto es la cantidad de goles que hizo esa fecha            
plt.plot(mejor_dia["fecha"].values[0],mejor_dia["goles"].values[0],"o")

plt.show()