from PIL import Image, ImageDraw, ImageFont

# Crear una nueva imagen con fondo blanco
image = Image.new('RGB', (200, 100), color = (255, 255, 255))

# Crear un objeto para dibujar en la imagen
draw = ImageDraw.Draw(image)

# Cargar una fuente (se necesita el archivo de la fuente)
font = ImageFont.truetype("deep/norwester.otf", 16)

# Dibujar texto
draw.text((10, 10), "Hola, mundo!", fill=(0, 0, 0), font=font)

# Guardar la imagen
image.save('deep/texto.png')
