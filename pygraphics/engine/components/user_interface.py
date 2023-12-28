from pygraphics.engine.components.component import Component
from pygraphics.factory_engine import FactoryEngine

class UserInterface(Component):
    def __init__(self):
        super().__init__()
        self.gui = FactoryEngine.get_gui()

    def render(self):
        pass

