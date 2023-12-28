from OpenGL.GL import *
from pygraphics.factory_engine import FactoryEngine

from pygraphics.api.gui.gl_glfw_imgui import GlGlfwImgui 

class System:

    render = None
    input_manager = None
    gui = None

    end = False
    cursor_mouse_enabled = True

    @staticmethod
    def init(code_source=None):
        System.render = FactoryEngine.get_new_render()
        System.input_manager = FactoryEngine.get_new_input_manager()
        System.gui = FactoryEngine.get_new_gui()
        
        System.render.init()
        System.gui.init()

        System.input_manager.link_render(System.render)
        System.gui.link_render(System.render)

        System.input_manager.link_gui(System.gui)
        System.input_manager.init()
    
        if code_source is not None:
            code_source()

    @staticmethod
    def exit():
        System.end = True

    @staticmethod
    def loop(code_source):       
        while not System.render.is_closed() and not System.end:
            System.gui.update()
            glClearColor(0.1, 0.1, 0.1, 1.0);
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
            System.gui.render_frame()
            code_source()
            System.gui.render()
            System.input_manager.buffers_events()
        System.gui.clear()
        System.render.clear()
