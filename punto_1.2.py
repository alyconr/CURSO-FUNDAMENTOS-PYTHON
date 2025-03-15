def calcular_matricula(valor_matricula, estrato, edad):
    """
    Calcula el precio de la matrícula con descuentos según estrato y edad.

    Args:
        valor_matricula (float): El valor base de la matrícula.
        estrato (int): El estrato del estudiante (1 o 2).
        edad (int): La edad del estudiante.

    Returns:
        tuple: Una tupla con el valor del descuento y el precio final de la matrícula.
    """

    descuento = 0

    if estrato == 1:
        if edad < 18:
            descuento = 0.20  # 20% de descuento
        else:
            descuento = 0.15  # 15% de descuento
    elif estrato == 2:
        if edad < 18:
            descuento = 0.10  # 10% de descuento
        else:
            descuento = 0.05  # 5% de descuento

    valor_descuento = valor_matricula * descuento
    precio_final = valor_matricula - valor_descuento

    return valor_descuento, precio_final

def limpiar_valor_matricula(valor_str):
    """
    Limpia la cadena de entrada para convertirla en un número float.

    Args:
        valor_str (str): La cadena de entrada con separadores de miles (puntos).

    Returns:
        float: El valor numérico de la matrícula.
    """
    valor_str = valor_str.replace(".", "")  # Elimina los puntos
    return float(valor_str)

# Ejemplo de uso
valor_matricula_str = input("Ingrese el valor de la matrícula (ej: 1.800.000): ")
valor_matricula = limpiar_valor_matricula(valor_matricula_str) #Limpiar el valor
estrato = int(input("Ingrese el estrato del estudiante (1 o 2): "))
edad = int(input("Ingrese la edad del estudiante: "))

descuento, precio_final = calcular_matricula(valor_matricula, estrato, edad)

print(f"Valor del descuento: ${descuento:.0f}")
print(f"Precio final de la matrícula: ${precio_final:.0f}")