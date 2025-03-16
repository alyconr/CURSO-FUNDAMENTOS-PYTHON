# Inicialización de variables
temperatura = 75  # Temperatura inicial
motor_encendido = True  # El motor comienza encendido

# Bucle principal (simula la lectura continua de la temperatura)
while True:
    # Simulación de la lectura de la temperatura (en un sistema real, esto vendría de un sensor)
    temperatura = float(input("Ingrese la temperatura actual: "))

    print(f"Temperatura actual: {temperatura} grados")

    # Condicional para apagar el motor
    if temperatura > 80:
        motor_encendido = False
        print("¡Alerta! Temperatura alta. Motor apagado.")
    else:
        motor_encendido = True
        print("Temperatura normal. Motor encendido.")

    # Mostrar el estado del motor
    if motor_encendido:
        print("Estado del motor: Encendido")
    else:
        print("Estado del motor: Apagado")

    # Puedes agregar aquí un tiempo de espera (por ejemplo, time.sleep()) para simular un ciclo de control
