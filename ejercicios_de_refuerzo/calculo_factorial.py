def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

num = int(input("Introduce un número para calcular su factorial: "))
print(f"El factorial de {num} es {factorial(num)}.")
