# Lista original de códigos de productos con duplicados
lista_productos = [101, 102, 103, 101, 104, 105, 103]
print(f"Lista original de productos: {lista_productos}")

# Convertir la lista a un conjunto para eliminar duplicados
inventario_original = set(lista_productos)
print(f"Inventario original: {inventario_original}")

# Agregar un nuevo producto
nuevo_producto = 110
inventario_original.add(nuevo_producto)
print(f"Inventario tras agregar producto {nuevo_producto}: {inventario_original}")

# Descartar un producto específico
producto_a_descartar = 103
inventario_original.discard(producto_a_descartar)
print(f"Inventario tras descartar producto {producto_a_descartar}: {inventario_original}")

print("\n--- Comparación de inventarios ---")

# Definir los inventarios de los dos almacenes
inventario_almacen_a = {101, 102, 104, 110}
inventario_almacen_b = {102, 104, 107, 110}
print(f"Inventario Almacén A: {inventario_almacen_a}")
print(f"Inventario Almacén B: {inventario_almacen_b}")

# Identificar productos comunes (intersección)
productos_comunes = inventario_almacen_a.intersection(inventario_almacen_b)
print(f"Productos comunes: {productos_comunes}")

# Identificar productos exclusivos del Almacén A (diferencia)
productos_exclusivos_a = inventario_almacen_a.difference(inventario_almacen_b)
print(f"Productos exclusivos en Almacén A: {productos_exclusivos_a}")

# Identificar productos exclusivos del Almacén B (diferencia)
productos_exclusivos_b = inventario_almacen_b.difference(inventario_almacen_a)
print(f"Productos exclusivos en Almacén B: {productos_exclusivos_b}")
