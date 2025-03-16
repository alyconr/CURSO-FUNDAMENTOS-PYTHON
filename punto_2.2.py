# Crear una lista de números
mi_lista = [1, 2, 3, 4, 2, 5, 2, 6, 7, 2, 8]

# Solicitar un número al usuario
numero_a_borrar = int(input("Ingresa el número que deseas borrar de la lista: "))

# Borrar el número de la lista en todas sus posiciones
mi_lista = [numero for numero in mi_lista if numero != numero_a_borrar]

# Presentar la lista final
print("Lista final:", mi_lista)