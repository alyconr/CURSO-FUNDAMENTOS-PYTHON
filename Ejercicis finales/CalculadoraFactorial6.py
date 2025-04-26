#ejercicio
#calculadora factorial 

def calcular_factorial():
    try:
        num = int(input("Ingrese un número entero para calcular su factorial: "))

        if num < 0:
            raise ValueError("El número no puede ser negativo.")

        factorial = 1
        for i in range(1, num + 1):
            factorial *= i

        print(f"El factorial de {num} es {factorial}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

calcular_factorial()
