import emoji

# Texto con nombres de emojis
texto = "Hola, quiero una :pizza: y un :ice_cream:!"

# Convertir nombres de emojis a símbolos
texto_con_emojis = emoji.emojize(texto)

print(texto_con_emojis)