#Ejercicio 9: Generador de Contraseñas Aleatorias
#Descripción:
#Crea una función que genere una contraseña aleatoria de una longitud especificada por el usuario.

#Utiliza el módulo random junto con la biblioteca string para construir la contraseña a partir de letras (mayúsculas y minúsculas), dígitos y caracteres especiales.
#Valida la entrada y maneja excepciones para asegurarte de que la longitud es un número entero positivo.

#Ejemplo de salida:
#Ingrese la longitud deseada para la contraseña: 10 Contraseña generada: A8b#K3d!Qz

import random
import string

def generar_contraseña():
    try:
        # Solicitar la longitud de la contraseña al usuario
        longitud = int(input("Ingrese la longitud deseada para la contraseña: "))

        if longitud <= 0:
            print("Error: La longitud debe ser un número entero positivo.")
            return

        # Definir los caracteres que se usarán en la contraseña
        caracteres = string.ascii_letters + string.digits + string.punctuation

        # Generar la contraseña aleatoria
        contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))

        print(f"Contraseña generada: {contraseña}")

    except ValueError:
        print("Error: Debe ingresar un número entero para la longitud de la contraseña.")

# Ejecutar la función
generar_contraseña()
