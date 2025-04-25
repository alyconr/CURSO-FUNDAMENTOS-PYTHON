def centimetros_a_pulgadas(cm):
    try:
        cm = float(cm)
        if cm < 0:
            return "Error: La longitud no puede ser negativa."
        pulgadas = cm / 2.54
        return pulgadas
    except ValueError:
        return "Error: Por favor, ingrese un valor numérico para los centímetros."

def kilometros_a_millas(km):
    try:
        km = float(km)
        if km < 0:
            return "Error: La distancia no puede ser negativa."
        millas = km * 0.621371
        return millas
    except ValueError:
        return "Error: Por favor, ingrese un valor numérico para los kilómetros."

print("Seleccione la conversión:")
print("1. Centímetros a pulgadas")
print("2. Kilómetros a millas")

opcion = input("Opción: ")

if opcion == '1':
    cantidad_cm = input("Ingrese la cantidad en centímetros: ")
    resultado = centimetros_a_pulgadas(cantidad_cm)
    if isinstance(resultado, str):
        print(resultado)
    else:
        print(f"{cantidad_cm} cm = {resultado:.2f} pulgadas")
elif opcion == '2':
    cantidad_km = input("Ingrese la cantidad en kilómetros: ")
    resultado = kilometros_a_millas(cantidad_km)
    if isinstance(resultado, str):
        print(resultado)
    else:
        print(f"{cantidad_km} km = {resultado:.2f} millas")
else:
    print("Opción inválida.")