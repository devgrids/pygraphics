from pygraphics.engine.components.component import Component
from pygraphics.graphics_resource import GraphicsResource

class Program(Component):
    def __init__(self, name):
        super().__init__()
        self.to = GraphicsResource.get_program(name)
    
    def start(self):
        pass

    def update(self, transform, camera=None):
        pass

    def render(self):
        pass

