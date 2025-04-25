import random

def jugar_adivina_el_numero():
    numero_secreto = random.randint(1, 50)
    intentos = 0

    print("¡Bienvenido al juego 'Adivina el Número'!")
    print("Estoy pensando en un número entre 1 y 50.")

    while True:
        intentos += 1
        try:
            intento_usuario_str = input(f"Intento {intentos} - Ingresa tu número: ")
            intento_usuario = int(intento_usuario_str)

            if intento_usuario < numero_secreto:
                print("El número secreto es mayor.")
            elif intento_usuario > numero_secreto:
                print("El número secreto es menor.")
            else:
                print(f"¡Felicidades! Has adivinado el número secreto: {numero_secreto}")
                break
        except ValueError:
            print("Error: Por favor, ingresa un número entero válido.")

if __name__ == "__main__":
    jugar_adivina_el_numero()