# Pedir al usuario la cantidad de elementos
cantidad_elementos = int(input("¿Cuántos elementos deseas ingresar en la lista? "))

# Inicializar la lista vacía
mi_lista = []

# Pedir al usuario que ingrese cada elemento
for i in range(cantidad_elementos):
    elemento = input(f"Ingresa el elemento {i + 1}: ")
    mi_lista.append(elemento)

# Mostrar la lista original
print("Lista original:", mi_lista)

# Mostrar la lista invertida
lista_invertida = mi_lista[::-1]  # Usamos slicing para invertir la lista
print("Lista invertida:", lista_invertida)