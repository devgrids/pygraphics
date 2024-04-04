from pygraphics.api.type.render_type import RenderType
from pygraphics.api.type.input_type import InputType
from pygraphics.api.type.gui_type import GuiType
from pygraphics.api.type.texture_type import TextureType

class GraphicsApi:
    
    app_width = 1080
    app_height = 720

    selected_graphics_backend = RenderType.GL4
    selected_input_backend = InputType.GLFW
    selected_gui_backend = GuiType.IMGUI
    selected_texture_backend = TextureType.PILLOW

    render = None
    input_manager = None
    time_manager = None
    gui = None

    @staticmethod
    def create_render_instance():
        from pygraphics.api.render.gl4_render import GL4Render
        if GraphicsApi.selected_graphics_backend == RenderType.GL4:
            return GL4Render(GraphicsApi.app_width, GraphicsApi.app_height)
        else:
            return None
    
    @staticmethod
    def create_input_manager_instance():
        from pygraphics.api.input_manager.gl_glfw_input_manager import GlGlfwInputManager
        if GraphicsApi.selected_input_backend == InputType.GLFW:
            if GraphicsApi.selected_graphics_backend == RenderType.GL1:
                return GlGlfwInputManager()
            elif GraphicsApi.selected_graphics_backend == RenderType.GL4:
                return GlGlfwInputManager()
            else:
                return None
        else:
            return None
        
    @staticmethod
    def create_time_manager_instance():
        from pygraphics.api.time_manager.glfw_time_manager import GLFWTimeManager
        if GraphicsApi.selected_input_backend == InputType.GLFW:
            return GLFWTimeManager()
        else:
            return None
        
    @staticmethod
    def create_gui_instance():
        from pygraphics.api.gui.gl_glfw_imgui import GlGlfwImgui 
        if GraphicsApi.selected_input_backend == InputType.GLFW:
            if GraphicsApi.selected_graphics_backend == RenderType.GL1:
                if GraphicsApi.selected_gui_backend == GuiType.IMGUI:
                    return GlGlfwImgui()
                else:
                    return None
            elif GraphicsApi.selected_graphics_backend == RenderType.GL4:
                if GraphicsApi.selected_gui_backend == GuiType.IMGUI:
                    return GlGlfwImgui()
                else:
                    return None
            else:
                return None
        else:
            return None
        
    @staticmethod
    def get_new_render():
        GraphicsApi.render = GraphicsApi.create_render_instance()
        return GraphicsApi.render
    
    @staticmethod
    def get_new_input_manager():
        GraphicsApi.input_manager = GraphicsApi.create_input_manager_instance()
        return GraphicsApi.input_manager
    
    @staticmethod
    def get_new_time_manager():
        GraphicsApi.time_manager = GraphicsApi.create_time_manager_instance()
        return GraphicsApi.time_manager
    
    @staticmethod
    def get_new_gui():
        GraphicsApi.gui = GraphicsApi.create_gui_instance()
        return GraphicsApi.gui
        
    @staticmethod
    def set_type_graphic(type_graphic):
        GraphicsApi.selected_graphics_backend = type_graphic

    @staticmethod
    def set_type_input(type_input):
        GraphicsApi.selected_input_backend = type_input

    @staticmethod
    def set_type_gui(type_gui):
        GraphicsApi.selected_gui_backend = type_gui

    @staticmethod
    def set_type_texture(type_texture):
        GraphicsApi.selected_texture_backend = type_texture

    @staticmethod
    def get_type_graphic():
        return GraphicsApi.selected_graphics_backend
    
    @staticmethod
    def get_type_input():
        return GraphicsApi.selected_input_backend
    
    @staticmethod
    def get_type_gui():
        return GraphicsApi.selected_gui_backend
    
    @staticmethod
    def get_type_texture():
        return GraphicsApi.selected_texture_backend

    @staticmethod
    def get_render():
        return GraphicsApi.render
    
    @staticmethod
    def get_input_manager():
        return GraphicsApi.input_manager
    
    @staticmethod
    def get_time_manager():
        return GraphicsApi.time_manager
    
    @staticmethod
    def get_gui():
        return GraphicsApi.gui
