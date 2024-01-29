from pygraphics.engine.core.core_behaviour import CoreBehaviour
from pygraphics.engine.components.user_interface import UserInterface
from pygraphics.engine.components.texture import Texture
import cv2

class Video2D(CoreBehaviour):
    def __init__(self, path):
        super().__init__()
        self.game_object.name = self.game_object.name + " - Video2D"
        self.game_object.add_component(UserInterface)
        self.game_object.add_component(Texture)
        self.user_interface = self.game_object.get_component(UserInterface)
        self.texture = self.game_object.get_component(Texture)
        self.path = path
        self.capture = cv2.VideoCapture(path)
        self.frame = None

    def start(self):
        self.id = self.texture.to.get_id()
        self.width = self.texture.to.width
        self.height = self.texture.to.height
       
    def update(self, delta_time, camera=None):
        pass

    def render(self): 
        ret, self.frame = self.capture.read()
        if not ret:
            self.capture.set(cv2.CAP_PROP_POS_FRAMES, 0)
            return
        self.texture.to.load_data(self.frame)
        self.user_interface.to.set_image(self.game_object.name, self.id, self.texture.to.width/3, self.texture.to.height/3)
        
