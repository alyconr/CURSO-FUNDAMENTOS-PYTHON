def inspeccionar_pieza(estándares):
    """
    Inspecciona una pieza según los estándares de calidad.

    Args:
        estándares (str): Una cadena binaria donde 1 significa estándar cumplido y 0 no cumplido.

    Returns:
        bool: True si la pieza es aprobada, False si es rechazada.
    """

    for estándar in estándares:
        if estándar == '0':
            print("¡Alerta! Estándar de calidad no cumplido.")
            return False  # Rechazar la pieza

    return True  # Aprobar la pieza

# Ejemplo de uso
estándares_pieza = input("Ingrese los estándares de calidad (ej: 1101): ")

if inspeccionar_pieza(estándares_pieza):
    print("Pieza aprobada. Continuar con la producción.")
else:
    print("Pieza rechazada. Enviando alerta al operador.")