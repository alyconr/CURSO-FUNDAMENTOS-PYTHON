password_correcto = "1234"  # Reemplaza con la contraseña real

for intento in range(5):
    password_ingresado = input("Ingresa la contraseña: ")

    if password_ingresado == password_correcto:
        print("¡Bienvenido al programa!")
        break  
    else:
        print("Contraseña incorrecta.")

if intento == 4 and password_ingresado != password_correcto:
    print("Demasiados intentos fallidos. El programa se cerrará.")