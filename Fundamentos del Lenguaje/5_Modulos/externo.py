from matematicas import *

print(sumar(5, 6))
print(restar(5, 6))
print(Multiplicar(5, 6))
print(dividir(0, 9))

# APROPIACION
#Realiza una función llamada agregar_una_vez(lista, el) que reciba una lista y un elemento. La función debe añadir el elemento al final de la lista con la condición de no repetir ningún elemento. Además si este elemento ya se encuentra en la lista se debe invocar un error de tipo ValueError que debes capturar y mostrar este mensaje en su lugar:
#Error: Imposible añadir elementos duplicados => [elemento].
#Mostrar el siguiente mensaje siempre que se ejecute independientemente de que la ejecución haya sido exitosa o no
#Gracias por usar este programa



agregar(lista, 5)
agregar(lista, 2)
agregar(lista, 7)
agregar(lista, "Juan")
agregar(lista, "KrisR")
agregar(lista, "James")

print(lista)
print("Gracias por usar este programa")

import emoji

while True:
    estado = input("Como te sientes hoy? (feliz, triste, enojado, sorprendido, salir): ").lower()

    if estado == "feliz":
        print(emoji.emojize("Me alegra saber eso! :smile:", language="alias"))
    elif estado == "triste":
        print(emoji.emojize("Animo, todo mejora. :pensive:", language="alias"))
    elif estado == "enojado":
        print(emoji.emojize("Respira hondo. :angry:", language="alias"))
    elif estado == "sorprendido":
        print(emoji.emojize("Wow! Que sorpresa! :open_mouth:", language="alias"))
    elif estado == "salir":
        print(emoji.emojize("Hasta pronto! :wave:", language="alias"))
        break
    else:
        print(emoji.emojize("No entendi tu emocion, pero te mando un abrazo! :hugging_face:", language="alias"))