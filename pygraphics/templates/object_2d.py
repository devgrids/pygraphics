from pygraphics.engine.core.core_behaviour import CoreBehaviour
from pygraphics.engine.components.sprite_renderer import SpriteRenderer
from pygraphics.engine.components.animator import Animator
from pygraphics.engine.components.user_interface import UserInterface
from pygraphics.engine.components.program import Program

class Object2D(CoreBehaviour):
    def __init__(self):
        super().__init__()
        self.game_object.name = self.game_object.name + " - 2D"
        self.game_object.add_component(SpriteRenderer)
        self.game_object.add_component(Animator)
        self.game_object.add_component(Program, "sprite2d")
        self.game_object.add_component(UserInterface)
        self.sprite_renderer = self.game_object.get_component(SpriteRenderer)
        self.animator = self.game_object.get_component(Animator)
        self.program = self.game_object.get_component(Program)
        self.user_interface = self.game_object.get_component(UserInterface)

    def start(self):
        self.sprite_renderer.start()
        self.animator.set_sprite(self.sprite_renderer)
       
    def update(self, delta_time, camera=None):
        self.sprite_renderer.update(self.transform, camera, self.program.to)
        self.animator.update(delta_time)

    def render(self):
        self.sprite_renderer.render()
        self.user_interface.to.object(self.game_object)

            
        