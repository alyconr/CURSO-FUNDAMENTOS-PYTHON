entrada = input("Ingrese una secuencia de caracteres: ")

letras = [c for c in entrada if c.isalpha()]

resultado = tuple(letras)

print("\nSecuencia de letras extraídas:", resultado)
