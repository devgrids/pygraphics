from pygraphics.engine.core.core import Core
from pygraphics.engine.core.game_object import GameObject
from pygraphics.engine.components.transform import Transform
from abc import abstractmethod

class CoreBehaviour(Core):
    def __init__(self):
        self.game_object = GameObject()
        self.game_object.add_component(Transform)
        self.transform = self.game_object.get_component(Transform)

    @abstractmethod
    def start(self, *args, **kwargs):
        pass

    @abstractmethod
    def update(self, *args, **kwargs):
        pass

    @abstractmethod
    def render(self, *args, **kwargs):
        pass
