from pygraphics.engine.core.core_behaviour import CoreBehaviour
from pygraphics.engine.components.sprite_renderer import SpriteRenderer
from pygraphics.engine.components.user_interface import UserInterface
from pygraphics.engine.components.animator import Animator

class Character2D(CoreBehaviour):
    def __init__(self):
        super().__init__()
        self.game_object.name = self.game_object.name + " - Character2D"
        self.game_object.add_component(SpriteRenderer)
        self.game_object.add_component(UserInterface)
        self.game_object.add_component(Animator)
        self.sprite_renderer = self.game_object.get_component(SpriteRenderer)
        self.user_interface = self.game_object.get_component(UserInterface)

    def start(self):
        pass

    def update(self):
        pass

    def render(self):
        self.sprite_renderer.render()

            
        