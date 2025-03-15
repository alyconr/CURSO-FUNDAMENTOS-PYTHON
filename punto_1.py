# Programa para calcular el índice de cosecha de un cultivo

def main():
    print("Programa para calcular el índice de cosecha de un cultivo")
    print("-------------------------------------------------------")
    
    # Solicitar datos al usuario con manejo simple de errores
    try:
        frutos_recolectados = float(input("Ingrese la cantidad de frutos recolectados: "))
        frutos_totales = float(input("Ingrese la cantidad total de frutos producidos: "))
        
        # Validar datos
        if frutos_recolectados < 0 or frutos_totales <= 0:
            print("Error: Los valores deben ser positivos y frutos totales debe ser mayor que cero")
            input("Presione Enter para salir...")
            return
        
        if frutos_recolectados > frutos_totales:
            print("Error: La cantidad de frutos recolectados no puede exceder el total producido")
            input("Presione Enter para salir...")
            return
        
        # Calcular el índice de cosecha
        indice = frutos_recolectados / frutos_totales
        
        # Clasificar el índice
        if indice >= 0.9:
            clasificacion = "Excelente"
        elif indice >= 0.8:
            clasificacion = "Muy buena"
        elif indice >= 0.7:
            clasificacion = "Buena"
        elif indice >= 0.5:
            clasificacion = "Regular"
        else:
            clasificacion = "Deficiente"
        
        # Mostrar resultados
        print("\nResultados:")
        print(f"Frutos recolectados: {frutos_recolectados}")
        print(f"Frutos totales producidos: {frutos_totales}")
        print(f"Índice de cosecha: {indice:.2f} ({indice*100:.1f}%)")
        print(f"Clasificación: {clasificacion}")
        
    except ValueError:
        print("Error: Por favor ingrese solo números")
    except Exception as e:
        print(f"Error inesperado: {e}")
    
    # Mantener la consola abierta
    input("\nPresione Enter para salir...")

# Ejecutar el programa
if __name__ == "__main__":
    main()