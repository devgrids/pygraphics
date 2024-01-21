from pygraphics.engine.components.component import Component
from pygraphics.graphics_resource import GraphicsResource

class SpriteRenderer(Component):
    def __init__(self):
        super().__init__()
        self.to = GraphicsResource.create_sprite_instance()
        self.texture = None
        
    def start(self):
        self.to.start()

    def update(self, transform, camera=None, program=None):
        self.to.update(transform, program)

    def render(self):
        self.to.render(self.texture)

    def load_texture(self, path):
        if path == "":
            self.texture = GraphicsResource.load_texture("pygraphics/resources/images/default.jpg")
        else:
            self.texture = GraphicsResource.load_texture(path)

    def set_size(self, size):
        self.to.size = size

    def set_offset(self, offset):
        self.to.offset = offset


