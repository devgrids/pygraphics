from pygraphics.engine.components.component import Component
from pygraphics.graphics_resource import GraphicsResource

class SpriteRenderer(Component):
    def __init__(self):
        super().__init__()
        self.to = GraphicsResource.create_sprite_instance()
        
    def start(self):
        self.to.start()

    def update(self, transform, camera=None, program=None):
        self.to.update(transform, program)

    def render(self, texture):
        self.to.render(texture)

