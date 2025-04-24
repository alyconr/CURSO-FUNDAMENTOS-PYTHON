"""
Descripción:
Desarrolla una función que reciba el nombre de un directorio y una subcadena para buscar archivos cuyo nombre la contenga.

Utiliza el módulo os para listar el contenido del directorio.
Aplica estructuras de control para filtrar los archivos según la subcadena.
Implementa manejo de excepciones para controlar errores como directorio no existente o permisos insuficientes.
"""

import os

def buscar_archivos(directorio, subcadena):
    try:
        archivos = os.listdir(directorio)
        
        archivos_encontrados = [archivo for archivo in archivos if subcadena in archivo]
        
        if archivos_encontrados:
            print(f'Archivos encontrados que contienen "{subcadena}":')
            for archivo in archivos_encontrados:
                print(archivo)
        else:
            print(f"No se encontraron archivos que contengan '{subcadena}' en el directorio '{directorio}'.")

    except FileNotFoundError:
        print(f"Error: El directorio '{directorio}' no existe.")
    except PermissionError:
        print(f"Error: Permisos insuficientes para acceder al directorio '{directorio}'.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def solicitar_busqueda():
    directorio = input("Ingrese la ruta del directorio: ")
    subcadena = input("Ingrese la subcadena a buscar: ")
    buscar_archivos(directorio, subcadena)

solicitar_busqueda()