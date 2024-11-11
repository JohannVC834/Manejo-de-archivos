import csv

# Leer CSV y convertirlo a una lista de diccionarios
with open("archivo.csv", "r") as archivo_csv:
    lector_csv = csv.DictReader(archivo_csv)
    datos = [fila for fila in lector_csv]

# Escribir CSV desde una lista de diccionarios
with open("archivo.csv", "w", newline="") as archivo_csv:
    campos = ["columna1", "columna2"]
    escritor_csv = csv.DictWriter(archivo_csv, fieldnames=campos)
    escritor_csv.writeheader()
    escritor_csv.writerows(datos)
