#1. Realiza una función que tome una lista de números enteros y devuelva dos listas ordenadas. La primera con los números pares y la segunda con los números impares.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []
impares = []


def mostrar_numeros():
    for i in numeros:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)


mostrar_numeros()

print("Pares:", pares)
print("Impares:", impares)
