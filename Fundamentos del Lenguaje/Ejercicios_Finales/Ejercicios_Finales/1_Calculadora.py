"""
Ejercicio 1: Calculadora Avanzada
Descripción:
Crea una función que actúe como calculadora. La función recibirá dos números y un operador (por ejemplo, '+', '-', '*', '/', '**', '//') para realizar la operación correspondiente.

Utiliza estructuras de control (if/else) para seleccionar la operación a realizar.
Usa manejo de excepciones para controlar errores como la división por cero y entradas no numéricas.
Puedes importar el módulo math para operaciones adicionales si es necesario.
Ejemplo de salida:

Ingrese el primer número: 10 Ingrese el segundo número: 5 Ingrese el operador (+, -, *, /, **, //): / Resultado: 10 / 5 = 2.0
"""

def calculadora(num1, num2, operador):

    try:
        num1 = float(num1)
        num2 = float(num2)
        if operador == '+':
            resultado = num1 + num2
        elif operador == '-':
            resultado = num1 - num2
        elif operador == '*':
            resultado = num1 * num2
        elif operador == '/':
            if num2 == 0:
                raise ZeroDivisionError("No se puede dividir por cero.")
            resultado = num1 / num2
        elif operador == '**':
            resultado = num1 ** num2
        elif operador == '//':
            if num2 == 0:
                raise ZeroDivisionError("No se puede dividir por cero.")
            resultado = num1 // num2
        else:
            raise ValueError("Operador no válido. Usa +, -, *, /, **, o //.")
        return resultado
    except ValueError as ve:
        return f"Error: {ve}"
    except ZeroDivisionError as zde:
        return f"Error: {zde}"
    except Exception as e:
        return f"Error inesperado: {e}"

try:
    primer_numero = input("Ingrese el primer número: ")
    segundo_numero = input("Ingrese el segundo número: ")
    operador = input("Ingrese el operador (+, -, *, /, **, //): ")

    resultado = calculadora(primer_numero, segundo_numero, operador)
    print(f"Resultado: {primer_numero} {operador} {segundo_numero} = {resultado}")

except Exception as e:
    print(f"Error en la entrada: {e}")