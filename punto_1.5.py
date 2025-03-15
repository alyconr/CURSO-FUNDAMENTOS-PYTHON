def calcular_recaudo_descuento(valor_boleta):
    """Calcula el recaudo y descuento para una persona."""
    estrato = int(input("Ingrese el estrato (1 o 2): "))
    edad = int(input("Ingrese la edad: "))

    descuento = 0
    if estrato == 1:
        if edad < 18:
            descuento = 0.20
        else:
            descuento = 0.15
    elif estrato == 2:
        if edad < 18:
            descuento = 0.10
        else:
            descuento = 0.05

    valor_descontado = valor_boleta * descuento
    valor_pagado = valor_boleta - valor_descontado

    return valor_pagado, valor_descontado

def calcular_totales(n, valor_boleta):
    """Calcula el total recaudado y descontado para N personas."""
    total_recaudado = 0
    total_descontado = 0

    for _ in range(n):
        valor_pagado, valor_descontado = calcular_recaudo_descuento(valor_boleta)
        total_recaudado += valor_pagado
        total_descontado += valor_descontado

    return total_recaudado, total_descontado

# Ejemplo de uso
n = int(input("Ingrese el número de personas(de preferencia números pequeños ): "))
valor_boleta = float(input("Ingrese el valor de la boleta: "))

total_recaudado, total_descontado = calcular_totales(n, valor_boleta)

print(f"Total recaudado: ${total_recaudado:.0f}")
print(f"Total descontado: ${total_descontado:.0f}")
