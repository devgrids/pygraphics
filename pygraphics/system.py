from OpenGL.GL import *
from pygraphics.factory_engine import FactoryEngine

class System:

    render = None
    input_manager = None
    gui = None

    end = False
    cursor_mouse_enabled = True

    @staticmethod
    def init():
        System.render = FactoryEngine.get_new_render()
        System.input_manager = FactoryEngine.get_new_input_manager()
        System.gui = FactoryEngine.get_new_gui()
        
        System.render.init()
        System.gui.init()

        System.input_manager.link_render(System.render)
        System.gui.link_render(System.render)

        System.input_manager.link_gui(System.gui)
        System.input_manager.init()

    @staticmethod
    def exit():
        System.end = True

    @staticmethod
    def loop(code_source):       
        while not System.render.is_closed() and not System.end:
            System.render.update()
            System.gui.update()
            code_source()
            System.gui.render()
            System.input_manager.buffers_events()

        System.gui.clear()
        System.render.clear()
