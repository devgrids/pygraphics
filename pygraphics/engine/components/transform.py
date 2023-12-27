from pygraphics.engine.components.component import Component

class Transform(Component):
    def __init__(self):
        super().__init__()
        self.position = (0.0, 0.0) 
        self.scale = (1.0, 1.0)    
        self.rotation = 0.0        