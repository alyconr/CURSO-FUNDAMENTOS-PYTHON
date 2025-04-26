#ejercicio 7
#Manejo de fechas y Horas

from datetime import datetime
print("Calculador de días hasta una fecha")
fecha_texto = input("Ingrese una fecha (DD/MM/AAAA): ")

try:
    fecha_futura = datetime.strptime(fecha_texto, "%d/%m/%Y")
    hoy = datetime.now()
    hoy = datetime(hoy.year, hoy.month, hoy.day)
    
    diferencia = fecha_futura - hoy
    dias = diferencia.days
    
    if dias > 0:
        print(f"Faltan {dias} días para el {fecha_texto}.")
    elif dias == 0:
        print(f"¡Hoy es {fecha_texto}!")
    else:
        print(f"El {fecha_texto} ya pasó hace {abs(dias)} días.")
        
except:
    print("Error: Formato de fecha incorrecto. Use DD/MM/AAAA")