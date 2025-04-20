"""
Ejercicio 2: Administrador de Inventarios
Descripción:
Desarrolla un sistema para gestionar el inventario de productos usando un diccionario donde cada clave es el nombre del producto y su valor la cantidad en stock.
Implementa funciones para agregar, actualizar y eliminar productos.
Utiliza estructuras de control para recorrer y mostrar el inventario.
Incluye manejo de excepciones para capturar intentos de actualizar o eliminar un producto inexistente.
Ejemplo de salida:
Inventario inicial: {'manzanas': 50, 'naranjas': 30, 'peras': 20} Actualizando stock de 'peras' a 25... Producto 'bananas' agregado con 40 unidades. Eliminando 'naranjas'... Inventario final: {'manzanas': 50, 'peras': 25, 'bananas': 40}
"""

inventario = {"manzanas": 50, "naranjas": 30, "peras": 20}


def mostrar_inventario():

    print("Inventario actual:", inventario)

def agregar_producto(nombre, cantidad):
    
    inventario[nombre] = inventario.get(nombre, 0) + cantidad
    print(f"Producto '{nombre}' agregado con {cantidad} unidades.")

def actualizar_producto(nombre, cantidad):

    if nombre in inventario:
        inventario[nombre] = cantidad
        print(f"Actualizando stock de '{nombre}' a {cantidad}...")
    else:
        raise KeyError(f"El producto '{nombre}' no existe en el inventario.")

def eliminar_producto(nombre):

    if nombre in inventario:
        del inventario[nombre]
        print(f"Eliminando '{nombre}'...")
    else:
        raise KeyError(f"El producto '{nombre}' no existe en el inventario.")

print("Inventario inicial:", inventario)

try:
        actualizar_producto('peras', 60)
        agregar_producto('bananas', 10)
        eliminar_producto('manzanas')
except KeyError as e:
        print(e)

mostrar_inventario()