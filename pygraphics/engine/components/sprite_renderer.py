from pygraphics.engine.components.component import Component
from pygraphics.graphics_resource import GraphicsResource

class SpriteRenderer(Component):
    def __init__(self, path=None):
        super().__init__()
        self.to = GraphicsResource.create_sprite_instance()
        self.texture = GraphicsResource.load_texture(path)
        
    def start(self):
        self.to.start()

    def update(self, transform, camera=None, program=None):
        self.to.update(transform, program)

    def render(self):
        self.to.render(self.texture)

    def load_texture(self, path):
        self.texture = GraphicsResource.load_texture(path)

