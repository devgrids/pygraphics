from pygraphics.factory_engine import FactoryEngine

class System:

    render = None
    input_manager = None

    @staticmethod
    def init_system():
        System.render = FactoryEngine.get_new_render()
        System.input_manager = FactoryEngine.get_new_input_manager()

        System.render.init()
        System.input_manager.init()
        System.input_manager.link_render(System.render)

    @staticmethod
    def exit():
        System.end = True

    @staticmethod
    def main_loop():
        while not System.render.is_closed():
            System.input_manager.buffers_events()
        System.render.clear()
