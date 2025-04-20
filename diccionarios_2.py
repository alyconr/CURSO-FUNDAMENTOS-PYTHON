# Inventario inicial de la tienda
inventario = {"manzanas": 50, "naranjas": 30, "peras": 20}
print(f"Inventario inicial:{inventario}\n")

# Consulta de stock
producto_consultar = "naranjas"
if producto_consultar in inventario:
    cantidad = inventario[producto_consultar]
    print(f"Consulta: ¿Cuántas {producto_consultar} hay? -> {cantidad}\n")
else:
    print(f"El producto '{producto_consultar}' no se encuentra en el inventario.\n")

# Actualización de stock
producto_actualizar = "peras"
nueva_cantidad = 25
if producto_actualizar in inventario:
    inventario[producto_actualizar] = nueva_cantidad
    print(f"Actualizando stock de {producto_actualizar} a {nueva_cantidad}.\n")
else:
    print(f"No se puede actualizar el stock de '{producto_actualizar}' porque no existe en el inventario.\n")

# Agregar nuevo producto
nuevo_producto = "bananas"
stock_nuevo_producto = 40
inventario[nuevo_producto] = stock_nuevo_producto
print(f'Agregando producto: "{nuevo_producto}" con stock {stock_nuevo_producto}.\n')

# Eliminar producto
producto_eliminar = "naranjas"
if producto_eliminar in inventario:
    del inventario[producto_eliminar]
    print(f'Eliminando producto: "{producto_eliminar}".\n')
else:
    print(f"No se puede eliminar '{producto_eliminar}' porque no existe en el inventario.\n")

# Mostrar inventario final
print(f"Inventario final:{inventario}")