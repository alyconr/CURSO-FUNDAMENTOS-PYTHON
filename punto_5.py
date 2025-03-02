def transformar_frase(frase):
  """Transforma una frase a mayúsculas sostenidas e invierte su contenido.

  Args:
    frase: La frase a transformar.

  Returns:
    La frase transformada.
  """

  frase_mayusculas = frase.upper()
  frase_invertida = frase_mayusculas[::-1]
  return frase_invertida

if __name__ == "__main__":
  frase_usuario = input("Introduce una frase: ")
  frase_transformada = transformar_frase(frase_usuario)
  print("Frase transformada:", frase_transformada)