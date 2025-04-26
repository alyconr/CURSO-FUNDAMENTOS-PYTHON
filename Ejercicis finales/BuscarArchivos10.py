# ejercicio 10
# Buscador de archivos en un directorio 

import os

def buscar_archivos():
    try:
        ruta = input("Ingrese la ruta del directorio: ").strip()
        subcadena = input("Ingrese la subcadena a buscar: ").strip()

        if not os.path.exists(ruta):
            raise FileNotFoundError("El directorio no existe.")
        if not os.path.isdir(ruta):
            raise NotADirectoryError("La ruta proporcionada no es un directorio.")

        archivos = os.listdir(ruta)
        encontrados = []

        for archivo in archivos:
            ruta_completa = os.path.join(ruta, archivo)
            if os.path.isfile(ruta_completa) and subcadena.lower() in archivo.lower():
                encontrados.append(archivo)

        if encontrados:
            print(f"\nArchivos encontrados que contienen \"{subcadena}\":\n")
            for archivo in encontrados:
                print(archivo)
        else:
            print(f"No se encontraron archivos que contengan \"{subcadena}\".")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except NotADirectoryError as e:
        print(f"Error: {e}")
    except PermissionError:
        print("Error: Permiso denegado para acceder al directorio.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

buscar_archivos()