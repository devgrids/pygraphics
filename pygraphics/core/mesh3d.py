import glm
from pygraphics.material.material import Material
from pygraphics.data.vertex import Vertex

class Mesh3D:
    mesh_id = 0

    def __init__(self):
        self.list_vertex = []
        self.v_triangle_idx_list = []
        Mesh3D.mesh_id += 1
        self.color_rgb = glm.vec3(0.0, 0.0, 0.0)  # Asumiendo que glm está disponible
        self.material = None

        # Implementación específica para inicializar material
        # Depende de cómo esté estructurado Material y FactoryEngine en Python
        # ...

    def get_mesh_id(self):
        return Mesh3D.mesh_id

    def add_vertex(self, v):
        self.list_vertex.append(v)

    def get_vertex_list(self):
        return self.list_vertex

    def set_material(self, material):
        self.material = material

    def set_list_triangle(self, list):
        self.v_triangle_idx_list = list

    def get_material(self):
        return self.material

    def get_list_triangle_idx(self):
        return self.v_triangle_idx_list

    def add_triangle(self, v_id1, v_id2, v_id3):
        self.v_triangle_idx_list.extend([v_id1, v_id2, v_id3])
