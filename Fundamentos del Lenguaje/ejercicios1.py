#1.  En un sistema de automatización industrial, un motor puede estar encendido o apagado. 
# Si la temperatura de la máquina supera los 80 grados, el motor debe apagarse automáticamente. 
# Escribir un programa que controle el estado del motor y lo apague si la temperatura supera los 80 grados.
temp_maquina = int(input("ingrece si el motor encendico(1) o apagado(0) : "))
if temp_maquina == 0:
    print("la maquina esta apagada, por favor enciendela")
elif temp_maquina == 1:
    temp_maquina = int(input("la maquina esta necendida, ingrese cual es su temperatura   "))
    if temp_maquina >= 80:
        print ("la temperatura es muy alta  el motor se apago")
    if temp_maquina < 80:
        print("la temperatura es normal el motor seguira encendido")
#2.Una universidad ofrece un descuento a los estudiantes que depende del estrato y la edad. 
# Si el estrato es 1 y su edad es menor a 18 el descuento será del 20% sobre el valor de la matrícula. 
# Si el estrato es 1 y el alumno tiene 18 o mas años, el descuento será del 15%. Si el estrato es 2 y 
# la edad es menor a 18 años, el descuento será del 10% y si el estrato es 2 y la edad es 18 años o mas, 
# el descuento será del 5%.

v_m = float(input("Ingrese el cual es el valor de su matrícula: "))
estrato = int(input("Ingrese el estrato del estudiante (1 o 2): "))
edad = int(input("Ingrese la edad del estudiante: "))

desc = 0

if estrato == 1:
    if edad < 18:
        desc = 0.20
    else:
        desc = 0.15
elif estrato == 2:
    if edad < 18:
        desc = 0.10
    else:
        desc = 0.05
else:
    print("Estrato inválido. Ingrese 1 o 2.")


v_desc = v_m * desc
precio_final = v_m - v_desc

print("Valor del descuento:", v_desc)
print("Precio final de la matrícula:", precio_final)


#3. En un sistema de control de calidad, se deben inspeccionar las piezas de un producto para determinar 
# si cumplen con los estándares de calidad. Si la pieza es defectuosa, se debe marcar como rechazada y 
# enviar una alerta al operador. Si la pieza cumple con los estándares de calidad, se debe marcar como 
# aprobada y continuar con la producción.
#Realice un programa que lea una entrada binaria en la que los 1s significan estándares de calidad cumplidos 
# y los 0s significan estándares de calidad No cumplidos. El programa debe rechazar la pieza ante cualquier 
# estándar no cumplido.

num_piezas = int(input("Ingrese el número de piezas: "))

for i in range(num_piezas):
    pieza = input("Ingrese los estándares de calidad (binario): ")

    if pieza == "0" * len(pieza) or pieza == "1" * len(pieza):
        if "0" in pieza:
            print("La pieza ha sido rechazada.")
            break
        else:
            print("La pieza ha sido aprobada.")
    else:
        print("Error: Entrada inválida. Solo se permiten 0s y 1s.")
        