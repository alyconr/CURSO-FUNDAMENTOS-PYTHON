# Descripción: Implementa un sistema que gestione un registro de exámenes y sus calificaciones. El programa debe permitir agregar nuevos registros, listar todos los exámenes con sus respectivas calificaciones e incluir opciones para consultar las calificaciones por estudiante o por examen específico.


notas = {}

while True:
    # se crea un menu para que los usuarios vean las opciones
    opcion = input(
        "\n1. Agregar/Actualizar notas\n2. Consultar notas\n3. Mostrar todos los registros\n4. Salir\nSeleccione una opción: ")
    # se almacena el nombre del estudiante
    if opcion == "1":
        nombre = input("Nombre del estudiante: ")
        # si no encuentra un registro
        if nombre not in notas:
            notas[nombre] = []  # Se crea la entrada si no existe

        for i in range(int(input("¿Cuántas notas desea agregar?: "))):
            materia = input(f"Materia: ")
            nota = float(input("Calificación: "))
            notas[nombre].append((materia, nota))

    elif opcion == "2":
        nombre = input("Ingrese el nombre del estudiante: ")
        # Muestra o avisa si no existe
        print(notas.get(nombre, "Estudiante no encontrado."))

    elif opcion == "3":
        for estudiante, calificaciones in notas.items():
            print(f"\n{estudiante}: {calificaciones}")

    elif opcion == "4":
        print("Cerrando el programa...")
        break

    else:
        print("Opción no válida.")
