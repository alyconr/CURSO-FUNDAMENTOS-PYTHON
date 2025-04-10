#2. Realiza una función que reciba una palabra y devuelva un diccionario donde las claves sean las diferentes letras que se encuentran en la palabra y los valores sean el número de veces que se repite cada letra en la palabra

# palabra = "colombia"
# {"c":1, "o":2, "l":1, "m":1, "b":1, "i":1, "a":1}

def word(palabra):
    contar_letras = {}
    for letra in palabra:
        if letra in contar_letras:
            contar_letras[letra] += 1
        else:
            contar_letras[letra] = 1
    return contar_letras


# resultados
palabra = input("Ingrese la palabra que usted desee: ")
resultado = word(palabra)
print(resultado)
