tareas = ["Comprar pan", "Lavar el coche - ✅", "Estudiar Python", "Pagar facturas - ✅", "Hacer ejercicio"]

print("Lista de actividades inicial:")
for i, tarea in enumerate(tareas):
    print(f"{i}: {tarea}")

tareas_pendientes = [tarea for tarea in tareas if "✅" not in tarea]

print("\nLista de actividades después del filtrado:")
for i, tarea in enumerate(tareas_pendientes):
    print(f"{i}: {tarea}")
