import glm

class Vertex:
    def __init__(self, position=None):
        self.position = position if position is not None else glm.vec4(0.0, 0.0, 0.0, 0.0)
