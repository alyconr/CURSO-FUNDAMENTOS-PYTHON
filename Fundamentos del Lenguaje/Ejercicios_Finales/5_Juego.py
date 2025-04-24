"""
Descripción:
Implementa un juego en el que la computadora selecciona aleatoriamente un número en un rango (por ejemplo, 1 a 50) y el usuario debe adivinarlo.

Emplea el módulo random para generar el número secreto.
Utiliza un bucle que permita múltiples intentos, con retroalimentación indicando si el número ingresado es mayor o menor que el secreto.
Gestiona excepciones para capturar entradas no numéricas.
"""

import random

def adivina_el_numero():
    numero_secreto = random.randint(1, 50)
    intentos = 0

    print("¡Bienvenido al juego de adivinar el número!")
    print("He seleccionado un número entre 1 y 50. ¡Intenta adivinarlo!")

    while True:
        try:
            adivinanza = int(input("Ingrese su numero: "))
            intentos += 1
            if adivinanza < numero_secreto:
                print("El número es mayor. Intenta de nuevo.")
            elif adivinanza > numero_secreto:
                print("El número es menor. Intenta de nuevo.")
            else:
                print(f"¡Felicidades! Has adivinado el número {numero_secreto} en {intentos} intentos.")
                break

        except ValueError:
            print("Error: Por favor, ingresa un número válido.")

adivina_el_numero()