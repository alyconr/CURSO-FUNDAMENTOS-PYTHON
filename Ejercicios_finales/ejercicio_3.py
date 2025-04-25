def calcular_frecuencia_palabras(texto):
    if not texto:
        return "Error: No se ingresó ningún texto."
    if not isinstance(texto, str):
        return "Error: La entrada debe ser una cadena de texto."

    texto_en_minusculas = texto.lower()
    palabras = texto_en_minusculas.split()

    frecuencia = {}
    for palabra in palabras:
        palabra_limpia = palabra.strip('.,!?"\'()[]{};:')
        if palabra_limpia: 
            if palabra_limpia in frecuencia:
                frecuencia[palabra_limpia] += 1
            else:
                frecuencia[palabra_limpia] = 1
    return frecuencia

texto_usuario = input("Ingrese un texto: ")
resultado_frecuencia = calcular_frecuencia_palabras(texto_usuario)

if isinstance(resultado_frecuencia, str):
    print(resultado_frecuencia)
else:
    print("Frecuencia de palabras:")
    for palabra, count in resultado_frecuencia.items():
        print(f"{palabra}: {count}")