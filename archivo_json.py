import json

# Leer archivo JSON
with open("archivo.json", "r") as archivo_json:
    datos = json.load(archivo_json)

# Modificar datos y guardar en JSON
datos["nueva_clave"] = "nuevo valor"
with open("archivo.json", "w") as archivo_json:
    json.dump(datos, archivo_json, indent=4)
