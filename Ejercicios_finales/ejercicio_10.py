import os

def buscar_archivos(ruta_directorio, subcadena):
    try:
        if not os.path.isdir(ruta_directorio):
            return f"Error: El directorio '{ruta_directorio}' no existe."

        archivos_encontrados = []
        for nombre_archivo in os.listdir(ruta_directorio):
            if subcadena in nombre_archivo:
                archivos_encontrados.append(nombre_archivo)

        if archivos_encontrados:
            resultado = f"Archivos encontrados que contienen '{subcadena}':\n"
            for archivo in archivos_encontrados:
                resultado += f"{archivo}\n"
            return resultado
        else:
            return f"No se encontraron archivos con la subcadena '{subcadena}' en '{ruta_directorio}'."

    except OSError as e:
        return f"Error: No se pudo acceder al directorio '{ruta_directorio}'. {e}"

ruta = input("Ingrese la ruta del directorio: ")
buscar = input("Ingrese la subcadena a buscar: ")
resultado_busqueda = buscar_archivos(ruta, buscar)
print(resultado_busqueda)