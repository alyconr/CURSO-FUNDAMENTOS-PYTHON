"""
Ejercicio 6: Calculadora de Factorial
Descripción:
Crea una función que calcule el factorial de un número entero ingresado por el usuario.

La función debe utilizar estructuras de control para iterar (o una solución recursiva) y calcular el factorial.
Implementa manejo de excepciones para asegurarte de que el número ingresado es entero y no negativo.
"""

def calcular_factorial(n):
    if n < 0:
        raise ValueError("El número debe ser un entero no negativo.")
    
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def solicitar_numero():
    while True:
        try:
            numero = int(input("Ingrese un número entero no negativo para calcular su factorial: "))
            if numero < 0:
                print("Error: El número debe ser no negativo. Intente de nuevo.")
                continue
            resultado = calcular_factorial(numero)
            print(f"El factorial de {numero} es {resultado}.")
            break

        except ValueError:
            print("Error: Por favor, ingrese un número entero válido.")

solicitar_numero()