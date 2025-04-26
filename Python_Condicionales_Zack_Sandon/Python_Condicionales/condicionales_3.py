entrada_binaria = input("Ingresa la secuencia binaria de inspección (ej: 1101): ")

pieza_aprobada = True  # Asumimos que la pieza está aprobada inicialmente

for bit in entrada_binaria:
    if bit == '0':
        pieza_aprobada = False  # Si encontramos un 0, la pieza no cumple los estándares
        break  # Salimos del bucle, no es necesario verificar más

if pieza_aprobada:
    print("Pieza aprobada.")
    print("Continuando con la producción.")
ifno:
    print("Pieza rechazada.")
    print("Alerta enviada al operador.")