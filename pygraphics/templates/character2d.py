from pygraphics.engine.core.core_behaviour import CoreBehaviour
from pygraphics.engine.components.sprite_renderer import SpriteRenderer
# from pygraphics.engine.components.animator import Animator

class Character2D(CoreBehaviour):
    def __init__(self):
        super().__init__()
        self.gameObject.add_component(SpriteRenderer)
        # self.gameObject.add_component(Animator)
        self.sprite_renderer = self.gameObject.get_component(SpriteRenderer)

    def start(self):
        pass

    def update(self):
        pass

    def render(self):
        self.sprite_renderer.render()