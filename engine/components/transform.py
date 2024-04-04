from pygraphics.engine.components.component import Component
import glm

class Transform(Component):
    def __init__(self):
        super().__init__()
        self.position = glm.vec4(0.0, 0.0, 0.0, 0.0)
        self.rotation = glm.vec4(0.0, 0.0, 0.0, 0.0)
        self.scale = glm.vec4(1.0, 1.0, 1.0, 0.0)