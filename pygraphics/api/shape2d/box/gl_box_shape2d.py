from pygraphics.api.shape2d.shape2d import Shape2D
from OpenGL.GL import *
import glm

class GLBoxShape2D(Shape2D):
    def __init__(self):
        self.VAO = 0

    def start(self):
        import numpy as np
        vertices = np.array([
            0.5,  0.5, 0.0,  # top right
            0.5, -0.5, 0.0,  # bottom right
           -0.5, -0.5, 0.0,  # bottom left
           -0.5,  0.5, 0.0   # top left 
        ], dtype=np.float32)

        indices = np.array([
            0, 1, 3,  # primer triángulo
            1, 2, 3   # segundo triángulo
        ], dtype=np.uint32)

        # Generación de VBO, VAO, y EBO
        self.VAO = glGenVertexArrays(1)
        VBO = glGenBuffers(1)
        EBO = glGenBuffers(1)

        # Configuración de VAO, VBO, y EBO
        glBindVertexArray(self.VAO)
        glBindBuffer(GL_ARRAY_BUFFER, VBO)
        glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices, GL_STATIC_DRAW)

        # Configuración de los atributos de los vértices
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 12, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)

        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glBindVertexArray(0)

    def update(self, transform, program=None):
        model = glm.mat4(1.0)
        model = glm.translate(model, glm.vec3(transform.position.x, transform.position.y, 0.0))
        model = glm.rotate(model, glm.radians(transform.rotation.z), glm.vec3(0.0, 0.0, 1.0))
        model = glm.scale(model, glm.vec3(transform.scale.x, transform.scale.y, 1.0))
        program.use()
        program.set_matrix("u_model", model)

    def render(self, color, program):
        program.use()
        program.set_vec3("u_color", color)
        glBindVertexArray(self.VAO)
        glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, None)

