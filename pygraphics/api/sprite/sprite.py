from pygraphics.engine.core.core import Core
from abc import abstractmethod
class Sprite(Core):
    def __init__(self):
        pass

    @abstractmethod
    def start(self, *args, **kwargs):
        pass

    @abstractmethod
    def update(self, *args, **kwargs):
        pass

    @abstractmethod
    def render(self, *args, **kwargs):
        pass