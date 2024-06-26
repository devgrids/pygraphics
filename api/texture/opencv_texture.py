from pygraphics.api.texture.texture import Texture

class CV2Texture(Texture):
    def __init__(self):
        super().__init__()

    def load(self, path):
        import OpenGL.GL as gl
        self.id = gl.glGenTextures(1)
        gl.glPixelStorei(gl.GL_UNPACK_ALIGNMENT, 1)
        import cv2
        img = cv2.imread(path)
        self.height, self.width, _ = img.shape
        self.load_data(img)

    def load_data(self, data):
        super().load_data(data)
        import OpenGL.GL as gl
        import cv2

        image = self.data
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        self.height, self.width, _ = image.shape

        gl.glBindTexture(gl.GL_TEXTURE_2D, self.id)
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)

        self.load_texture(self.width, self.height, image)
        # gl.glGenerateMipmap(gl.GL_TEXTURE_2D)

    def load_texture(self, width, height, data):
        import OpenGL.GL as gl
        gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, width, height, 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, data)

        