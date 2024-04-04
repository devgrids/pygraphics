from pygraphics.engine.components.component import Component
from pygraphics.graphics_resource import GraphicsResource

class VideoRenderer(Component):
    def __init__(self):
        super().__init__()
        self.to = GraphicsResource.create_sprite_instance()
        self.texture = GraphicsResource.load_texture("pygraphics/resources/images/default.jpg")
        
    def start(self):
        self.to.start()

    def update(self, transform, camera=None, program=None):
        self.to.update(transform, program)

    def render(self):
        self.to.render(self.texture)


