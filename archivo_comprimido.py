import zipfile

# Crear un archivo ZIP y agregar archivos
with zipfile.ZipFile("archivo.zip", "w") as archivo_zip:
    archivo_zip.write("archivo.txt")
    archivo_zip.write("vaca.jpg")

# Extraer todos los archivos de un archivo ZIP
with zipfile.ZipFile("archivo.zip", "r") as archivo_zip:
    archivo_zip.extractall("carpeta_destino")
