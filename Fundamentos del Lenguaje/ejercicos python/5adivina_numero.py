#Ejercicio 5: Juego "Adivina el Número"
#Descripción:
#Implementa un juego en el que la computadora selecciona aleatoriamente un número en un rango (por ejemplo, 1 a 50) y el usuario debe adivinarlo.

#Emplea el módulo random para generar el número secreto.
#Utiliza un bucle que permita múltiples intentos, con retroalimentación indicando si el número ingresado es mayor o menor que el secreto.
#Gestiona excepciones para capturar entradas no numéricas.
#Ejemplo de salida:
#¡Bienvenido al juego "Adivina el Número"! Estoy pensando en un número entre 1 y 50. Intento 1 - Ingresa tu número: 25 El número secreto es mayor. Intento 2 - Ingresa tu número: 35 El número secreto es menor. Intento 3 - Ingresa tu número: 30 ¡Felicidades! Has adivinado el número secreto: 30

import random  # Importamos el módulo para generar el número aleatorio

def adivina_el_numero():
    print('¡Bienvenido al juego "Adivina el Número"!')
    print("Estoy pensando en un número entre 1 y 50.")

    numero_secreto = random.randint(1, 50)  # El número secreto que debes adivinar
    intento = 1  # Contador de intentos

    while True:
        try:
            # Pedimos al usuario que escriba un número
            entrada = input(f"Intento {intento} - Ingresa tu número: ")
            adivinanza = int(entrada)

            # Verificamos si el número es correcto
            if adivinanza < numero_secreto:
                print("El número secreto es mayor.")
            elif adivinanza > numero_secreto:
                print("El número secreto es menor.")
            else:
                print(f"¡Felicidades! Has adivinado el número secreto: {numero_secreto}")
                break  # Sale del bucle si adivinó

            intento += 1  # Aumentamos el número de intento

        except ValueError:
            print("Por favor, escribe un número válido.")

# Llamamos a la función
adivina_el_numero()
