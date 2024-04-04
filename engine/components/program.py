from pygraphics.engine.components.component import Component
from pygraphics.graphics_resource import GraphicsResource

class Program(Component):
    def __init__(self, path=None):
        super().__init__()
        self.to = GraphicsResource.load_program(path)
    
    def start(self):
        pass

    def update(self, transform, camera=None):
        pass

    def render(self):
        pass

    def load(self, path):
        self.to = GraphicsResource.load_program(path)

