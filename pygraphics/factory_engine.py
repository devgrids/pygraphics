from pygraphics.type.render_type import RenderType
from pygraphics.type.input_type import InputType

from pygraphics.render.gl4_render import GL4Render
from pygraphics.input_manager.glfw_input_manager import GLFWInputManager

class FactoryEngine:
    
    app_width = 1080
    app_height = 720

    selected_graphics_backend = RenderType.GL4
    selected_input_backend = InputType.GLFW

    render = None
    input_manager = None

    @staticmethod
    def create_render_instance():
        if FactoryEngine.selected_graphics_backend == RenderType.GL4:
            return GL4Render(FactoryEngine.app_width, FactoryEngine.app_height)
        else:
            return None
    
    @staticmethod
    def create_input_manager_instance():
        if FactoryEngine.selected_input_backend == InputType.GLFW:
            return GLFWInputManager()
        else:
            return None
        
    @staticmethod
    def get_new_render():
        FactoryEngine.render = FactoryEngine.create_render_instance()
        return FactoryEngine.render
    
    @staticmethod
    def get_new_input_manager():
        FactoryEngine.input_manager = FactoryEngine.create_input_manager_instance()
        return FactoryEngine.input_manager
        
    @staticmethod
    def set_type_graphic(type_graphic):
        FactoryEngine.selected_graphics_backend = type_graphic

    @staticmethod
    def set_type_input(type_input):
        FactoryEngine.selected_input_backend = type_input

    @staticmethod
    def get_type_graphic():
        return FactoryEngine.selected_graphics_backend
    
    @staticmethod
    def get_type_input():
        return FactoryEngine.selected_input_backend

    @staticmethod
    def get_render():
        return FactoryEngine.render
    
    @staticmethod
    def get_input():
        return FactoryEngine.input_manager
