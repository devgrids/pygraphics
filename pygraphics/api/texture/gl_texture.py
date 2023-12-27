import OpenGL.GL as gl
from PIL import Image

def load_texture(path):
    # Cargar la imagen con Pillow
    img = Image.open(path)
    img = img.transpose(Image.FLIP_TOP_BOTTOM)  # Flip the image vertically
    img_data = img.convert("RGBA").tobytes()

    # Crear una textura en OpenGL
    texture = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture)

    # Configurar parámetros de la textura
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)

    # Cargar la imagen en la textura
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGBA, img.size[0], img.size[1], 0, gl.GL_RGBA, gl.GL_UNSIGNED_BYTE, img_data)

    # Generar mipmaps
    gl.glGenerateMipmap(gl.GL_TEXTURE_2D)

    return texture


