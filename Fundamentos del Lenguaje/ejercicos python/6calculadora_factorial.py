#Ejercicio 6: Calculadora de Factorial
#Descripción:
#Crea una función que calcule el factorial de un número entero ingresado por el usuario.

#La función debe utilizar estructuras de control para iterar (o una solución recursiva) y calcular el factorial.
#Implementa manejo de excepciones para asegurarte de que el número ingresado es entero y no negativo.
#Ejemplo de salida:
#Ingrese un número entero para calcular su factorial: 5 El factorial de 5 es 120

def calcular_factorial():
    try:
        numero = int(input("Ingrese un número entero para calcular su factorial: "))

        if numero < 0:
            print("No se puede calcular el factorial de un número negativo.")
            return

        factorial = 1
        for i in range(1, numero + 1):
            factorial *= i  # Esto es igual a factorial = factorial * i

        print(f"El factorial de {numero} es {factorial}")

    except ValueError:
        print("Por favor, ingrese un número entero válido.")

# Ejecutar la función
calcular_factorial()
