from pygraphics.core.core_behaviour import CoreBehaviour
from pygraphics.components.sprite_renderer import SpriteRenderer
from pygraphics.components.animator import Animator

class Character2D(CoreBehaviour):
    def __init__(self):
        self.__init__()
        self.gameObject.add_component(SpriteRenderer)
        self.gameObject.add_component(Animator)

    def start(self):
        pass

    def update(self):
        pass

    def render(self):
        pass