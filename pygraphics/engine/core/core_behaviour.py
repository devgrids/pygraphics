from pygraphics.engine.core.game_object import GameObject
from pygraphics.engine.components.transform import Transform
from abc import ABC, abstractmethod

class CoreBehaviour(ABC):
    def __init__(self):
        self.game_object = GameObject()
        self.game_object.add_component(Transform)
        self.transform = self.game_object.get_component(Transform)

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def update(self, camera=None):
        pass

    @abstractmethod
    def render(self):
        pass
