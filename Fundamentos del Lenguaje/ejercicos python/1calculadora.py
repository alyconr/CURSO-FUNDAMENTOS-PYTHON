#Crea una función que actúe como calculadora. La función recibirá dos números y un operador (por ejemplo, '+', '-', '*', '/', '**', '//') para realizar la operación correspondiente.

def calculadora():
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        operador = input("Ingrese el operador (+, -, *, /, **, //): ")

        if operador == '+':
            resultado = num1 + num2
        elif operador == '-':
            resultado = num1 - num2
        elif operador == '*':
            resultado = num1 * num2
        elif operador == '/':
            resultado = num1 / num2
        elif operador == '**':
            resultado = num1 ** num2
        elif operador == '//':
            resultado = num1 // num2
        else:
            print("Operador no válido.")
            return

        print(f"Resultado: {num1} {operador} {num2} = {resultado}")

    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
    except ValueError:
        print("Error: Entrada no válida. Por favor, ingrese números.")

# Ejecutar la función
calculadora()
