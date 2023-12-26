from OpenGL.GL import *
from pygraphics.factory_engine import FactoryEngine

class System:

    render = None
    input_manager = None

    end = False
    cursor_mouse_enabled = True

    @staticmethod
    def init_system():
        System.render = FactoryEngine.get_new_render()
        System.input_manager = FactoryEngine.get_new_input_manager()

        System.render.init()
        System.input_manager.link_render(System.render)
        System.input_manager.init()

    @staticmethod
    def exit():
        System.end = True

    @staticmethod
    def main_loop():
        while not System.render.is_closed() and not System.end:
            glClearColor(0.0, 1.0, 0.0, 1.0);
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
            if System.input_manager.is_pressed_down('e'):
                System.exit()
            System.input_manager.buffers_events()
        System.render.clear()
