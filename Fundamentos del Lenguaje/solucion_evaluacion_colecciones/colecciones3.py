# Descripción: Diseña una aplicación que permita al usuario leer frases, le indique al usuario si las frases están escritas correctamente o no(sin errores), procese la información, la estructure correctamente y elimine caracteres especiales o innecesarios.

# Pedir al usuario una cadena de texto
cadena_texto = input("Ingrese cualquier tipo de cadena de texto: ")

# Separar las palabras en una lista
lista_palabras = cadena_texto.split()

# Crear una nueva lista para guardar solo letras
lista_filtrada = []

# Recorrer cada palabra
for palabra in lista_palabras:
    nueva_palabra = ""  # Variable para almacenar la palabra limpia
    for caracter in palabra:
        if caracter.isalpha():  # Verificar si el carácter es una letra
            nueva_palabra += caracter  # Agregar solo letras
    # Agregar la palabra limpia a la nueva lista
    lista_filtrada.append(nueva_palabra)

# Convertir la lista en una tupla (inmutable)
tupla_resultado = tuple(lista_filtrada)

# Mostrar el resultado
print("Texto procesado: ", tupla_resultado)
