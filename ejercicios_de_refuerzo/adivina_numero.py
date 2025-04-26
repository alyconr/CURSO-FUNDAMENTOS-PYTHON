import random

numero_secreto = random.randint(1, 100)
intento = None

print("Adivina el número secreto entre 1 y 100")

while intento != numero_secreto:
    intento = int(input("Introduce tu número: "))
    if intento < numero_secreto:
        print("El número secreto es mayor.")
    elif intento > numero_secreto:
        print("El número secreto es menor.")
    else:
        print("¡Felicidades! Has adivinado el número.")
