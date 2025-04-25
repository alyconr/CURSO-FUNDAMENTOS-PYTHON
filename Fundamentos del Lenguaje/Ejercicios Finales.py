#1.Calculadora
def calculadora_avanzada():
    try:
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        operador = input("Ingrese el operador (+, -, *, /, //, **): ")

        if operador == '+':
            resultado = num1 + num2
        elif operador == '-':
            resultado = num1 - num2
        elif operador == '*':
            resultado = num1 * num2
        elif operador == '/':
            resultado = num1 / num2
        elif operador == '//':
            resultado = num1 / num2
        elif operador == '**':
            resultado = num1 / num2
        else:
            print("Operador NO valido.")
            return

        print(f"Resultado: {num1} {operador} {num2} = {resultado}")

    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
    except ValueError:
        print("Error. Por favor ingrese números que sean validos.")

if __name__ == "__main__":
    calculadora_avanzada()
#////////////////////////////////////////////////////////////////////////////////////////
#2. Administrador de inventarios 
inventario = {"manzanas": 50, "naranjas": 30, "peras": 20}


def mostrar_inventario():

    print("Inventario actual:", inventario)

def agregar_producto(nombre, cantidad):
    
    inventario[nombre] = inventario.get(nombre, 0) + cantidad
    print(f"Producto '{nombre}' agregado con {cantidad} unidades.")

def actualizar_producto(nombre, cantidad):

    if nombre in inventario:
        inventario[nombre] = cantidad
        print(f"Actualizando stock de '{nombre}' a {cantidad}...")
    else:
        raise KeyError(f"El producto '{nombre}' no existe en el inventario.")

def eliminar_producto(nombre):

    if nombre in inventario:
        del inventario[nombre]
        print(f"Eliminando '{nombre}'...")
    else:
        raise KeyError(f"El producto '{nombre}' no existe en el inventario.")

print("Inventario inicial:", inventario)

try:
        actualizar_producto('peras', 60)
        agregar_producto('bananas', 10)
        eliminar_producto('manzanas')
except KeyError as e:
        print(e)

mostrar_inventario()
#/////////////////////////////////////////////////////////////////////////////////////
#3. Analisis de texto
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
#//////////////////////////////////////////////////////////////////////////////////////////////////
#4. Conversor de unidades
def cm_a_pulgadas(cm):
    return cm / 2.54

def km_a_millas(km):
    return km / 1.60934

def convertir_unidad():
    while True:
        try:
            opcion = input("Seleccione la conversión:\n1. Centímetros a Pulgadas\n2. Kilómetros a Millas\n3. Salir\nOpción: ")
            
            if opcion == '1':
                cm = float(input("Ingrese la cantidad en centímetros: "))
                pulgadas = cm_a_pulgadas(cm)
                print(f"{cm} centímetros son {pulgadas:.2f} pulgadas.")
                
            elif opcion == '2':
                km = float(input("Ingrese la cantidad en kilómetros: "))
                millas = km_a_millas(km)
                print(f"{km} kilómetros son {millas:.2f} millas.")
                
            elif opcion == '3':
                print("Saliendo del programa.")
                break
                
            else:
                print("Opción no válida. Por favor, seleccione 1, 2 o 3.")
        
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")

convertir_unidad()
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#5. Juego "Adivina el numero"
import random

def adivina_el_numero():
    print('Este es mi juego "Adivina el Numero"')
    print("El numero secreto esta entre 1 y 50.")

    numero_secreto = random.randint(1, 50)
    intentos = 0

    while True:
        intentos += 1
        try:
            entrada = input(f"Intento {intentos} - Ingresa tu número: ")
            numero = float(entrada)

            if numero < 1 or numero > 50:
                print("Ingresa un número dentro del rango 1-50.")
                continue

            if numero < numero_secreto:
                print("El número secreto es mayor.")
            elif numero > numero_secreto:
                print("El número secreto es menor.")
            else:
                print(f"¡Felicidades! Has adivinado el número secreto: {numero_secreto}")
                break
        except ValueError:1
        
        print("Entrada inválida. Por favor, ingresa un número entero.")

