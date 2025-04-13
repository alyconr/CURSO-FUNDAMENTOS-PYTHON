def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def Multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def agregar(lista, el):
    try:
        if el in lista:
            raise ValueError(f"Imposible añadir elementos duplicados => [{el}]")
        lista.append(el)
    except ValueError as tin:
        print(f"Error: ", tin)

lista = [1, 2, 3, 4, 5, 6, "James"]

