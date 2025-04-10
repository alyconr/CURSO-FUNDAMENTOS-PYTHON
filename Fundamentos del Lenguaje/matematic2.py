import Matematic

numero1 = 9
numero2 = 2

if numero1 > 15:
    print(Matematic.div(numero1, numero2))
elif numero1 > 10:
    print(Matematic.multi(numero1, numero2))
elif numero1 > 5:
    print(Matematic.resta(numero1, numero2))
elif numero1 > 0:
    print(Matematic.suma(numero1, numero2))
else:
    print("El numero no es valido")