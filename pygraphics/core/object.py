# Suponiendo que Mesh3D está definido en otro lugar
# from mesh3d import Mesh3D
from pygraphics.core.entity import Entity

class Object(Entity):
    def __init__(self):
        super().__init__()
        self.mesh = None
        self.type = 0

    def set_mesh(self, mesh):
        self.mesh = mesh

    def get_mesh(self):
        return self.mesh

    def load_data_from_file(self, file):
        pass
