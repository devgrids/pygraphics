from pygraphics.api.texture.texture import Texture

class GLTexture(Texture):
    def __init__(self):
        super().__init__()

    def load(self, path):
        import OpenGL.GL as gl
        self.id = gl.glGenTextures(1)
        from PIL import Image
        img = Image.open(path)
        img = img.transpose(Image.FLIP_TOP_BOTTOM)
        img_data = img.convert("RGBA").tobytes()
        self.path = path
        self.width = img.size[0]
        self.height = img.size[1]
        self.load_data(img_data)

    def load_data(self, data):
        super().load_data(data)
        import OpenGL.GL as gl

        image = self.data

        gl.glBindTexture(gl.GL_TEXTURE_2D, self.id)

        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)

        self.load_texture(self.width, self.height, image)
        gl.glGenerateMipmap(gl.GL_TEXTURE_2D)

    def load_texture(self, width, height, data):
        import OpenGL.GL as gl
        gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGBA, width, height, 0, gl.GL_RGBA, gl.GL_UNSIGNED_BYTE, data)

        