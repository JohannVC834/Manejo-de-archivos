
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()

with open("archivo.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())

with open("archivo.txt", "w") as archivo:
    archivo.write("Bienvenido al archivo de tecto..\n")


with open("archivo.txt", "a") as archivo:
    archivo.write("Adios\n")
