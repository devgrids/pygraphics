from pygraphics.engine.core.core_behaviour import CoreBehaviour
from pygraphics.engine.components.sprite_renderer import SpriteRenderer
from pygraphics.engine.components.user_interface import UserInterface
# from pygraphics.engine.components.animator import Animator

class Character2D(CoreBehaviour):
    def __init__(self):
        super().__init__()
        self.gameObject.add_component(SpriteRenderer)
        self.gameObject.add_component(UserInterface)
        self.sprite_renderer = self.gameObject.get_component(SpriteRenderer)
        self.user_interface = self.gameObject.get_component(UserInterface)

    def start(self):
        pass

    def update(self):
        pass

    def render(self):
        self.sprite_renderer.render()
        self.user_interface.gui.text(self.gameObject.name, "Python + IA")
        self.user_interface.gui.set_drag_float_3f(self.gameObject.name, "position", self.transform.position)