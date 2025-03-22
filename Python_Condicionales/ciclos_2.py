N = int(input("Ingresa el número de personas: "))
valor_boleta = float(input("Ingresa el valor de la boleta: "))

total_recaudado = 0
total_descuento = 0

for i in range(N):
    estrato = int(input("Ingresa el estrato (1 o 2): "))
    edad = int(input("Ingresa la edad: "))

    descuento = 0
    if estrato == 1:
        descuento = valor_boleta * (0.20 if edad < 18 else 0.15)
    elif estrato == 2:
        descuento = valor_boleta * (0.10 if edad < 18 else 0.05)

    total_descuento += descuento
    total_recaudado += valor_boleta - descuento

print(f"Total recaudado: ${total_recaudado:.2f}")
print(f"Total descontado: ${total_descuento:.2f}")