from pygraphics.engine.core.core_behaviour import CoreBehaviour
from pygraphics.engine.components.program import Program
from pygraphics.engine.components.shape2d.box_shape_2d import BoxShape2D
from pygraphics.engine.components.user_interface import UserInterface

class Cube2D(CoreBehaviour):
    def __init__(self):
        super().__init__()
        self.game_object.name = self.game_object.name + " - Cube2D"
        self.game_object.add_component(Program, "cube2d")
        self.game_object.add_component(BoxShape2D)
        self.game_object.add_component(UserInterface)
        self.program = self.game_object.get_component(Program)
        self.box2d = self.game_object.get_component(BoxShape2D)
        self.user_interface = self.game_object.get_component(UserInterface)

    def start(self):
        self.box2d.start()

    def update(self, delta_time, camera=None):
        self.box2d.update(self.transform, camera, self.program.to)

    def render(self):
        self.box2d.render(self.program.to)
        self.user_interface.to.object(self.game_object)

            
        