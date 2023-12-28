from pygraphics.api.type.render_type import RenderType
from pygraphics.api.type.input_type import InputType
from pygraphics.api.type.gui_type import GuiType

from pygraphics.api.render.gl4_render import GL4Render
from pygraphics.api.input_manager.gl_glfw_input_manager import GlGlfwInputManager
from pygraphics.api.gui.gl_glfw_imgui import GlGlfwImgui 

class FactoryEngine:
    
    app_width = 1080
    app_height = 720

    selected_graphics_backend = RenderType.GL4
    selected_input_backend = InputType.GLFW
    selected_gui_backend = GuiType.NONE

    render = None
    input_manager = None
    gui = None

    @staticmethod
    def create_render_instance():
        if FactoryEngine.selected_graphics_backend == RenderType.GL4:
            return GL4Render(FactoryEngine.app_width, FactoryEngine.app_height)
        else:
            return None
    
    @staticmethod
    def create_input_manager_instance():
        if FactoryEngine.selected_input_backend == InputType.GLFW:
            if FactoryEngine.selected_graphics_backend == RenderType.GL1:
                return GlGlfwInputManager()
            elif FactoryEngine.selected_graphics_backend == RenderType.GL4:
                return GlGlfwInputManager()
            else:
                return None
        else:
            return None
        
    @staticmethod
    def create_gui_instance():
        if FactoryEngine.selected_input_backend == InputType.GLFW:
            if FactoryEngine.selected_graphics_backend == RenderType.GL1:
                if FactoryEngine.selected_gui_backend == GuiType.IMGUI:
                    return GlGlfwImgui()
                else:
                    return None
            elif FactoryEngine.selected_graphics_backend == RenderType.GL4:
                if FactoryEngine.selected_gui_backend == GuiType.IMGUI:
                    return GlGlfwImgui()
                else:
                    return None
            else:
                return None
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
    def get_new_gui():
        FactoryEngine.gui = FactoryEngine.create_gui_instance()
        return FactoryEngine.gui
        
    @staticmethod
    def set_type_graphic(type_graphic):
        FactoryEngine.selected_graphics_backend = type_graphic

    @staticmethod
    def set_type_input(type_input):
        FactoryEngine.selected_input_backend = type_input

    @staticmethod
    def set_type_gui(type_gui):
        FactoryEngine.selected_gui_backend = type_gui

    @staticmethod
    def get_type_graphic():
        return FactoryEngine.selected_graphics_backend
    
    @staticmethod
    def get_type_input():
        return FactoryEngine.selected_input_backend
    
    @staticmethod
    def get_type_gui():
        return FactoryEngine.selected_gui_backend

    @staticmethod
    def get_render():
        return FactoryEngine.render
    
    @staticmethod
    def get_input():
        return FactoryEngine.input_manager
    
    @staticmethod
    def get_gui():
        return FactoryEngine.gui
