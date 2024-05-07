import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("Archivos_problemas_resueltos\\Archivos_problemas_graficos\\ingresos_BadHonga.csv")
print(df)

#Utilizando seaborn 
sns.barplot(x="fuente",y="ingresos",data=df)

#Obteniendo el ingreso total
ingresos_totales = df["ingresos"].sum()

print(f"El total de los ingresos por mes es {ingresos_totales} pesos")

plt.show()