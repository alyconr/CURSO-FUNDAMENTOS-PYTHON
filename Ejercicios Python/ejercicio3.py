#Un alumno desea saber cuál será su calificación final en la materia de Matemáticas. Dicha calificación se compone de los siguientes porcentajes: 55% del promedio de sus tres calificaciones parciales (se debe leer cada calificación parcial). 30% de la calificación del examen final. 15% de la calificación de un trabajo final.
print("Ingrese las tres calificaciones parciales:")
Calificacion_Parcial_1= float(input("Primer parcial: "))
Calificacion_Parcial_2= float(input("Segundo parcial: "))
Calificacion_Parcial_3= float(input("Tercer parcial: "))
   
Examen_Final= float(input("Ingrese la calificación del examen final: "))

Trabajo_Final= float(input("Ingrese la calificación del trabajo final: "))

Calificacion_Parcial_55 = ((Calificacion_Parcial_1 + Calificacion_Parcial_2 + Calificacion_Parcial_3) / 3)  * 0.55
Examen_Final_30 = Examen_Final * 0.30
Trabajo_Final_15 = Examen_Final * 0.15

Promedio = Calificacion_Parcial_55 + Examen_Final_30 + Trabajo_Final_15

print(Promedio)