#ejercicio 8
#Registro de estudiantes

registro_estudiantes = {
    'Ana': 90,
    'Luis': 78,
    'Carlos': 85
}


def listar_estudiantes(registro):
    print("\n== Lista de Estudiantes ==")
    if len(registro) == 0:
        print("No hay estudiantes registrados.")
    else:
        for nombre, calificacion in registro.items():
            print(f"{nombre} - {calificacion}")
    print() 


def agregar_estudiante(registro):
    nombre = input("Ingrese el nombre del estudiante: ")
    
    if nombre in registro:
        print(f"El estudiante {nombre} ya existe.")
        return registro
    
    try:
        calificacion = int(input("Ingrese la calificación: "))
        if calificacion < 0 or calificacion > 100:
            print("La calificación debe estar entre 0 y 100.")
            return registro
        
        registro[nombre] = calificacion
        print(f"Estudiante agregado: {nombre} - {calificacion}")
    except ValueError:
        print("Error: La calificación debe ser un número.")
    
    return registro

def actualizar_calificacion(registro):
    nombre = input("Ingrese el nombre del estudiante: ")
    
    if nombre not in registro:
        print(f"El estudiante {nombre} no existe en el registro.")
        return registro
    
    try:
        calificacion = int(input("Ingrese la nueva calificación: "))
        if calificacion < 0 or calificacion > 100:
            print("La calificación debe estar entre 0 y 100.")
            return registro
        
        registro[nombre] = calificacion
        print(f"Estudiante actualizado: {nombre} - {calificacion}")
    except ValueError:
        print("Error: La calificación debe ser un número.")
    
    return registro

def eliminar_estudiante(registro):
    nombre = input("Ingrese el nombre del estudiante a eliminar: ")
    
    if nombre in registro:
        del registro[nombre]
        print(f"Estudiante {nombre} eliminado correctamente.")
    else:
        print(f"El estudiante {nombre} no existe en el registro.")
    
    return registro

def mostrar_menu():
    print("\nMenú:")
    print("1. Agregar estudiante")
    print("2. Actualizar calificación")
    print("3. Eliminar estudiante")
    print("4. Listar estudiantes")
    print("5. Salir")

def main():
    print("Registro de estudiantes inicial:", registro_estudiantes)
    salir = False
    
    while not salir:
        mostrar_menu()
        
        try:
            opcion = int(input("Opción: "))
            
            if opcion == 1:
                registro_estudiantes.update(agregar_estudiante(registro_estudiantes))
            elif opcion == 2:
                registro_estudiantes.update(actualizar_calificacion(registro_estudiantes))
            elif opcion == 3:
                registro_estudiantes.update(eliminar_estudiante(registro_estudiantes))
            elif opcion == 4:
                listar_estudiantes(registro_estudiantes)
            elif opcion == 5:
                salir = True
                print("\nRegistro final:", registro_estudiantes)
                print("¡Gracias por usar el sistema de registro!")
            else:
                print("Opción no válida. Por favor ingrese un número del 1 al 5.")
        except ValueError:
            print("Error: Debe ingresar un número.")

if __name__ == "__main__":
    main()