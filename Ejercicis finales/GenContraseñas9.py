#ejercicio 9
#generador de contraseñas

import random
import string

def generar_contraseña():
    try:
        longitud = int(input("Ingrese la longitud deseada para la contraseña: "))

        if longitud <= 0:
            raise ValueError("La longitud debe ser un número entero positivo.")

        caracteres = string.ascii_letters + string.digits + string.punctuation
        contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))

        print(f"Contraseña generada: {contraseña}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

generar_contraseña()