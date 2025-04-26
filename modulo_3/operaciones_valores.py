valores = [10, 25, 7, 30, 15]

def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Calcular la suma total")
    print("2. Ordenar valores")
    print("3. Eliminar un valor")
    print("4. Salir")

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print(f"Suma total de los valores: {sum(valores)}")
    
    elif opcion == "2":
        valores.sort()
        print(f"Valores ordenados: {valores}")

    elif opcion == "3":
        try:
            valor_eliminar = int(input("Ingrese el valor a eliminar: "))
            valores.remove(valor_eliminar)
            print(f"Valor {valor_eliminar} eliminado. Lista actualizada: {valores}")
        except ValueError:
            print("El valor no está en la lista.")
    
    elif opcion == "4":
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida. Intente de nuevo.")
