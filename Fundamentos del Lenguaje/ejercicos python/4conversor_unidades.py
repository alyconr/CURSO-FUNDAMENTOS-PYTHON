#Ejercicio 4: Conversor de Unidades
#Descripción:
#Desarrolla un conjunto de funciones para convertir unidades métricas. Por ejemplo:

#De centímetros a pulgadas.
#De kilómetros a millas.
#Utiliza estructuras de control para verificar que la entrada sea numérica, y maneja excepciones cuando el usuario ingrese datos inválidos.
#Ejemplo de salida:
#Seleccione la conversión:

#Centímetros a pulgadas

#Kilómetros a millas Opción: 1 Ingrese la cantidad en centímetros: 100 Resultado: 100 cm = 39.37 pulgadas

def cm_a_pulgadas(cm):
    return cm / 2.54  # 1 pulgada = 2.54 cm

def km_a_millas(km):
    return km * 0.621371  # 1 kilómetro = 0.621371 millas

def conversor():
    print("escoja una opcion")
    print("1. Centímetros a pulgadas")
    print("2. Kilómetros a millas")

    opcion = input("Opción (1 o 2): ")

    try:
        if opcion == "1":
            cantidad = float(input("Ingrese la cantidad en centímetros: "))
            resultado = cm_a_pulgadas(cantidad)
            print(f"Resultado: {cantidad} cm = {round(resultado, 2)} pulgadas")

        elif opcion == "2":
            cantidad = float(input("Ingrese la cantidad en kilómetros: "))
            resultado = km_a_millas(cantidad)
            print(f"Resultado: {cantidad} km = {round(resultado, 2)} millas")

        else:
            print("Opción no válida. Por favor elija 1 o 2.")

    except ValueError:
        print("Error: Por favor ingrese un número válido.")

# Ejecutar el conversor
conversor()
