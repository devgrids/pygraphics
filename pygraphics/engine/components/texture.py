from pygraphics.engine.components.component import Component
from pygraphics.graphics_resource import GraphicsResource

class Texture(Component):
    def __init__(self):
        super().__init__()
        self.to = GraphicsResource.create_sprite_instance()
        self.path = "/path/to/sprite"
        self.flip = False
    
    def start(self):
        self.to.start()

    def update(self):
        pass

    def render(self):
        pass

