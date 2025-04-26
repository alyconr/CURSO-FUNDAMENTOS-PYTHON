#ejercicio2
# Administrador de inventarios 
# Sistema de Administración de Inventarios

inventario = {'manzanas': 50, 'naranjas': 30, 'peras': 20}
def mostrar_inventario(inv):
    print("Inventario actual:")
    for producto, cantidad in inv.items():
        print(f"- {producto}: {cantidad} unidades")
    print() 

def agregar_producto(inv, producto, cantidad):
    try:
        cantidad = int(cantidad)
        if cantidad < 0:
            print(f"Error: La cantidad debe ser un número positivo")
            
            return inv
        
        if producto in inv:
            print(f"El producto '{producto}' ya existe en el inventario. Utilice la función actualizar.")
        else:
            inv[producto] = cantidad
            print(f"Producto '{producto}' agregado con {cantidad} unidades.")
    except ValueError:
        print("Error: La cantidad debe ser un número entero")
    
    return inv

def actualizar_producto(inv, producto, cantidad):
    try:
        cantidad = int(cantidad)
        if cantidad < 0:
            print(f"Error: La cantidad debe ser un número positivo")

            return inv
        
        if producto in inv:
            inv[producto] = cantidad
            print(f"Actualizando stock de '{producto}' a {cantidad}...")
        else:
            print(f"Error: El producto '{producto}' no existe en el inventario")
    except ValueError:
        print("Error: La cantidad debe ser un número entero")
    
    return inv


def eliminar_producto(inv, producto):
    if producto in inv:
        del inv[producto]
        print(f"Eliminando '{producto}'...")
    else:
        print(f"Error: El producto '{producto}' no existe en el inventario")

    return inv


print("Inventario inicial:", inventario)
print()
mostrar_inventario(inventario)
inventario = actualizar_producto(inventario, 'peras', 25)
inventario = agregar_producto(inventario, 'bananas', 40)
inventario = eliminar_producto(inventario, 'naranjas')
inventario = eliminar_producto(inventario, 'uvas')
print("\nInventario final:", inventario)