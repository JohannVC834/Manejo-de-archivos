import pandas as pd

# Leer una hoja de un archivo Excel
df = pd.read_excel("Var_continua.xlsx", sheet_name="Hoja1")

# Mostrar el contenido del DataFrame
print(df.head())

# Escribir un nuevo DataFrame a Excel
df.to_excel("archivo_modificado.xlsx", sheet_name="NuevaHoja", index=False)