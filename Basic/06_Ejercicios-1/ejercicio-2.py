texto = input("Dime un texto a leer: ")
lista_texto = texto.split()
lista_texto = len(lista_texto)
persona_promedio_tiempo_hablando = int((lista_texto)/2)


#Ejercicio B
if(persona_promedio_tiempo_hablando >= 60):
    print("Para flaco tampoco te pedí que me digas un textamento")
else:
#Ejercicio A
    print(f"Una persona normal tardó {persona_promedio_tiempo_hablando} segundos en decir la frase y dijo {lista_texto} palabras")


#Ejercicio C
promedio_menos_que_habla_Dalto = (30*persona_promedio_tiempo_hablando)/100
print(f"Dalto tardaría {(persona_promedio_tiempo_hablando) - promedio_menos_que_habla_Dalto} segundos en decir la frase y dijo {lista_texto} palabras")