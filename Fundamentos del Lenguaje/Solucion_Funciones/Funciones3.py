#3. Realiza una función que reciba un número y devuelva una cadena con los nombres de los números recibidos, separando cada número con un guión medio.  Por ejemplo, si el número recibido es 134, la función devolverá la cadena "uno - tres - cuatro"

def numero_a_palabras(numero):
    numeros_en_letras = {
        "0": "cero",
        "1": "uno",
        "2": "dos",
        "3": "tres",
        "4": "cuatro",
        "5": "cinco",
        "6": "seis",
        "7": "siete",
        "8": "ocho",
        "9": "nueve"
    }

    numero_str = str(numero)  # Convertir a cadena para recorrerlo
    palabras = []

    for digito in numero_str:
        if digito in numeros_en_letras:
            palabras.append(numeros_en_letras[digito])

    resultado = " - ".join(palabras)
    return resultado


# Ejemplo de uso
numero = input("Ingresa un número: ")
print(numero_a_palabras(numero))
