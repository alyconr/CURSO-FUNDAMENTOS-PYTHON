#Recibir una frase y transformarla a mayúscula sostenida e invirtiendo su contenido

frase_usuario = input("Ingrese una frase: ")

frase_mayuscula = frase_usuario.upper()
frase_invertida = frase_mayuscula[::-1]

print("Frase transformada:", frase_invertida)