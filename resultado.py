import matematicas 

numero = 0
print("Opciones:\n 1. Sumar\n 2. Restar\n 3. Multiplicar\n 4. Dividir")


while numero != 5:
    numero = int(input("Que desea realizar"))
    if numero == 1 :
        a = int(input("primer numero"))
        b = int(input("segundo numero"))
        print(matematicas.suma(a,b))
    elif numero == 2:
        a = int(input("primer numero"))
        b = int(input("segundo numero"))
        print(matematicas.resta(a,b))
    elif numero == 3:
        a = int(input("primer numero"))
        b = int(input("segundo numero"))
        print(matematicas.multiplicacion(a,b))
        
    elif numero == 4:
        a = int(input("primer numero"))
        b = int(input("segundo numero"))
        print(matematicas.division(a,b))
print("Resta:", matematicas.resta(a, b))
print("Multiplicación:", matematicas.multiplicacion(a, b))
print("División:", matematicas.division(a, b))