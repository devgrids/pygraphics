from pygraphics.engine.core.core_behaviour import CoreBehaviour
from pygraphics.engine.components.program import Program
from pygraphics.engine.components.user_interface import UserInterface

class Cube3D(CoreBehaviour):
    def __init__(self):
        super().__init__()
        self.game_object.name = self.game_object.name + " - Cube3D"
        self.game_object.add_component(Program, "cube2d")
        self.game_object.add_component(UserInterface)
        self.program = self.game_object.get_component(Program)
        self.user_interface = self.game_object.get_component(UserInterface)

    def start(self):
        pass

    def update(self, delta_time, camera=None):
        pass

    def render(self):
        self.user_interface.to.object(self.game_object)

            
        