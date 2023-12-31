from abc import ABC, abstractmethod
class Texture(ABC):
    def __init__(self):
        self.id = 0

    @abstractmethod
    def load(self, path):
        pass

    def get_id(self):
        return self.id