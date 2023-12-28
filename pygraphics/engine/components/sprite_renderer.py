from pygraphics.engine.components.component import Component
from pygraphics.api.sprite.gl_sprite import GLSprite
from pygraphics.factory_component import FactoryComponent

class SpriteRenderer(Component):
    def __init__(self):
        super().__init__()
        self.sprite = FactoryComponent.create_sprite_instance()
        self.sprite.init()
        self.path = "/path/to/sprite"
        self.flip = False

    def render(self):
        self.sprite.render()

