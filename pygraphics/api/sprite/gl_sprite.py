from OpenGL.GL import *
from pygraphics.api.sprite.sprite import Sprite
from pygraphics.api.type.render_program import RenderProgramType
from pygraphics.api.render_program.glsl_shader import GLSLShader
from pygraphics.api.texture.gl_texture import load_texture
import numpy as np

class GLSprite(Sprite):
    def __init__(self):
        #super().__init__()
        self.program = GLSLShader()
        self.program.set_program("pygraphics/resources/shaders/model.vert", RenderProgramType.VERTEX)
        self.program.set_program("pygraphics/resources/shaders/model.frag", RenderProgramType.FRAGMENT)
        self.program.link_programs()
        self.program.use()

        self.texture  = load_texture('deep/resources/sprites/goku/base/icon.png')
        glBindTexture(GL_TEXTURE_2D, self.texture)

    def init(self):
        vertices = [
            -0.5, -0.5, 0.0, 0.0,  # Inferior izquierdo
             0.5, -0.5, 1.0, 0.0,  # Inferior derecho
             0.5,  0.5, 1.0, 1.0,  # Superior derecho
            -0.5,  0.5, 0.0, 1.0   # Superior izquierdo
        ]
        indices = [
            0, 1, 2,  # Primer triángulo
            2, 3, 0   # Segundo triángulo
        ]

        vertices = np.array(vertices, dtype=np.float32)
        indices = np.array(indices, dtype=np.uint32)

        vao = glGenVertexArrays(1)
        glBindVertexArray(vao)

        vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, vbo)
        glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

        ebo = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ebo)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices, GL_STATIC_DRAW)

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 16, ctypes.c_void_p(0))
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 16, ctypes.c_void_p(8))

    def render(self):
        glBindTexture(GL_TEXTURE_2D, self.texture)
        glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, None)
