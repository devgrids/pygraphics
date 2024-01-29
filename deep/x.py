import os

# Ruta con caracteres especiales
ruta_archivo = r'C:\Users\yordy\OneDrive\Imágenes\325904863_756539332471029_8397011208428151741_n.jpg'

# Obtener la unidad (por ejemplo, 'C:')
unidad, resto_ruta = os.path.splitdrive(ruta_archivo)

# Normalizar la ruta para manejar caracteres especiales
resto_ruta = os.path.normpath(resto_ruta)

# Obtener las carpetas (lista)
carpetas = []
while True:
    resto_ruta, carpeta = os.path.split(resto_ruta)
    if not carpeta:
        break
    carpetas.insert(0, carpeta)

# Obtener el nombre de archivo y extensión
nombre_archivo, extension = os.path.splitext(os.path.basename(ruta_archivo))

# Imprimir los resultados
print("Unidad:", unidad)
print("Carpetas:", carpetas)
print("Nombre de archivo:", nombre_archivo)
print("Extensión:", extension)
