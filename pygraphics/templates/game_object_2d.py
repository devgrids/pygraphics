from pygraphics.engine.core.core_behaviour import CoreBehaviour
from pygraphics.engine.components.sprite_renderer import SpriteRenderer
from pygraphics.engine.components.user_interface import UserInterface
from pygraphics.engine.components.program import Program

class GameObject2D(CoreBehaviour):
    def __init__(self, path_sprite):
        super().__init__()
        self.game_object.name = self.game_object.name + " - GameObject2D"
        self.game_object.add_component(SpriteRenderer, path_sprite)
        self.game_object.add_component(Program, "sprite2d")
        self.game_object.add_component(UserInterface)
        self.sprite_renderer = self.game_object.get_component(SpriteRenderer)
        self.program = self.game_object.get_component(Program)
        self.user_interface = self.game_object.get_component(UserInterface)

    def start(self):
        self.sprite_renderer.start()

    def update(self, camera=None):
        self.sprite_renderer.update(self.transform, camera, self.program.to)

    def render(self):
        self.sprite_renderer.render()
        self.user_interface.to.object(self.game_object)

            
        