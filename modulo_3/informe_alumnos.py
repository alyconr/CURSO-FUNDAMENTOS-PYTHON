alumnos = ["Ana", "Bruno", "Carlos", "Daniela", "Elena"]
calificaciones = [85, 92, 78, 88, 95]

print("Informe de alumnos y calificaciones:")
for i, (nombre, nota) in enumerate(zip(alumnos, calificaciones)):
    print(f"{i}: {nombre} - {nota}")

while True:
    try:
        indice = int(input("\nIngrese el número de estudiante para ver su calificación (o un número fuera del rango para salir): "))
        if 0 <= indice < len(alumnos):
            print(f"{alumnos[indice]} tiene una calificación de {calificaciones[indice]}")
        else:
            print("Saliendo del sistema.")
            break
    except ValueError:
        print("Entrada no válida, intente de nuevo.")
