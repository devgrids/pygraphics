from pygraphics.engine.core.core_behaviour import CoreBehaviour
from pygraphics.engine.components.user_interface import UserInterface
from pygraphics.engine.components.texture import Texture

class Image2D(CoreBehaviour):
    def __init__(self, path):
        super().__init__()
        self.game_object.name = self.game_object.name + " - Image 2D"
        self.game_object.add_component(UserInterface)
        self.game_object.add_component(Texture)
        self.user_interface = self.game_object.get_component(UserInterface)
        self.texture = self.game_object.get_component(Texture)
        self.path = path

    def start(self):
        self.texture.to.load(self.path)
        self.id = self.texture.to.get_id()
        self.width = self.texture.to.width
        self.height = self.texture.to.height
       
    def update(self, delta_time, camera=None):
        pass

    def render(self):
        self.user_interface.to.set_image(self.game_object.name, self.id, self.width/4,self.height/4)
        pass

            
        