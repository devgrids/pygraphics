from pygraphics.engine.components.component import Component
from pygraphics.api.sprite.gl_sprite import GLSprite
from pygraphics.graphics_resource import GraphicsResource

class SpriteRenderer(Component):
    def __init__(self):
        super().__init__()
        self.sprite = GraphicsResource.create_sprite_instance()
        self.path = "/path/to/sprite"
        self.flip = False
    
    def start(self):
        self.sprite.init()

    def update(self):
        # self.sprite.update()
        pass

    def render(self):
        self.sprite.render()

