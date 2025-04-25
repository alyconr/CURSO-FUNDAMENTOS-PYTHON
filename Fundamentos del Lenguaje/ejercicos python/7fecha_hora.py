
#Ejercicio 7: Manejo de Fechas y Horas
#Descripción:
#Desarrolla una función que reciba una fecha ingresada por el usuario en formato "DD/MM/AAAA" y determine cuántos días faltan para esa fecha a partir de hoy.

#Importa el módulo datetime para trabajar con fechas.
#Utiliza estructuras de control para validar el formato y maneja excepciones en caso de error en el ingreso de la fecha.
#Ejemplo de salida:
#Ingrese una fecha (DD/MM/AAAA): 25/12/2023 Faltan 150 días para el 25/12/2023.


import datetime  # Importamos el módulo datetime

def calcular_dias_faltantes():
    try:
        # Pedimos la fecha al usuario en formato "DD/MM/AAAA"
        fecha_str = input("Ingrese una fecha (DD/MM/AAAA): ")

        # Convertimos la fecha ingresada a formato datetime
        fecha_ingresada = datetime.datetime.strptime(fecha_str, "%d/%m/%Y")

        # Obtenemos la fecha actual (hoy)
        hoy = datetime.datetime.today()

        # Calculamos la diferencia en días
        diferencia = fecha_ingresada - hoy
        dias_faltantes = diferencia.days

        if dias_faltantes > 0:
            print(f"Faltan {dias_faltantes} días para el {fecha_str}.")
        elif dias_faltantes < 0:
            print(f"La fecha {fecha_str} ya pasó hace {-dias_faltantes} días.")
        else:
            print(f"¡Hoy es el {fecha_str}!")

    except ValueError:
        print("Error: Por favor, ingrese la fecha en el formato correcto 'DD/MM/AAAA'.")

# Ejecutar la función
calcular_dias_faltantes()
