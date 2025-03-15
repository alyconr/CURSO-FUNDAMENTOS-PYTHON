def verificar_password(password_correcto):
    intentos = 0
    while intentos < 5:
        password_ingresado = input("Ingresa la contraseña: ")
        if password_ingresado == password_correcto:
            print("Bienvenido al programa!")
            return  # Salir de la función si la contraseña es correcta
        else:
            intentos += 1
            print("Password incorrecto. Intentos restantes:", 5 - intentos)

    print("Demasiados intentos fallidos. El programa se cerró.")

# Ejemplo de uso
password_correcto = "secretito123"  
verificar_password(password_correcto)