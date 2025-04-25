import random
import string

def generar_contrasena(longitud_str):
    try:
        longitud = int(longitud_str)
        if longitud <= 0:
            return "Error: La longitud de la contraseña debe ser un número entero positivo."
        caracteres = string.ascii_letters + string.digits + string.punctuation
        contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
        return contrasena
    except ValueError:
        return "Error: Por favor, ingrese un número entero válido para la longitud."

longitud_deseada_str = input("Ingrese la longitud deseada para la contraseña: ")
contrasena_generada = generar_contrasena(longitud_deseada_str)
print(f"Contraseña generada: {contrasena_generada}")