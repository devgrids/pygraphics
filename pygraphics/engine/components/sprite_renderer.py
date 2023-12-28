from pygraphics.engine.components.component import Component
from pygraphics.api.sprite.gl_sprite import GLSprite
# from pygraphics.factory_engine import FactoryEngine

class SpriteRenderer(Component):
    def __init__(self):
        super().__init__()
        self.sprite = GLSprite()
        self.sprite.init()

    def render(self):
        self.sprite.render()

