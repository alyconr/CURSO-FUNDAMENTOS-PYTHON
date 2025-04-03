# Descripción: Se debe desarrollar un sistema que administre un inventario compuesto por distintos artículos. El programa permitirá a los usuarios agregar nuevos artículos y/o actualizar los ya existentes, así como eliminar productos. Además, se podrá consultar la cantidad de un producto específico, así como el total del inventario.

inventario = {}

# Solicitar cantidad de productos
cantidad = int(input("Ingrese la cantidad de productos que desea ingresar: "))

# Recopilar información de los productos
for i in range(1, cantidad + 1):
    producto = input(f"\nIngrese el nombre del producto {i}: ")
    existencia = int(input(f"Ingrese la existencia del {producto}: "))
    inventario[producto] = existencia

# Mostrar productos con stock menor que 10
print("\nProductos con stock menor que 10:")
for producto, existencia in inventario.items():
    if existencia < 10:
        print(producto, "tiene un stock menor que 10")

# Mostrar lista completa de productos con su existencia
print("\nLista de productos con sus existencias:")
for producto, existencia in inventario.items():
    print(f"{producto}: {existencia}")
