#Realice un programa que calcule el índice de cosecha de un cultivo en función de la cantidad de frutos recolectados y la cantidad de frutos producidos en total.
Cantidad_frutas_recolectadas = int(input("ingrese cantidad de frutas recolectadas: "))
Cantidad_frutas_producidas= int(input("ingrese cantidad de frutas producidas: "))

Indice_de_cosecha = (Cantidad_frutas_recolectadas / Cantidad_frutas_producidas) * 100
print("El indice de cosecha es: " , Indice_de_cosecha , "%")