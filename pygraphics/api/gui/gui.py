from abc import ABC, abstractmethod
from typing import Tuple

class Gui(ABC):
    @abstractmethod
    def begin(self):
        pass

    @abstractmethod
    def end(self):
        pass

    @abstractmethod
    def init(self):
        pass

    @abstractmethod
    def step(self, time_step: float):
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def set_input_int(self, id: str, label: str, value: int, new_line: bool = False, description: str = "") -> bool:
        pass

    @abstractmethod
    def set_color_3f(self, id: str, label: str, value: Tuple[float, float, float], new_line: bool = False, description: str = "") -> bool:
        pass

    @abstractmethod
    def set_drag_float_3f(self, id: str, label: str, value: Tuple[float, float, float], new_line: bool = False, description: str = "") -> bool:
        pass

    @abstractmethod
    def button(self, id: str, label: str, new_line: bool = False, description: str = "") -> bool:
        pass

    @abstractmethod
    def debug(self):
        pass

    @abstractmethod
    def render(self, id: str, id_fb: int):
        pass

