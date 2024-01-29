from pygraphics.engine.core.core_behaviour import CoreBehaviour
from pygraphics.engine.components.user_interface import UserInterface
from pygraphics.engine.components.texture import Texture
from pygraphics.engine.components.convolutional_neural_network import ConvolutionalNeuralNetwork
from pygraphics.helpers.path import path_split

class Image2DCNN(CoreBehaviour):
    def __init__(self):
        super().__init__()
        self.game_object.name = self.game_object.name + " - Image2D CNN"
        self.game_object.add_component(UserInterface)
        self.game_object.add_component(Texture)
        self.game_object.add_component(ConvolutionalNeuralNetwork)
        self.user_interface = self.game_object.get_component(UserInterface)
        self.texture = self.game_object.get_component(Texture)
        self.convolutional_neural_network = self.game_object.get_component(ConvolutionalNeuralNetwork)
        self.path = None
        self.path_view = None
        self.load_image = False

    def start(self):
        # self.texture.to.load(self.path)
        # self.id = self.texture.to.get_id()
        # self.width = self.texture.to.width
        # self.height = self.texture.to.height
        pass
       
    def update(self, delta_time, camera=None):
        pass

    def render(self):
        self.path = self.user_interface.to.set_file(self.game_object.name,"Load Image")
        if self.path != self.path_view:
            self.load_image = False
        if self.path is not None and not self.load_image:
            print(self.path)
            path_split(self.path)
            self.texture.to.load(self.path)
            self.id = self.texture.to.get_id()
            self.width = self.texture.to.width
            self.height = self.texture.to.height
            self.load_image = True
            self.path_view = self.path

        if self.load_image:
            self.user_interface.to.set_image(self.game_object.name, self.id, 600, 400)

        if self.user_interface.to.button(self.game_object.name, "Predict"):
            self.convolutional_neural_network.predict(self.path_view)
        

            
        