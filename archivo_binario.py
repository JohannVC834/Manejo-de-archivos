
with open("vaca.jpg", "rb") as archivo_binario:
    contenido_binario = archivo_binario.read()


with open("copia_vaca.jpg", "wb") as archivo_copia:
    archivo_copia.write(contenido_binario)
