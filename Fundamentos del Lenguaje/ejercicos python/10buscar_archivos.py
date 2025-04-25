
#Ejercicio 10: Buscador de Archivos en un Directorio
#Descripción:
#Desarrolla una función que reciba el nombre de un directorio y una subcadena para buscar archivos cuyo nombre la contenga.

#Utiliza el módulo os para listar el contenido del directorio.
#Aplica estructuras de control para filtrar los archivos según la subcadena.
#Implementa manejo de excepciones para controlar errores como directorio no existente o permisos insuficientes.
#Ejemplo de salida:
#Ingrese la ruta del directorio: /ruta/al/directorio Ingrese la subcadena a buscar: reporte Archivos encontrados que contienen "reporte":

#reporte_enero.pdf

#reporte_febrero.xlsx

#resumen_reporte.txt



import os

def buscar_archivos():
    try:
        # Pedir la ruta del directorio y la subcadena al usuario
        ruta_directorio = input("Ingrese la ruta del directorio: ")
        subcadena = input("Ingrese la subcadena a buscar: ")

        # Verificar si el directorio existe
        if not os.path.isdir(ruta_directorio):
            print("Error: El directorio no existe o no es un directorio válido.")
            return

        # Listar todos los archivos en el directorio
        archivos = os.listdir(ruta_directorio)

        # Filtrar los archivos que contienen la subcadena
        archivos_encontrados = [archivo for archivo in archivos if subcadena in archivo]

        if archivos_encontrados:
            print(f"Archivos encontrados que contienen \"{subcadena}\":")
            for archivo in archivos_encontrados:
                print(archivo)
        else:
            print(f"No se encontraron archivos que contengan \"{subcadena}\".")

    except PermissionError:
        print("Error: No tienes permisos suficientes para acceder al directorio.")
    except Exception as e:
        print(f"Error inesperado: {e}")

# Ejecutar la función
buscar_archivos()
