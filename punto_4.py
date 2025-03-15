def main():
    print("CONTADOR DE PALABRAS EN UNA FRASE")
    print("================================")
    
    # Solicitar la frase al usuario
    frase = input("Ingrese una frase: ")
    
    # Método 1: Usando split() para dividir la frase en palabras
    palabras = frase.split()
    numero_palabras = len(palabras)
    
    # Mostrar el resultado
    print("\nRESULTADO:")
    print(f"La frase: \"{frase}\"")
    print(f"Contiene {numero_palabras} palabra(s).")
    
    # Si hay palabras, mostrarlas numeradas
    if numero_palabras > 0:
        print("\nPalabras encontradas:")
        for i, palabra in enumerate(palabras, 1):
            print(f"{i}. {palabra}")
    
    # Mantener la consola abierta
    input("\nPresione Enter para finalizar...")

# Ejecutar el programa
if __name__ == "__main__":
    main()