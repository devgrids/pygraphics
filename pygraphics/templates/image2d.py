from pygraphics.engine.core.core_behaviour import CoreBehaviour
from pygraphics.engine.components.user_interface import UserInterface
from pygraphics.engine.components.texture import Texture

class Image2D(CoreBehaviour):
    def __init__(self, path):
        super().__init__()
        self.game_object.name = self.game_object.name + " - Image"
        self.game_object.add_component(UserInterface)
        self.game_object.add_component(Texture)
        self.user_interface = self.game_object.get_component(UserInterface)
        self.texture = self.game_object.get_component(Texture)
        self.path = path

    def start(self):
        pass
       
    def update(self, delta_time):
        pass

    def render(self):
        pass

            
        