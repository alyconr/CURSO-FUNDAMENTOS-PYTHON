#1. Leer un número y presentar la tabla de multiplicar de ese número entre 1 y 10. Utilizar el siguiente formato de ejemplo:
#1 x 1 = 1
#1 x 2 = 2
#1 x 3 = 3
#1 x 4 = 4
#1 x 5 = 5


numero = int(input("Introduce un número para mostrar su tabla de multiplicar: "))


for i in range(1, 11): 
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    

#2. En un partido de fútbol, se ofrece un descuento a los aficionados que depende del estrato y la edad. 
# Si el estrato es 1 y su edad es menor a 18 el descuento será del 20% sobre el valor de la boleta. 
# Si el estrato es 1 y el alumno tiene 18 o mas años, el descuento será del 15%. Si el estrato es 2 y la edad 
# es menor a 18 años, el descuento será del 10% y si el estrato es 2 y la edad es 18 años o más, el descuento 
# será del 5%. Determinar el total del dinero recaudado y descontado por las últimas N personas que ingresan 
# al partido.



total_recaudado = 0
total_descuento = 0
N = int(input("¿Cuántas personas ingresarán al partido? "))


for _ in range(N):
    estrato = int(input("Introduce el estrato (1 o 2): "))
    edad = int(input("Introduce la edad: "))
    valor_boleta = 10000  

    if estrato == 1:
        if edad < 18:
            descuento = 0.20
        else:
            descuento = 0.15
    elif estrato == 2:
        if edad < 18:
            descuento = 0.10
        else:
            descuento = 0.05
    else:
        descuento = 0  
    precio_final = valor_boleta * (1 - descuento)
    total_recaudado += precio_final
    total_descuento += valor_boleta * descuento

print(f"Total recaudado: {total_recaudado}")
print(f"Total descontado: {total_descuento}")

#3. Leer un password de ingreso a un programa y mostrar el mensaje de bienvenida si es correcto. 
# Mientras no lo sea, debe mostrar el mensaje de Password incorrecto. El programa debe terminar 
# automáticamente al quinto intento fallido.


password_correcto = "mi_contraseña"  
intentos = 0


while intentos < 5:  
    password = input("Introduce la contraseña: ")
    
    if password == password_correcto:
        print("¡Bienvenido!")
        break 
    else:
        print("Password incorrecto.")
        intentos += 1  

if intentos == 5:
    print("Has alcanzado el número máximo de intentos.")
    