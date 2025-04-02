#4. Registro y Consulta de Calificaciones de Exámenes
#Descripción:
#Implementa un sistema que gestione un registro de estudiantes y sus calificaciones. El programa debe permitir agregar nuevos registros, 
#listar todos los existentes y consultar la calificación de un estudiante introduciendo su nombre. Se espera que la información se actualice y se presente de forma clara en cada paso.

estudiantes = ["pablo","natalia","natasha"]
notas = [3,1,5] 

for i in range (min(len(estudiantes), len(notas))):
    print(f"{i} {estudiantes[i]} = {notas[i]}")
    

pregunta =int(input(""" que desea hacer?
 1. nuevo estudiante
 2. buscar estudiante"""))

if pregunta == 1:
    estudiante_nuevo = input("Nombre del nuevo estudiante")
    nota_nuevo = int(input("nota del estudiante"))  
    estudiantes.append(estudiante_nuevo)
    notas.append(nota_nuevo)
elif pregunta == 2:
    consulta = int(input("que estudiante desea buscar"))
    print(f"{estudiantes[consulta]} = {notas[consulta]}")
    
    
for i in range(min(len(estudiantes), len(notas))):
    print(f"{i+1} {estudiantes[i]} = {notas[i]}")