import csv

with open("Archivos//datos.csv",encoding="UTF-8") as archivo:
    reader = csv.reader(archivo)
    for row in archivo:
        print(row)
        
    print("Si lees esto es porque se abrió y cerró correctamente")