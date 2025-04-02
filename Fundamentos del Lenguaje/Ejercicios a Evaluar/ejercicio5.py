#5. Calculadora de Estadísticas de Números
#Descripción:
#Desarrolla una aplicación que trabaje con una colección de números predefinidos. El sistema debe ofrecer al usuario un menú interactivo con opciones para calcular el promedio,
#identificar el valor máximo y mínimo, o eliminar un número. Tras cada operación, se mostrará tanto el resultado como el estado actual de la colección.

numeros = [1, 2, 3, 4, 5, 6]
num = 0

while num != 5:
    print("\nMenú de opciones:")
    print("1. Calcular el promedio")
    print("2. Encontrar el valor máximo")
    print("3. Encontrar el valor mínimo")
    print("4. Eliminar un número")
    print("5. Salir")
    
    num = int(input("¿Qué opción quiere hacer? "))

    if num == 1:
        print(f"El promedio es: {sum(numeros) / len(numeros)}")
    elif num == 2:
        print(f"El valor máximo es: {max(numeros)}")
    elif num == 3:
        print(f"El valor mínimo es: {min(numeros)}")
    elif num == 4:
        eliminar = int(input("Ingrese el número a eliminar: "))
        if eliminar in numeros:
            numeros.remove(eliminar)
            print(f"Número {eliminar} eliminado.")
        else:
            print("El número no está en la lista.")
    elif num == 5:
        print("Saliendo del programa...")
        break
    
    print(f"Estado actual de la colección: {numeros}")