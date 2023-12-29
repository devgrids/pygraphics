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

        self.texture  = load_texture('deep/resources/sprites/goku/ui/transform/0.png')
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

    def update(self, position, size, rotate, flip):
        import glm
        projection = glm.ortho(-10.0, 10.0, -10.0, 10.0, -1.0, 1.0)
        self.program.set_matrix("u_projection", projection)

        # Trasladar el modelo
        model = glm.mat4(1.0)
        model = glm.translate(model, glm.vec3(position.x, position.y, 0.0))
        # Trasladar para rotar alrededor del centro del cuadrado
        # model = glm.translate(model, glm.vec3(0.5 * size.x, 0.5 * size.y, 0.0))

        # Rotar el modelo
        model = glm.rotate(model, glm.radians(rotate), glm.vec3(0.0, 0.0, 1.0))

        # Rotación adicional para voltear
        model = glm.rotate(model, glm.radians(180.0 * flip), glm.vec3(0.0, 1.0, 0.0))

        # Trasladar de vuelta después de la rotación
        # model = glm.translate(model, glm.vec3(-0.5 * size.x, -0.5 * size.y, 0.0))

        # Escalar el modelo
        model = glm.scale(model, glm.vec3(size.x, size.y, 1.0))
        self.program.set_matrix("u_model", model)

    def render(self):
        glBindTexture(GL_TEXTURE_2D, self.texture)
        glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, None)
