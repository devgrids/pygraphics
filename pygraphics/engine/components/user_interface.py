from pygraphics.engine.components.component import Component
from pygraphics.graphics_api import GraphicsApi

class UserInterface(Component):
    def __init__(self):
        super().__init__()
        self.to = GraphicsApi.get_gui()

    def render(self):
        pass

