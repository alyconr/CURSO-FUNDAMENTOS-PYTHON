def operaciones_matematicas():
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        
        suma = num1 + num2
        print(f"La suma de {num1} y {num2} es: {suma}")
        
        resta = num1 - num2
        print(f"La resta de {num1} y {num2} es: {resta}")
        
        multiplicacion = num1 * num2
        print(f"La multiplicación de {num1} y {num2} es: {multiplicacion}")
        
        if num2 != 0:
            division = num1 / num2
            print(f"La división de {num1} entre {num2} es: {division}")
        else:
            print("Error: No se puede dividir entre cero.")
    
    except ValueError:
        print("Error: Por favor, ingrese números válidos.")

operaciones_matematicas()
