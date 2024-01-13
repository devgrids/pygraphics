from pygraphics.engine.components.component import Component
from pygraphics.api.shape2d.box.gl_box_shape2d import GLBoxShape2D

class BoxShape2D(Component):
    def __init__(self):
        super().__init__()
        self.to = GLBoxShape2D()

    def start(self):
        self.to.start()

    def update(self, transform, camera=None, program=None):
        self.to.update(transform, program)

    def render(self, color, program=None):
        self.to.render(color, program)