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
    def begin(self, id, description="None"):
        pass

    @abstractmethod
    def end(self):
        pass

    @abstractmethod
    def text(self, id, text="None"):
        pass

    @abstractmethod
    def set_drag_float_3f(self, id: str, label: str, value, description: str = "") -> bool:
        pass
    
    @abstractmethod
    def link_render(self, render):
        pass
    
    # @abstractmethod
    # def step(self, time_step: float):
    #     pass

    # @abstractmethod
    # def set_input_int(self, id: str, label: str, value: int, new_line: bool = False, description: str = "") -> bool:
    #     pass

    # @abstractmethod
    # def set_color_3f(self, id: str, label: str, value: Tuple[float, float, float], new_line: bool = False, description: str = "") -> bool:
    #     pass

    # @abstractmethod
    # def set_drag_float_3f(self, id: str, label: str, value: Tuple[float, float, float], new_line: bool = False, description: str = "") -> bool:
    #     pass

    # @abstractmethod
    # def button(self, id: str, label: str, new_line: bool = False, description: str = "") -> bool:
    #     pass

    # @abstractmethod
    # def debug(self):
    #     pass

    

