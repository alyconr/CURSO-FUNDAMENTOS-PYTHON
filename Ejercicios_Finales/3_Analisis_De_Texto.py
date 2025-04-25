"""
Descripción:
Crea una función que reciba una cadena de texto y calcule la frecuencia de cada palabra en el mismo.

Convierte el texto a minúsculas y separa las palabras usando algún método (puedes utilizar expresiones regulares con el módulo re).
Emplea un diccionario para almacenar la palabra (clave) y su frecuencia (valor).
Controla excepciones en caso de que el usuario no ingrese ningún texto o ingrese caracteres inesperados.
Ejemplo de salida:
Ingrese un texto: "Hola mundo, hola a todos en el mundo" Frecuencia de palabras: hola: 2 mundo: 2 a: 1 todos: 1 en: 1 el: 1
"""

import re

def calcular(texto):
    if not texto:
        return "Error: No se ingresó ningún texto."
    
    texto = texto.lower()
    
    palabras = re.findall(r'\b\w+\b', texto)
    
    frecuencia = {}
    
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    
    return frecuencia

texto_usuario = input("Ingrese un texto: ")
resultado = calcular(texto_usuario)

if isinstance(resultado, dict):
    print("Frecuencia de palabras:")
    for palabra, cuenta in resultado.items():
        print(f"{palabra}: {cuenta}")
else:
    print(resultado)