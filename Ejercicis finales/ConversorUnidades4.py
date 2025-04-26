#ejercicio 4
#conversor de unidades

def cm_a_pulgadas(cm):
    return cm / 2.54

def km_a_millas(km):
    return km * 0.621371

print("Seleccione la conversión:")
print("1. Centímetros a pulgadas")
print("2. Kilómetros a millas")

try:
    opcion = int(input("Opción: "))

    if opcion == 1:
        cantidad = float(input("Ingrese la cantidad en centímetros: "))
        resultado = cm_a_pulgadas(cantidad)
        print(f"Resultado: {cantidad} cm = {round(resultado, 2)} pulgadas")

    elif opcion == 2:
        cantidad = float(input("Ingrese la cantidad en kilómetros: "))
        resultado = km_a_millas(cantidad)
        print(f"Resultado: {cantidad} km = {round(resultado, 2)} millas")

    else:
        print("Opción no válida. Seleccione 1 o 2.")

except ValueError:
    print("Error: Ingrese solo números válidos.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")