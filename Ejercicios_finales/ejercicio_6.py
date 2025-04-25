def calcular_factorial(numero_str):
    try:
        numero = int(numero_str)
        if numero < 0:
            return "Error: El factorial no está definido para números negativos."
        elif numero == 0:
            return 1
        else:
            factorial = 1
            for i in range(1, numero + 1):
                factorial *= i
            return factorial
    except ValueError:
        return "Error: Por favor, ingrese un número entero válido."

numero_ingresado_str = input("Ingrese un número entero para calcular su factorial: ")
resultado = calcular_factorial(numero_ingresado_str)

if isinstance(resultado, str):
    print(resultado)
else:
    print(f"El factorial de {numero_ingresado_str} es {resultado}")