from abc import ABC, abstractmethod

class Gui(ABC):

    @abstractmethod
    def init(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def widget(self, id, code=None):
        pass

    @abstractmethod
    def text(self, id, text="None"):
        pass

    @abstractmethod
    def button(self, id: str, label: str) -> bool:
        pass

    @abstractmethod
    def set_drag_float_3f(self, id: str, label: str, value) -> bool:
        pass

    @abstractmethod
    def set_file(self, id: str, label: str) -> str:
        pass

    @abstractmethod
    def set_image(self, id, texture, width, height):
        pass
    
    @abstractmethod
    def link_render(self, render):
        pass

    @abstractmethod   
    def info(self):
        pass

    @abstractmethod   
    def objects(self):
        pass

    @abstractmethod   
    def tweak(self):
        pass

    # ----------- Neural Network --------------------
    @abstractmethod   
    def convolutional_neural_network(self):
        pass

    

