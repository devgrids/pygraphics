from pygraphics.FactoryEngine import FactoryEngine
import glfw

class System:
    render = None

    @staticmethod
    def init_system():
        System.render = FactoryEngine.get_new_render()
        System.render.init()

    @staticmethod
    def exit():
        System.end = True

    @staticmethod
    def main_loop():
        while not System.render.is_closed():
            glfw.poll_events()
            glfw.swap_buffers(System.render.get_window())
        glfw.terminate()
