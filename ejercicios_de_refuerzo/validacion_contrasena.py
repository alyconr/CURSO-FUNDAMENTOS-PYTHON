import re

def es_contrasena_segura(contrasena):
    return (len(contrasena) >= 8 and 
            any(c.isupper() for c in contrasena) and 
            any(c.islower() for c in contrasena) and 
            any(c.isdigit() for c in contrasena))

while True:
    contrasena = input("Introduce una contraseña segura: ")
    if es_contrasena_segura(contrasena):
        print("Contraseña válida.")
        break
    else:
        print("La contraseña debe tener al menos 8 caracteres, una mayúscula, una minúscula y un número.")
