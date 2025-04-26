# ejercicio 3 Analisis de texto 
import re

def analizar_texto(texto):
    if not texto:
        print("Error: No has ingresado ningún texto.")
        return {}
    
    try:
        texto = texto.lower()
        texto_limpio = re.sub(r'[^\w\s]', ' ', texto)
        palabras = texto_limpio.split()
        frecuencia = {}
        
        for palabra in palabras:
            if palabra in frecuencia:
                frecuencia[palabra] += 1
            else:
                frecuencia[palabra] = 1
        
        return frecuencia
    
    except Exception as e:
        print(f"Error al procesar el texto: {e}")
        return {}


def mostrar_resultados(frecuencia):
    print("Frecuencia de palabras:")
    for palabra, veces in frecuencia.items():
        print(f"{palabra}: {veces}")
def main():
    try:
  
        texto = input("Ingrese un texto: ")
        resultado = analizar_texto(texto)
        if resultado:
            mostrar_resultados(resultado)
        
    except Exception as e:
        print(f"Error en el programa: {e}")

if __name__ == "__main__":
    main()