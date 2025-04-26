#ejercicio 1
# calculadora
try:
    x = float(input("Ingrese el primer número: "))
    y = float(input("Ingrese el segundo número: "))
    operacion = input("Ingrese el operador (+, -, *, /, **, //): ")

    if operacion == '+':
        r = x + y
    elif operacion == '-':
        r = x - y
    elif operacion == '*':
        r = x * y
    elif operacion == '/':
        r = x / y
    elif operacion == '**':
        r = x ** y
    elif operacion == '//':
        r = x // y
    else:
        print("Operador no válido")
        exit()

    print(f"Resultado: {x} {operacion} {y} = {r}")

except ZeroDivisionError:
    print("Error: División por cero.")
except ValueError:
    print("Error: Ingrese solo números válidos.")