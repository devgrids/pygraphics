from abc import ABC, abstractmethod
class Texture(ABC):
    def __init__(self):
        self.path = ""
        self.id = 0
        self.data = None
        self.height, self.width = 0, 0

    @abstractmethod
    def load(self, path):
        self.path = path

    def load_data(self, data):
        self.data = data

    def get_id(self):
        return self.id
     
    def get_data(self):
        return self.data
    
    def to_base64(self):
        import base64
        with open(self.path, 'rb') as file:
            bits = file.read()
        return base64.b64encode(bits).decode('utf-8')