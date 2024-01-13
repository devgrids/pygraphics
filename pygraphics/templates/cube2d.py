from pygraphics.engine.core.core_behaviour import CoreBehaviour
from pygraphics.engine.components.program import Program
from pygraphics.engine.components.shape2d.box_shape_2d import BoxShape2D
import glm

class Cube2D(CoreBehaviour):
    def __init__(self):
        super().__init__()
        self.game_object.name = self.game_object.name + " - Cube2D"
        self.game_object.add_component(Program, "cube2d")
        self.game_object.add_component(BoxShape2D)
        self.program = self.game_object.get_component(Program)
        self.box2d = self.game_object.get_component(BoxShape2D)

    def start(self):
        self.box2d.start()

    def update(self, camera=None):
        self.box2d.update(self.transform, camera, self.program.to)

    def render(self, color=glm.vec3(1.0, 1.0, 1.0)):
        self.box2d.render(color, self.program.to)

            
        