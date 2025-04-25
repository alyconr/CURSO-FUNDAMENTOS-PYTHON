"""
Descripción:
Implementa un sistema que gestione un registro de estudiantes utilizando un diccionario, donde la clave sea el nombre y el valor la calificación.
Crea funciones para agregar un estudiante, actualizar la calificación, eliminar estudiantes y listar todo el registro.
Utiliza un bucle para mostrar un menú interactivo al usuario.
Maneja excepciones para gestionar errores en la selección de opciones o al intentar modificar un estudiante inexistente.
"""

def agregar_estudiante(registro):
    nombre = input("Ingrese el nombre del estudiante: ")
    calificacion = float(input("Ingrese la calificación del estudiante: "))
    registro[nombre] = calificacion
    print(f"Estudiante agregado: {nombre} - {calificacion}")

def actualizar_calificacion(registro):
    nombre = input("Ingrese el nombre del estudiante: ")
    if nombre in registro:
        calificacion = float(input("Ingrese la nueva calificación: "))
        registro[nombre] = calificacion
        print(f"Estudiante actualizado: {nombre} - {calificacion}")
    else:
        print("Error: Estudiante no encontrado.")

def eliminar_estudiante(registro):
    nombre = input("Ingrese el nombre del estudiante a eliminar: ")
    if nombre in registro:
        del registro[nombre]
        print(f"Estudiante eliminado: {nombre}")
    else:
        print("Error: Estudiante no encontrado.")

def listar_estudiantes(registro):
    if registro:
        print("Registro de estudiantes:")
        for nombre, calificacion in registro.items():
            print(f"{nombre}: {calificacion}")
    else:
        print("No hay estudiantes registrados.")

def menu():
    registro = {'Ana': 90, 'Luis': 78, 'Carlos': 85}  # Registro inicial
    print("Registro de estudiantes inicial:", registro)

    while True:
        print("\nMenú:")
        print("1. Agregar estudiante")
        print("2. Actualizar calificación")
        print("3. Eliminar estudiante")
        print("4. Listar estudiantes")
        print("5. Salir")
        
        try:
            opcion = int(input("Opción: "))
            if opcion == 1:
                agregar_estudiante(registro)
            elif opcion == 2:
                actualizar_calificacion(registro)
            elif opcion == 3:
                eliminar_estudiante(registro)
            elif opcion == 4:
                listar_estudiantes(registro)
            elif opcion == 5:
                print("Fianalizo el programa.")
                break
            else:
                print("Error: Opción no válida. Por favor, seleccione una opción del 1 al 5.")
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")

menu()