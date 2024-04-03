#Curso Dalto
curso_Dalto = 1.5

#Promedios de duraciones
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4

#Ejercicio A
#Diferencias de duracion
"""
Se pone menos 100 para saber cuanto porcentaje menos dura el video de dalto
ya que si no nos daria como resultado cuanto porcentje de tiempo es el video de 
dalto comparados con los otros
"""
#Promedio entre la duracion entre el curso de dalto y el minimo
diferencia_con_min = round(100-(curso_Dalto / otros_cursos_min * 100),2)
print(f"El video de Dalto es un {diferencia_con_min}% más rapido que el mas rapido")
#Promedio entre la duracion entre el curso de dalto y el maximo
diferencia_con_max = round(100-(curso_Dalto / otros_cursos_max * 100),2)
print(f"El video de Dalto es un {diferencia_con_max}% más rapido que el lento")
#Promedio entre la duracion entre el curso de dalto y el promedio
diferencia_con_promedio = round(100-(curso_Dalto / otros_cursos_promedio * 100),2)
print(f"El video de Dalto es un {diferencia_con_promedio}% más rapido que el promedio")

print("##############################################################################")

#Ejercicio B
#Duracion de crudos
crudos_Dalto = 3.5
crudos_promedio = 5

tiempo_vacio_promedio = round(100-(otros_cursos_promedio / crudos_promedio * 100),2)
tiempo_vacio_Dalto = round(100-(curso_Dalto / crudos_Dalto * 100),2)
print(f"Un curso promedio elimina un porcentaje del {tiempo_vacio_promedio}% del video")
print(f"El curso de Dalto elimina un porcentaje del {tiempo_vacio_Dalto}% del video")

print("##############################################################################")

#Ejercicio C
#Equivalencias entre duracion de cursos
print(f"Mirar 10 horas de este curso equivale a {round(otros_cursos_promedio/curso_Dalto*10,2)} horas de otros cursos")
print(f"Mirar 10 horas de otros cursos equivale a {round(curso_Dalto/otros_cursos_promedio*10,2)} horas de este curso")

print("##############################################################################")