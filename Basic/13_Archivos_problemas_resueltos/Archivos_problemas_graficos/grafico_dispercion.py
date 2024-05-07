import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("Archivos_problemas_resueltos\\Archivos_problemas_graficos\\dispercion.csv")
print(df)

#Utilizando seaborn 
sns.scatterplot(x="tiempo",y="dinero",data=df)

plt.show()