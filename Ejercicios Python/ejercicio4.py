#Recibir una frase por parte del usuario y devolver el número de palabras que se encuentran en la frase.
Frase_Usuario = input("Ingrese una frase: ")

Numero_Palabras = len(Frase_Usuario.split())

print(f"El número de palabras en la frase es:{Numero_Palabras}")