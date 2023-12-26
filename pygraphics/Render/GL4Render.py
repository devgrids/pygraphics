from OpenGL import GL
import glfw
from pygraphics.Render.Render import Render

class GL4Render(Render):
    def __init__(self, width, height):
        super().__init__()
        self.set_width(width)
        self.set_height(height)
        self.window = None

    def init(self):
        assert glfw.init()
        self.window = glfw.create_window(self.width, self.height, "Deep", None, None)
        if not self.window:
            glfw.terminate()
            return
        glfw.make_context_current(self.window)

    def is_closed(self):
        return glfw.window_should_close(self.window)

    def get_window(self):
        return self.window
