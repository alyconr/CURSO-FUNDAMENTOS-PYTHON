"""
Descripción:
Crea una función que genere una contraseña aleatoria de una longitud especificada por el usuario.

Utiliza el módulo random junto con la biblioteca string para construir la contraseña a partir de letras (mayúsculas y minúsculas), dígitos y caracteres especiales.
Valida la entrada y maneja excepciones para asegurarte de que la longitud es un número entero positivo.
"""

import random
import string

def generarContraseña(longitud):
    """Genera una contraseña aleatoria de la longitud especificada."""
    # Definir los caracteres que se utilizarán en la contraseña
    caracteres = string.ascii_letters + string.digits + string.punctuation
    # Generar la contraseña aleatoria
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def solicitarLongitud():
    while True:
        try:
            longitud = int(input("Ingrese la longitud de la contraseña (número entero positivo): "))
            if longitud <= 0:
                print("Error: La longitud debe ser un número entero positivo. Intente de nuevo.")
                continue
            
            # Generar y mostrar la contraseña
            contrasena = generarContraseña(longitud)
            print(f"Contraseña generada: {contrasena}")
            break  # Salir del bucle si se genera correctamente

        except ValueError:
            print("Error: Por favor, ingrese un número entero válido.")

solicitarLongitud()
