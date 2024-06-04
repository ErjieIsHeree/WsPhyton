#Diferencia en porcentaje entre el cuso actual y:
    #El más RÁPIDO de otros cursos
    #El más LENTO de otros cursos
    #El PROMEDIO de los cursos

curso_actual = 1.5

curso_mas_rapido = 2.5
diferencia_actual_rapido = 100 - curso_actual * 100 / curso_mas_rapido
print(f"La diferencia en porcenta entre el curso actual y el más rápido es de {diferencia_actual_rapido}%")

curso_mas_lento = 7
diferencia_actual_lento = 100 - curso_actual * 1000 // curso_mas_lento / 10
print(f"La diferencia en porcenta entre el curso actual y el más lento es de {diferencia_actual_lento}%")

curso_promedio = 4
diferencia_actual_promedio = 100 - curso_actual * 100 / curso_promedio
print(f"La diferencia en porcenta entre el curso actual y el promedio es de {diferencia_actual_promedio}%")
    
#Porcentaje de material inservible que se reduce en:
    #El promedio de los cursos
    #El curso actual (este curso)

print("")
material_crudo_actual = 3.5
material_inservible_actual = 100 - curso_actual * 1000 // material_crudo_actual / 10
print(f"El material inservible del curso actual = {material_inservible_actual}")

material_crudo_promedio = 5
material_inservible_promedio = 100 - curso_promedio * 1000 // material_crudo_promedio / 10
print(f"El material inservible del curso promedio = {material_inservible_promedio}")

#Ver 10 horas de este curso a cuantas de otros cursos equivale?

print("")

equivale_lento = curso_promedio * 100 // curso_actual / 10
print(f"Ver 10 horas de dalto equivale a {equivale_lento} del curso lento")

