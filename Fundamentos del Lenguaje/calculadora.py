import matematicas 

numero = 0
print("Opciones:\n 1. Sumar\n 2. Restar\n 3. Multiplicar\n 4. Dividir")


while numero != 5:
    numero = int(input("Que desea realizar"))
    if numero == 1 :
        a = int(input("primer numero"))
        b = int(input("segundo numero"))
        print(matematicas.sumar(a,b))
    elif numero == 2:
        a = int(input("primer numero"))
        b = int(input("segundo numero"))
        print(matematicas.restar(a,b))
    elif numero == 3:
        a = int(input("primer numero"))
        b = int(input("segundo numero"))
        print(matematicas.multiplicar(a,b))
    elif numero == 4:
        a = int(input("primer numero"))
        b = int(input("segundo numero"))
        print(matematicas.dividir(a,b))
 