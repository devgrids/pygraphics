from abc import ABC, abstractmethod
class Texture(ABC):
    def __init__(self):
        self.id = 0
        self.data = None
        self.height, self.width = 0, 0

    @abstractmethod
    def load(self, path):
        pass

    def load_data(self, data):
        self.data = data

    def get_id(self):
        return self.id
     
    def get_data(self):
        return self.data