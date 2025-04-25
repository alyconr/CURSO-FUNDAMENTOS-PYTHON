def calculadora_basica(num1, num2, operador):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        return "Error: Por favor, ingresa números válidos."

    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':
        if num2 == 0:
            return "Error: ¡No se puede dividir por cero!"
        resultado = num1 / num2
    elif operador == '**':
        resultado = num1 ** num2  # Exponenciación
    elif operador == '//':
        if num2 == 0:
            return "Error: ¡No se puede dividir por cero!"
        resultado = num1 // num2 # División entera
    else:
        return "Error: Operador no válido. Por favor, usa '+', '-', '*', '/', '**' o '//'."

    return f"Resultado: {num1} {operador} {num2} = {resultado}"

primer_numero_str = input("Ingrese el primer número: ")
segundo_numero_str = input("Ingrese el segundo número: ")
operacion = input("Ingrese el operador (+, -, *, /, **, //): ")
try:
    primer_numero = float(primer_numero_str)
    segundo_numero = float(segundo_numero_str)
except ValueError:
    print("Error: ¡Una o ambas entradas no son números válidos!")
else:
    resultado_final = calculadora_basica(primer_numero, segundo_numero, operacion)
    print(resultado_final)