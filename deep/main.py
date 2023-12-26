import sys
sys.path.append('C:\\dev\\deep')

from pygraphics.type.render_type import RenderType
from pygraphics.type.input_type import InputType

from pygraphics.core.mesh3d import Mesh3D
from pygraphics.core.object3d import Object3D

from pygraphics.factory_engine import FactoryEngine
from pygraphics.system import System
from pygraphics.data.vertex import Vertex

import glm

class TriangleRoot(Object3D):
    def __init__(self):
        self.mesh = Mesh3D()

        vertex1 = vertex2 = vertex3 = Vertex()
        vertex1.position = glm.vec4(-0.5, -0.5, 0.0, 1.0)
        vertex2.position = glm.vec4(0.0, 0.5, 0.0, 1.0)
        vertex3.position = glm.vec4(0.5, -0.5, 0.0, 1.0)

        self.mesh.add_vertex(vertex1)
        self.mesh.add_vertex(vertex2)
        self.mesh.add_vertex(vertex3)
        
        self.mesh.add_triangle(0, 1, 2)

    def compute_model_matrix(self):
        super().compute_model_matrix()
        matrix = glm.mat4(1.0)
        matrix = glm.translate(matrix, self.position)
        matrix = glm.rotate(matrix, self.rotation.x, glm.vec3(1.0, 0.0, 0.0))
        matrix = glm.rotate(matrix, self.rotation.y, glm.vec3(0.0, 1.0, 0.0))
        matrix = glm.rotate(matrix, self.rotation.z, glm.vec3(0.0, 0.0, 1.0))
        matrix = glm.scale(matrix, self.scale)
        self.model = matrix

    def step(self, delta_time):
        self.compute_model_matrix();
        self.rotation.y += delta_time * 2.0;

def main():
    FactoryEngine.set_type_graphic(RenderType.GL4)
    FactoryEngine.set_type_input(InputType.GLFW)

    System.init_system()
    System.main_loop()
    return 0

if __name__ == "__main__":
    main()

