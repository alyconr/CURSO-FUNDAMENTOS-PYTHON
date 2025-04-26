# Preferencias musicales de los dos grupos
preferencias_grupo_a = {'rock', 'pop', 'jazz'}
preferencias_grupo_b = {'pop', 'reggae', 'electrónica'}

print(f"Preferencias Grupo A: {preferencias_grupo_a}")
print(f"Preferencias Grupo B: {preferencias_grupo_b}")

# Verificar si tienen géneros en común
tienen_comun = not preferencias_grupo_a.isdisjoint(preferencias_grupo_b)
print(f"\n¿Tienen géneros en común? {'Sí' if tienen_comun else 'No'}")

# Calcular la intersección (géneros comunes)
generos_comunes = preferencias_grupo_a.intersection(preferencias_grupo_b)
print(f"Géneros comunes: {generos_comunes}")

# Calcular la unión de géneros
union_generos = preferencias_grupo_a.union(preferencias_grupo_b)
print(f"Unión de géneros: {union_generos}")

# Calcular la diferencia simétrica (géneros exclusivos)
diferencia_simetrica = preferencias_grupo_a.symmetric_difference(preferencias_grupo_b)
print(f"Géneros exclusivos (diferencia simétrica): {diferencia_simetrica}")