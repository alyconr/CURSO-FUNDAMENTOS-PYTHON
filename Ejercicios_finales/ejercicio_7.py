from datetime import datetime

def calcular_dias_faltantes(fecha_str):
    try:
        fecha_ingresada = datetime.strptime(fecha_str, "%d/%m/%Y").date()
        hoy = datetime.now().date()
        dias_faltantes = (fecha_ingresada - hoy).days
        return f"Faltan {dias_faltantes} días para el {fecha_ingresada.strftime('%d/%m/%Y')}."
    except ValueError:
        return "Error: Formato de fecha incorrecto. Por favor, use DD/MM/AAAA."

fecha_usuario = input("Ingrese una fecha (DD/MM/AAAA): ")
resultado = calcular_dias_faltantes(fecha_usuario)
print(resultado)