adivina_el_numero()
#/////////////////////////////////////////////////////////////////////////////////////////////////////////
#6. Calculadora Factorial
def calcular_factorial():
    try:
        numero = input("Ingrese un número entero para calcular su factorial: ")
        numero = int(numero)

        if numero < 0:
            raise ValueError("El número no puede ser negativo.")

        factorial = 1
        for i in range(1, numero + 1):
            factorial *= i

        print(f"El factorial de {numero} es {factorial}")

    except ValueError as e:
        print(f"Error: {e}")

calcular_factorial()
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#7. Manejo de fechas y horas
from datetime import datetime

def calcularDias(fecha_str):
    try:
        fecha_ingresada = datetime.strptime(fecha_str, "%d/%m/%Y")
        fecha_actual = datetime.now()
        diferencia = (fecha_ingresada - fecha_actual).days
        return diferencia

    except ValueError:
        return None

def fecha_solicitada ():
    while True:
        fecha_str = input("Ingrese una fecha en formato DD/MM/AAAA: ")
        dias_faltantes = calcularDias(fecha_str)
        
        if dias_faltantes is None:
            print("Error: El formato de la fecha es incorrecto. Tiene que usar el formato DD/MM/AAAA.")
        else:
            if dias_faltantes > 0:
                print(f"Faltan {dias_faltantes} días para la fecha {fecha_str}.")
            elif dias_faltantes == 0:
                print("La fecha ingresada es hoy.")
            else:
                print(f"La fecha {fecha_str} ya ha pasado.")
            break
fecha_solicitada()
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#8. Registro de estudiantes
def agregar_estudiante(registro):
    nombre = input("Ingrese el nombre del estudiante: ")
    calificacion = float(input("Ingrese la calificación del estudiante: "))
    registro[nombre] = calificacion
    print(f"Estudiante agregado: {nombre} - {calificacion}")

def actualizar_calificacion(registro):
    nombre = input("Ingrese el nombre del estudiante: ")
    if nombre in registro:
        calificacion = float(input("Ingrese la nueva calificación: "))
        registro[nombre] = calificacion
        print(f"Estudiante actualizado: {nombre} - {calificacion}")
    else:
        print("Error: Estudiante no encontrado.")

def eliminar_estudiante(registro):
    nombre = input("Ingrese el nombre del estudiante a eliminar: ")
    if nombre in registro:
        del registro[nombre]
        print(f"Estudiante eliminado: {nombre}")
    else:
        print("Error: Estudiante no encontrado.")

def listar_estudiantes(registro):
    if registro:
        print("Registro de estudiantes:")
        for nombre, calificacion in registro.items():
            print(f"{nombre}: {calificacion}")
    else:
        print("No hay estudiantes registrados.")

def estudiantes():
    registro = {'Juan': 90, 'Roberto': 78, 'Danna': 85}  
    print("Registro de estudiantes inicial:", registro)

    while True:
        print("\nMenú:")
        print("1. Agregar estudiante")
        print("2. Actualizar calificación")
        print("3. Eliminar estudiante")
        print("4. Listar estudiantes")
        print("5. Salir")
        
        try:
            opcion = int(input("Opción: "))
            if opcion == 1:
                agregar_estudiante(registro)
            elif opcion == 2:
                actualizar_calificacion(registro)
            elif opcion == 3:
                eliminar_estudiante(registro)
            elif opcion == 4:
                listar_estudiantes(registro)
            elif opcion == 5:
                print("Fianalizo el programa.")
                break
            else:
                print("Error: Opción no válida. Por favor, seleccione una opción del 1 al 5.")
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")

estudiantes()
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////
#9. Generador de contraseñas
import random
import string

def generarContraseña(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def solicitarLongitud():
    while True:
        try:
            longitud = int(input("Ingrese la longitud de la contraseña: "))
            if longitud <= 0:
                print("Error: La longitud no puede ser un numero negativo, Intente de nuevo.")
                continue
            
            contrasena = generarContraseña(longitud)
            print(f"Contraseña generada: {contrasena}")

        except ValueError:
            print("Error: Por favor, ingrese un número entero válido.")
        break 

solicitarLongitud()
#//////////////////////////////////////////////////////////////////////////////////////////
#Buscador de archivos
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
    subcadena = input("Ingrese la Subcadena a Buscar: ")
    buscar_archivos(directorio, subcadena)

solicitar_busqueda() 

