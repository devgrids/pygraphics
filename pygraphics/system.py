from OpenGL.GL import *
from pygraphics.factory_engine import FactoryEngine

from pygraphics.api.gui.glfw_imgui import GLFWImGui 

class System:

    render = None
    input_manager = None

    end = False
    cursor_mouse_enabled = True

    @staticmethod
    def init(code_source=None):
        System.render = FactoryEngine.get_new_render()
        System.input_manager = FactoryEngine.get_new_input_manager()

        System.render.init()
        System.input_manager.link_render(System.render)
        System.input_manager.init()
        if code_source is not None:
            code_source()

    @staticmethod
    def exit():
        System.end = True

    @staticmethod
    def loop(code_source):

        gui = GLFWImGui()
        gui.init()
        gui.link_render(System.render)

        while not System.render.is_closed() and not System.end:
            glClearColor(0.1, 0.1, 0.1, 1.0);
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
            code_source()
            gui.render_frame()
            System.input_manager.buffers_events()
        gui.clear()
        System.render.clear()
