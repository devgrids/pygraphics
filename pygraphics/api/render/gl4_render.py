import glfw
from OpenGL.GL import *
from pygraphics.api.render.render import Render

class GL4Render(Render):
    def __init__(self, width, height):
        super().__init__()
        self.set_width(width)
        self.set_height(height)
        self.window = None

    def init(self):
        super().init()
        assert glfw.init()
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
        glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
        self.window = glfw.create_window(self.width, self.height, "pygraphics", None, None)
        if not self.window:
            glfw.terminate()
            return
        glfw.make_context_current(self.window)

    def clear(self):
        glfw.terminate()

    def is_closed(self):
        return glfw.window_should_close(self.window)

    def get_window(self):
        return self.window
