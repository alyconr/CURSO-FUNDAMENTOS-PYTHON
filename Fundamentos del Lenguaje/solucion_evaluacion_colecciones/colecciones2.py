# Descripción: Crea una aplicación que solicite al usuario una palabra y, a continuación, le pida ingresar un texto. El programa deberá buscar la palabra en el texto ingresado y mostrar cuántas veces aparece dicha palabra en el texto.

# Paso 1: Pedir el texto al usuario
parrafo = input("Ingrese cualquier tipo de cadena de texto: ")
parrafo = parrafo.lower()

# Paso 2 y 3: Reemplazar signos de puntuación por espacios y dividir en palabras
for signo in ".,;:¡!¿?()[]{}\"'":
    parrafo = parrafo.replace(signo, " ")

palabras_limpias = parrafo.split()

# Paso 4: Pedir la palabra a buscar
palabra_buscar = input("Ingrese la palabra que desea buscar: ").lower()

# Paso 5: Buscar la palabra en la lista
conteo = 0
posiciones = []

for i in range(len(palabras_limpias)):
    if palabras_limpias[i] == palabra_buscar:
        conteo += 1
        posiciones.append(i)

# Paso 6: Mostrar el resultado
if conteo > 0:
    print(
        f'La palabra "{palabra_buscar}" aparece {conteo} veces en las posiciones {posiciones}.')
else:
    print(f'La palabra "{palabra_buscar}" no se encontró en el texto.')
