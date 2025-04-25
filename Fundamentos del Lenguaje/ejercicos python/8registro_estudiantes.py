#Ejercicio 8: Registro de Estudiantes
#Descripción:
#Implementa un sistema que gestione un registro de estudiantes utilizando un diccionario, donde la clave sea el nombre y el valor la calificación.

#Crea funciones para agregar un estudiante, actualizar la calificación, eliminar estudiantes y listar todo el registro.
#Utiliza un bucle para mostrar un menú interactivo al usuario.
#Maneja excepciones para gestionar errores en la selección de opciones o al intentar modificar un estudiante inexistente.
#Ejemplo de salida:
#Registro de estudiantes inicial: {'Ana': 90, 'Luis': 78, 'Carlos': 85}

#Menú:

#Agregar estudiante

#Actualizar calificación

#Eliminar estudiante

#Listar estudiantes

#Salir

#Opción: 2 Ingrese el nombre del estudiante: Luis Ingrese la nueva calificación: 82 Estudiante actualizado: Luis - 82

#Registro final: {'Ana': 90, 'Luis': 82, 'Carlos': 85}



# Registro de estudiantes inicial
registro_estudiantes = {'Ana': 90, 'Luis': 78, 'Carlos': 85}

def agregar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    try:
        calificacion = float(input(f"Ingrese la calificación de {nombre}: "))
        registro_estudiantes[nombre] = calificacion
        print(f"Estudiante agregado: {nombre} - {calificacion}")
    except ValueError:
        print("Error: La calificación debe ser un número válido.")

def actualizar_calificacion():
    nombre = input("Ingrese el nombre del estudiante: ")
    if nombre in registro_estudiantes:
        try:
            nueva_calificacion = float(input(f"Ingrese la nueva calificación para {nombre}: "))
            registro_estudiantes[nombre] = nueva_calificacion
            print(f"Estudiante actualizado: {nombre} - {nueva_calificacion}")
        except ValueError:
            print("Error: La calificación debe ser un número válido.")
    else:
        print("Error: El estudiante no existe.")

def eliminar_estudiante():
    nombre = input("Ingrese el nombre del estudiante a eliminar: ")
    if nombre in registro_estudiantes:
        del registro_estudiantes[nombre]
        print(f"Estudiante {nombre} eliminado.")
    else:
        print("Error: El estudiante no existe.")

def listar_estudiantes():
    if registro_estudiantes:
        print("Registro de estudiantes:")
        for nombre, calificacion in registro_estudiantes.items():
            print(f"{nombre}: {calificacion}")
    else:
        print("No hay estudiantes registrados.")

def menu():
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
                agregar_estudiante()
            elif opcion == 2:
                actualizar_calificacion()
            elif opcion == 3:
                eliminar_estudiante()
            elif opcion == 4:
                listar_estudiantes()
            elif opcion == 5:
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida. Por favor, elija una opción entre 1 y 5.")
        except ValueError:
            print("Error: Debe ingresar un número entre 1 y 5.")

# Ejecutar el menú
menu()
