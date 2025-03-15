def main():
    print("CÁLCULO DE CALIFICACIÓN FINAL EN MATEMÁTICAS")
    print("===========================================")
    
    try:
        # Leer las tres calificaciones parciales
        parcial1 = float(input("Ingrese la calificación del primer parcial: "))
        parcial2 = float(input("Ingrese la calificación del segundo parcial: "))
        parcial3 = float(input("Ingrese la calificación del tercer parcial: "))
        
        # Leer calificación del examen final
        examen_final = float(input("Ingrese la calificación del examen final: "))
        
        # Leer calificación del trabajo final
        trabajo_final = float(input("Ingrese la calificación del trabajo final: "))
        
        # Validar que las calificaciones estén en el rango adecuado (0-10 o 0-100)
        max_calif = 100 if (parcial1 > 10 or parcial2 > 10 or parcial3 > 10 or examen_final > 10 or trabajo_final > 10) else 10
        
        if (parcial1 < 0 or parcial1 > max_calif or 
            parcial2 < 0 or parcial2 > max_calif or 
            parcial3 < 0 or parcial3 > max_calif or 
            examen_final < 0 or examen_final > max_calif or 
            trabajo_final < 0 or trabajo_final > max_calif):
            print(f"Error: Las calificaciones deben estar en el rango de 0 a {max_calif}.")
            return
        
        # Calcular el promedio de los parciales
        promedio_parciales = (parcial1 + parcial2 + parcial3) / 3
        
        # Calcular la calificación final según los porcentajes
        # 55% parciales + 30% examen final + 15% trabajo final
        calificacion_final = (promedio_parciales * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15)
        
        # Mostrar resultados
        print("\nRESULTADOS:")
        print(f"Promedio de parciales: {promedio_parciales:.2f}")
        print(f"Examen final: {examen_final:.2f}")
        print(f"Trabajo final: {trabajo_final:.2f}")
        print(f"Calificación final: {calificacion_final:.2f}")
        
    except ValueError:
        print("Error: Por favor ingrese valores numéricos válidos para las calificaciones.")
    except Exception as e:
        print(f"Error inesperado: {e}")
        
    # Mantener la consola abierta
    input("\nPresione Enter para finalizar...")

# Ejecutar el programa
if __name__ == "__main__":
    main()