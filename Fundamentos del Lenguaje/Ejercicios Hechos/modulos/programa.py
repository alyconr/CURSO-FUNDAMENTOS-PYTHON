import matematicas

print(f"OPCIONES DE MENU: \n1. Suma \n2. Resta \n3. Multiplicacion \n4. Division \n5. Salir")

while True:
    
    opcion = int(input("Ingrese una opcion: "))
    
    if opcion == 1:
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))
        print(f"El resultado de la suma es: {matematicas.Suma(num1,num2)}")
        
    elif opcion == 2:
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))
        print(f"El resultado de la resta es: {matematicas.Resta(num1,num2)}")
        
    elif opcion == 3:
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))
        print(f"El resultado de la multiplicacion es: {matematicas.Multiplicacion(num1,num2)}")
        
    elif opcion == 4:
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))
        print(f"El resultado de la division es: {matematicas.Division(num1,num2)}")    
        
    elif opcion == 5:
        break