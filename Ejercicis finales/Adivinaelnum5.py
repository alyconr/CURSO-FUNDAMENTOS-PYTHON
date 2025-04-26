#ejercicio 5
#juego "adivina el numero"

import random
print("¡Bienvenido al juego \"Adivina el Número\"!")
print("Estoy pensando en un número entre 1 y 50.")

numero_secreto = random.randint(1, 50)
intentos = 0
adivinado = False

while not adivinado:
    intentos = intentos + 1
    print(f"Intento {intentos} - Ingresa tu número: ", end="")
    
    try:
        numero_usuario = int(input())
        if numero_usuario == numero_secreto:
            print(f"¡Felicidades! Has adivinado el número secreto: {numero_secreto}")
            adivinado = True
       
        elif numero_usuario < numero_secreto:
            print("El número secreto es mayor.")
        else:
            print("El número secreto es menor.")
            
    except:
        print("Error: Debes ingresar un número.")
        intentos = intentos - 1  

print(f"Lo lograste en {intentos} intentos.")