from pygraphics.engine.components.component import Component
from pygraphics.api.texture.opencv_texture import CV2Texture

class Texture(Component):
    def __init__(self):
        super().__init__()
        self.to = CV2Texture()
    
    def start(self):
        pass

    def update(self):
        pass

    def render(self):
        pass

    def load(self, path):
        pass