#Pregunte al usuario cuántos elementos desea ingresar en una lista, 
#luego solicite cada uno de ellos y presente el contenido de la lista y su contenido invertido.
n = int(input("¿Cuantas Elementos va ingresar? "))
lista = []
for i in range(n):
  elemento = input(f" elemento {i+1}: ")
  lista.append(elemento)

print("La lista original es: ", lista)
print("La lista invertida es: ", lista[::-1])



#Crear una lista de números y solicitar un número. Borrar de la lista ese número en todas las posiciones donde se encuentre. 
#Presentar la lista final

n = [1, 2, 3, 4, 2, 5, 2, 6]  
print("Lista original:", n)

b = int(input("Ingrese el número que desea borrar de la lista: "))

while b in n:
    n.remove(b)

print("La lista final es:", n)


#Solicite al usuario dos frases y devuelva una lista con todas las letras que se repiten en la misma posición de ambas listas
#ejemplo: frase1: "holasena" frase2: "todogana" salida: ["o","n", "a"]

frase1 = input("Ingrese su primera frase: ")
frase2 = input("Ingrese su segunda frase: ")

l_repetidas = []
l_minima = min(len(frase1), len(frase2))

for i in range(l_minima):
    if frase1[i] == frase2[i]:
        l_repetidas.append(frase1[i])

print("Letras repetidas en la misma posición:", l_repetidas) 