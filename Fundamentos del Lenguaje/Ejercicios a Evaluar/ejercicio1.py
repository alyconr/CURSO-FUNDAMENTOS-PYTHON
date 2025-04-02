productos = ["peras", "piñas", "manzanas", "bananos"]
unidades = [20, 20, 30, 5]
stock = 10

for i in range(len (productos)):
    print(f"{i + 1}. {productos [i]}: {unidades [i]} ")
    if unidades [i] < stock:
        print("Productos con bajo stock: ")
        print(f"El producto {productos [i]} no tiene suficiente stock: {unidades[i]} unidades ")

producto_seleccionado = int(input("Ingrese el numero del producto que desea actualizar: "))

cantidad = int(input("Ingrese la nueva cantidad: "))

unidades[producto_seleccionado ] = cantidad

for i in range(len(productos)):
    print(f"{i + 1} {productos [i]}: {unidades[i]}")
    if unidades[i] < stock:
        print("Productos con bajo stock: ")
        print(f"El producto {productos [i]} no tiene suficiente stock: {unidades[i]} unidades ")