#1. Leer una frase y devolver el 
#conjunto de caracteres que se encuentran presentes en la frase.

frase = input("ingrese una frase :")

lestras_dis = set(frase)
letras_ordenadas =  sorted(lestras_dis)
print(f"Su frase {frase} segmentada es {letras_ordenadas} ")





#2. En una escuela se permite la inscripcion de sus alumnos  a
#las siguientes actividades: Futbol(f), baloncesto(b). realize un programa que permita ingresar el nombre de 
#sus estudiantes  e inscribir a cada uno en uno de los dos deportes la aplicacion debe mostrar los sigientes listados:

#Estudiantes inscritos en  Futbolo, Estudiantes inscritos en Baloncesto, Estudiantes inscritos en ambos deportes, Todos los estudiantes inscritos en algun
#deporte, Estudiantes inscritos solo en un deporte.Genera un menú  con las opciones de aplicacion

baloncesto = set()

futbol = set()

numero_estudiantes = int(input("Ingrese el numero de estudiantes"))

for estudiantes in range(numero_estudiantes):
  nom = input("ingrese el nombre: ")
  seleccion = input("a que deporte se inscribira: Futbol(f), Baloncesto(b), Ambos(a), salir(s)").lower()
  if seleccion == 'f':
      futbol.add(nom)
  
  elif seleccion == 'b':
       baloncesto.add(nom)

  elif seleccion == 'a':
       futbol.add(nom)
       baloncesto.add(nom)
  else:
    print("No se agrego ninguna inscripcion")

print("futbol", futbol)
print("Baloncesto", baloncesto)
print("ambos", futbol.intersection(baloncesto))
print("algunos", futbol.union(baloncesto))
print("solo uno", futbol.symmetric_difference(baloncesto))
  




#3

frutas = {"Manzana": "Apple","Piña": "Pineaple","Banana" : "Banana"}
nombre_fruta = input("Ingrese el nombre de la fruta que quiere traducir: ")

if nombre_fruta == "Manzana":
  print(f"La traduccion de manzana es:",frutas["Manzana"])
elif nombre_fruta == "Piña":
  print(f"La traduccion de piña es:",frutas["Piña"])
elif nombre_fruta == "Banana":
  print(f"La traduccion de Banana es:",frutas["Banana"])
else:
    print("No se encuentra la traduccion de la fruta")