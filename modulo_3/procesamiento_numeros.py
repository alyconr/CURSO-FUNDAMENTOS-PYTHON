numeros = list(range(1, 21))

divisibles = [(i, num) for i, num in enumerate(numeros) if num % 2 == 0]
no_divisibles = len(numeros) - len(divisibles)
suma_divisibles = sum(num for _, num in divisibles)

print("Números divisibles por 2 con su posición:")
for pos, num in divisibles:
    print(f"Posición {pos}: {num}")

print(f"\nCantidad de números no divisibles por 2: {no_divisibles}")
print(f"Suma de los números divisibles por 2: {suma_divisibles}")
