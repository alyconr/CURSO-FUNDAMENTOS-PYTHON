"""
Consulte sobre algún paquete interesante en el PyPI instálelo y utilícelo en un programa. Presente el paquete usado y su utilidad y muestre su aplicación en el programa desarrollado.
"""


# Paquete utilizado: Rich
# Descripción: Rich es una biblioteca para Python que permite crear salidas de consola enriquecidas y coloridas. Facilita la creación de tablas, barras de progreso, mensajes de error y más, todo con un formato atractivo y fácil de leer.
from rich.console import Console
from rich.table import Table

def mostrar_tabla():
    console = Console()

    tabla = Table(title="Datos de Usuarios")

    tabla.add_column("Nombre", style="cyan", no_wrap=True)
    tabla.add_column("Edad", style="magenta")
    tabla.add_column("Ciudad", style="green")

    tabla.add_row("James", "17", "Bogota")
    tabla.add_row("Juan", "18", "Bogota")
    tabla.add_row("Gabriela", "17", "Bogota")

    console.print(tabla)

if __name__ == "__main__":
    console = Console()
    console.print("¡Bienvenido al programa!", style="bold yellow")
    mostrar_tabla()