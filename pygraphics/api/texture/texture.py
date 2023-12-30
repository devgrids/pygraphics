from abc import ABC, abstractmethod
class Texture(ABC):
    @abstractmethod
    def load(self, path):
        pass