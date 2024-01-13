from OpenGL.GL import *
from pygraphics.api.sprite.sprite import Sprite
from pygraphics.api.texture.gl_texture import GLTexture
import numpy as np
import glm

class GLSprite(Sprite):
    def __init__(self):
        self.vao = 0
        self.vbo = 0
        self.ebo = 0

    def start(self):
        vertices = [
            -0.5, -0.5, 0.0, 0.0,
             0.5, -0.5, 1.0, 0.0,
             0.5,  0.5, 1.0, 1.0,
            -0.5,  0.5, 0.0, 1.0 
        ]
        indices = [
            0, 1, 2,
            2, 3, 0 
        ]

        vertices = np.array(vertices, dtype=np.float32)
        indices = np.array(indices, dtype=np.uint32)

        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)

        self.vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

        self.ebo = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.ebo)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices, GL_STATIC_DRAW)

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 16, ctypes.c_void_p(0))
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 16, ctypes.c_void_p(8))

    def update(self, transform, program=None):
        model = glm.mat4(1.0)
        model = glm.translate(model, glm.vec3(transform.position.x, transform.position.y, 0.0))
        model = glm.rotate(model, glm.radians(transform.rotation.z), glm.vec3(0.0, 0.0, 1.0))
        model = glm.scale(model, glm.vec3(transform.scale.x, transform.scale.y, 1.0))

        program.use()
        program.set_matrix("u_model", model)

    def render(self, texture):    
        glBindVertexArray(self.vao) 
        glBindTexture(GL_TEXTURE_2D, texture.get_id())
        glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, None)
