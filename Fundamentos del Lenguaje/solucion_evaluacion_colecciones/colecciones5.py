# Descripción: Desarrolla una aplicación que trabaje con una lista de números enteros ingresados por el usuario. La aplicación deberá calcular estadísticas básicas como promedio, mediana, moda y desviación estándar sobre los números ingresados por el usuario; además deberá permitir ordenar los números tanto en orden ascendente como descendente.

datos = [5, 4, 3, 2, 1]

print(
    f"Este es el menú de opciones que tienes con estos datos.\n{datos}\n1. Calcular promedio\n2. Identificar el valor máximo\n3. Identificar el valor mínimo\n4. Eliminar un número")

while True:
    opcion = input("Elige una opción para el menú: ")

    if opcion == "1":
        promedio = sum(datos) / len(datos)
        print(f"El promedio de los números es: {promedio}")

    elif opcion == "2":
        maximo = max(datos)  # Encuentra el número más alto en la lista
        print(f"El valor máximo es: {maximo}")

    elif opcion == "3":
        minimo = min(datos)  # Encuentra el número más alto en la lista
        print(f"El valor minimo es: {minimo}")

    elif opcion == "4":
        num = int(input("Ingresa el número que deseas eliminar: "))
        if num in datos:  # Verifica si el número está en la lista
            datos.remove(num)  # Elimina el número
            print(
                f"El número {num} ha sido eliminado. Lista actualizada: {datos}")
        else:
            print("El número no está en la lista.")
    else:
        print("el numero no se encuentra en la lista.")
