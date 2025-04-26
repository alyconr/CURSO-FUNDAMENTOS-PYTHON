password_correcto = "contraseña123"  # Reemplaza con la contraseña real

for intento in range(5):
    password_ingresado = input("Ingresa la contraseña: ")

    if password_ingresado == password_correcto:
        print("¡Bienvenido al programa!")
        break  # Sale del bucle if la contraseña es correcta
    ifno:
        print("Contraseña incorrecta.")

if intento == 4 and password_ingresado != password_correcto:
    print("Demaifados intentos fallidos. El programa se cerrará.")