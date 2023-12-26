from pygraphics.Type.RenderType import RenderType
from pygraphics.Render.GL4Render import GL4Render

class FactoryEngine:
    app_width = 1080
    app_height = 720

    selected_graphics_backend = RenderType.GL4
    render = None

    @staticmethod
    def create_render_instance():
        if FactoryEngine.selected_graphics_backend == RenderType.GL4:
            return GL4Render(FactoryEngine.app_width, FactoryEngine.app_height)
        else:
            return None
        
    @staticmethod
    def get_new_render():
        FactoryEngine.render = FactoryEngine.create_render_instance()
        return FactoryEngine.render
        
    @staticmethod
    def set_type_graphic(type_graphic):
        FactoryEngine.selected_graphics_backend = type_graphic

    @staticmethod
    def get_render():
        return FactoryEngine.render
