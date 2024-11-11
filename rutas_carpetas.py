import os
from pathlib import Path

# Crear una carpeta si no existe
Path("nueva_carpeta").mkdir(parents=True, exist_ok=True)

# Verificar si un archivo existe
ruta = Path("nueva_carpeta/archivo.txt")
if ruta.exists():
    print("El archivo existe.")
else:
    print("El archivo no existe.")

# Combinar y normalizar rutas
ruta_completa = Path("nueva_carpeta") / "archivo.txt"
print(ruta_completa.resolve())
