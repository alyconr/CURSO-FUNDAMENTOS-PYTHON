#Ejercicio 2: Administrador de Inventarios 
#Desarrolla un sistema para gestionar el inventario de productos usando un diccionario donde cada clave es el nombre del producto y su valor la cantidad en stock.

#Implementa funciones para agregar, actualizar y eliminar productos.
#Utiliza estructuras de control para recorrer y mostrar el inventario.
#Incluye manejo de excepciones para capturar intentos de actualizar o eliminar un producto inexistente.

# Diccionario inicial
inventario = {
    'manzanas': 50,
    'naranjas': 30,
    'peras': 20
}

# Función para mostrar el inventario
def mostrar_inventario():
    print("Inventario actual:")
    for producto, cantidad in inventario.items():
        print(f"- {producto}: {cantidad} unidades")
    print()  # Línea en blanco

# Función para agregar un producto
def agregar_producto(nombre, cantidad):
    if nombre in inventario:
        print(f"El producto '{nombre}' ya existe. Usa actualizar_producto para cambiar su cantidad.")
    else:
        inventario[nombre] = cantidad
        print(f"Producto '{nombre}' agregado con {cantidad} unidades.")

# Función para actualizar un producto
def actualizar_producto(nombre, cantidad):
    try:
        inventario[nombre] = cantidad
        print(f"Actualizando stock de '{nombre}' a {cantidad} unidades.")
    except KeyError:
        print(f"Error: El producto '{nombre}' no existe en el inventario.")

# Función para eliminar un producto
def eliminar_producto(nombre):
    try:
        del inventario[nombre]
        print(f"Eliminando '{nombre}' del inventario...")
    except KeyError:
        print(f"Error: No se puede eliminar '{nombre}' porque no existe.")

# --- EJECUCIÓN DE FUNCIONES ---

print("Inventario inicial:")
mostrar_inventario()

# Actualizar
actualizar_producto('peras', 25)

# Agregar nuevo producto
agregar_producto('bananas', 40)

# Eliminar producto
eliminar_producto('naranjas')

# Mostrar inventario final
print("Inventario final:")
mostrar_inventario()
