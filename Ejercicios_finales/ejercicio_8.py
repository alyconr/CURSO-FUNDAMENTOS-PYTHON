def agregar_estudiante(registro):
    nombre = input("Ingrese el nombre del estudiante: ")
    while True:
        calificacion_str = input(f"Ingrese la calificación de {nombre}: ")
        try:
            calificacion = int(calificacion_str)
            if 0 <= calificacion <= 100:
                registro[nombre] = calificacion
                print(f"Estudiante '{nombre}' agregado con calificación {calificacion}.")
                break
            else:
                print("Error: La calificación debe estar entre 0 y 100.")
        except ValueError:
            print("Error: Por favor, ingrese un número entero para la calificación.")

def actualizar_calificacion(registro):
    nombre = input("Ingrese el nombre del estudiante a actualizar: ")
    if nombre in registro:
        while True:
            nueva_calificacion_str = input(f"Ingrese la nueva calificación para {nombre}: ")
            try:
                nueva_calificacion = int(nueva_calificacion_str)
                if 0 <= nueva_calificacion <= 100:
                    registro[nombre] = nueva_calificacion
                    print(f"Calificación de '{nombre}' actualizada a {nueva_calificacion}.")
                    break
                else:
                    print("Error: La calificación debe estar entre 0 y 100.")
            except ValueError:
                print("Error: Por favor, ingrese un número entero para la calificación.")
    else:
        print(f"Error: El estudiante '{nombre}' no existe en el registro.")

def eliminar_estudiante(registro):
    nombre = input("Ingrese el nombre del estudiante a eliminar: ")
    if nombre in registro:
        del registro[nombre]
        print(f"Estudiante '{nombre}' eliminado del registro.")
    else:
        print(f"Error: El estudiante '{nombre}' no existe en el registro.")

def listar_estudiantes(registro):
    if not registro:
        print("El registro de estudiantes está vacío.")
        return
    print("Registro de estudiantes:")
    for nombre, calificacion in registro.items():
        print(f"- {nombre}: {calificacion}")

registro_estudiantes = {'Ana': 90, 'Luis': 78, 'Carlos': 85}
print(f"Registro de estudiantes inicial: {registro_estudiantes}")

while True:
    print("\nMenú:")
    print("1. Agregar estudiante")
    print("2. Actualizar calificación")
    print("3. Eliminar estudiante")
    print("4. Listar estudiantes")
    print("5. Salir")

    opcion = input("Opción: ")

    if opcion == '1':
        agregar_estudiante(registro_estudiantes)
    elif opcion == '2':
        actualizar_calificacion(registro_estudiantes)
    elif opcion == '3':
        eliminar_estudiante(registro_estudiantes)
    elif opcion == '4':
        listar_estudiantes(registro_estudiantes)
    elif opcion == '5':
        print("Saliendo del registro de estudiantes. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción del menú.")

print(f"\nRegistro final: {registro_estudiantes}")