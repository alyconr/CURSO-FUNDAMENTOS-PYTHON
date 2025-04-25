"""
Descripción:
Desarrolla un conjunto de funciones para convertir unidades métricas. Por ejemplo:

De centímetros a pulgadas.
De kilómetros a millas.
Utiliza estructuras de control para verificar que la entrada sea numérica, y maneja excepciones cuando el usuario ingrese datos inválidos.
Ejemplo de salida:
Seleccione la conversión:

Centímetros a pulgadas

Kilómetros a millas Opción: 1 Ingrese la cantidad en centímetros: 100 Resultado: 100 cm = 39.37 pulgadas
"""

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