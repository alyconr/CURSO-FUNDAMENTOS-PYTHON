def mostrar_inventario(inventario):
    if not inventario:
        print("El inventario está vacío.")
        return
    print("Inventario actual:")
    for producto, cantidad in inventario.items():
        print(f"- {producto}: {cantidad}")

def agregar_producto(inventario, producto, cantidad):
    if producto in inventario:
        print(f"Advertencia: El producto '{producto}' ya existe en el inventario. Use 'actualizar_producto' para modificar la cantidad.")
    else:
        inventario[producto] = cantidad
        print(f"Producto '{producto}' agregado con {cantidad} unidades.")

def actualizar_producto(inventario, producto, nueva_cantidad):
    if producto in inventario:
        inventario[producto] = nueva_cantidad
        print(f"Stock de '{producto}' actualizado a {nueva_cantidad}.")
    else:
        print(f"Error: El producto '{producto}' no existe en el inventario.")

def eliminar_producto(inventario, producto):
    if producto in inventario:
        del inventario[producto]
        print(f"Producto '{producto}' eliminado del inventario.")
    else:
        print(f"Error: El producto '{producto}' no existe en el inventario.")

inventario = {'manzanas': 50, 'naranjas': 30, 'peras': 20}
print(f"Inventario inicial: {inventario}")

# Probando las funciones
actualizar_producto(inventario, 'peras', 25)
agregar_producto(inventario, 'bananas', 40)
eliminar_producto(inventario, 'naranjas')
eliminar_producto(inventario, 'uvas') 

print(f"Inventario final: {inventario}")
mostrar_inventario(inventario)