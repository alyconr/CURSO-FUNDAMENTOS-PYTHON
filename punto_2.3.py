def letras_repetidas_misma_posicion(frase1, frase2):

    letras_repetidas = []
    longitud_minima = min(len(frase1), len(frase2))

    for i in range(longitud_minima):
        if frase1[i] == frase2[i] and frase1[i].isalpha():
            letras_repetidas.append(frase1[i])

    return letras_repetidas

# Pedir al usuario que ingrese las dos frases
frase1 = input("Ingresa la primera frase: ")
frase2 = input("Ingresa la segunda frase: ")

# Encontrar las letras repetidas
resultado = letras_repetidas_misma_posicion(frase1, frase2)

# Mostrar el resultado
print("Letras repetidas en la misma posición:", resultado)