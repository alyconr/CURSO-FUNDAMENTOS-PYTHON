entrada_binaria = input("Ingresa la secuencia binaria de inspección (ej: 1101): ")

pieza_aprobada = True  

for bit in entrada_binaria:
    if bit == '0':
        pieza_aprobada = False  
        break  

if pieza_aprobada:
    print("Pieza aprobada.")
    print("Continuando con la producción.")
else:
    print("Pieza rechazada.")
    print("Alerta enviada al operador.")