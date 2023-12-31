from pygraphics.engine.components.component import Component
from pygraphics.api.sprite.gl_sprite import GLSprite
from pygraphics.graphics_resource import GraphicsResource

class SpriteRenderer(Component):
    def __init__(self):
        super().__init__()
        self.to = GraphicsResource.create_sprite_instance()
        self.path = "/path/to/sprite"
        self.flip = False
    
    def start(self):
        self.to.start()

    def update(self, program, transform=None, camera=None):
        self.to.update(program = program, transform = transform)

    def render(self):
        self.to.render()

