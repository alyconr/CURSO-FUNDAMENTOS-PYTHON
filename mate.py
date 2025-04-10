def suma(x,y):
    return x+y

def resta(x,y):
    return x-y

def multiplicacion(x,y):
    return x*y

def divi(x,y):
    try:
       resultado= x/y
       return resultado
    except ZeroDivisionError:
        return "No se puede dividir entre 0"
    
