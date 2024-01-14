from abc import ABC, abstractmethod
import glm
class Sprite(ABC):
    def __init__(self):
        self.offset = glm.vec2(0.0, 0.0)
        self.size = glm.ivec2(1, 1)
