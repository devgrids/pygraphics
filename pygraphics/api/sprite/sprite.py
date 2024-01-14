from abc import ABC, abstractmethod
import glm
class Sprite(ABC):
    def __init__(self, size = glm.ivec2(1, 1), offset = glm.vec2(0.0, 0.0)):
        self.size = size
        self.offset = offset
