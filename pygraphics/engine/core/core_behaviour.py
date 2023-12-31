from pygraphics.engine.core.game_object import GameObject
from pygraphics.engine.components.transform import Transform

class CoreBehaviour:
    def __init__(self):
        self.game_object = GameObject()
        self.game_object.add_component(Transform)
        self.transform = self.game_object.get_component(Transform)

    def start(self):
        pass

    def update(self):
        pass

    def render(self):
        pass
