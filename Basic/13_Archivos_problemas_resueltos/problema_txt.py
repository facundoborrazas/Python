#2 listas una con nombres y otra con apellidos:
nombres = ["Facundo","Franco","Gaby","Cristian"]
apellidos = ["Borrazás","Borrazás","Sosa","Blanco"]

with open("Archivos_problemas_resueltos//problema.txt","w",encoding="UTF-8") as archivo:
    archivo.write("Forma que lo hizo Dalto:\n")
    [archivo.write(f"El nombre es: {nombre} y el apellido {apellido}\n") for nombre, apellido in zip(nombres,apellidos)] 
    
    archivo.write("\nForma que lo hice yo antes sin ver el video:\n")
    contador = 0
    for nombre,apellido in zip(nombres,apellidos):
        archivo.write(f"El nombre es: {nombres[contador]} y el apellido {apellidos[contador]}\n")
        contador += 1