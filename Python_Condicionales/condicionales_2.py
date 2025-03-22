estrato_estudiante = int(input("Introduce su estrato: "))
edad_estudiante = int(input("Introduce su edad: "))
valor_matricula_estudiante = float(input("Introduce valor de la matricula: "))

descuento = 0.0

if estrato_estudiante == 1:
    if edad_estudiante < 18:
        descuento = valor_matricula_estudiante * 0.20 
    else:
        descuento = valor_matricula_estudiante * 0.15  
elif estrato_estudiante == 2:
    if edad_estudiante < 18:
        descuento = valor_matricula_estudiante * 0.10  
    else:
        descuento = valor_matricula_estudiante * 0.05  
print(f"El descuento aplicado es de: ${descuento}")
print(f"El valor total a pagar es de: ${valor_matricula_estudiante - descuento}")