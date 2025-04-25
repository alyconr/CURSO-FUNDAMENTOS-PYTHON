"""
Descripción:
Desarrolla una función que reciba una fecha ingresada por el usuario en formato "DD/MM/AAAA" y determine cuántos días faltan para esa fecha a partir de hoy.

Importa el módulo datetime para trabajar con fechas.
Utiliza estructuras de control para validar el formato y maneja excepciones en caso de error en el ingreso de la fecha.
"""
from datetime import datetime

def calcularDias(fecha_str):
    try:
        fecha_ingresada = datetime.strptime(fecha_str, "%d/%m/%Y")
        fecha_actual = datetime.now()
        diferencia = (fecha_ingresada - fecha_actual).days
        
        return diferencia

    except ValueError:
        return None

def solicitar_fecha():
    while True:
        fecha_str = input("Ingrese una fecha en formato DD/MM/AAAA: ")
        dias_faltantes = calcularDias(fecha_str)
        
        if dias_faltantes is None:
            print("Error: El formato de la fecha es incorrecto. Asegúrese de usar DD/MM/AAAA.")
        else:
            if dias_faltantes > 0:
                print(f"Faltan {dias_faltantes} días para la fecha {fecha_str}.")
            elif dias_faltantes == 0:
                print("La fecha ingresada es hoy.")
            else:
                print(f"La fecha {fecha_str} ya ha pasado.")

            break
solicitar_fecha()