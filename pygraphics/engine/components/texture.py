from pygraphics.engine.components.component import Component
from pygraphics.graphics_resource import GraphicsResource

class Texture(Component):
    def __init__(self, path=None):
        super().__init__()
        self.to = GraphicsResource.load_texture(path)
    
    def start(self):
        pass

    def update(self):
        pass

    def render(self):
        pass

    def load(self, path):
        self.to = GraphicsResource.load_texture(path)