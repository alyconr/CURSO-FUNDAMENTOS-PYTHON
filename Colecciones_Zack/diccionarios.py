# Diccionario inicial de español a inglés
traductor = {"hola": "hello", "mundo": "world", "casa": "house"}
print(f"Diccionario inicial: {traductor}")

while True:
    palabra_espanol = input("Ingrese una palabra en español (o 'salir' para terminar): ").lower()

    if palabra_espanol == "salir":
        print("Terminando el programa.")
        break

    if palabra_espanol in traductor:
        traduccion = traductor[palabra_espanol]
        print(f"La traducción de '{palabra_espanol}' es: {traduccion}")
    else:
        print(f"La palabra '{palabra_espanol}' no se encuentra en el diccionario.")
        nueva_traduccion = input(f"Ingrese la traducción de '{palabra_espanol}': ").lower()
        traductor[palabra_espanol] = nueva_traduccion
        print(f"Nueva entrada agregada: '{palabra_espanol}': '{nueva_traduccion}'")