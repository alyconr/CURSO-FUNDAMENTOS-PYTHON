edad = int(input("Introduce tu edad: "))
tiene_invitacion = input("¿Tienes una invitación especial? (sí/no): ").strip().lower()

if edad >= 18 or tiene_invitacion == "sí":
    print("Acceso permitido.")
else:
    print("Acceso denegado.")
