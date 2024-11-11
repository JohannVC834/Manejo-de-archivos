import os
import xml.etree.ElementTree as ET

ruta = "archivo.xml"

if os.path.getsize(ruta) > 0:
    tree = ET.parse(ruta)
    root = tree.getroot()
    print("Contenido XML:", root.tag)
else:
    print("El archivo XML está vacío o no es válido.")

