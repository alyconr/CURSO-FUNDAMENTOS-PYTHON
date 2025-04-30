def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir entre cero."

# Ejemplo de uso de las funciones
a = 10
b = 5

print(f"Suma de {a} y {b}: {suma(a, b)}")
print(f"Resta de {a} y {b}: {resta(a, b)}")
print(f"Multiplicación de {a} y {b}: {multiplicacion(a, b)}")
print(f"División de {a} entre {b}: {division(a, b)}")
