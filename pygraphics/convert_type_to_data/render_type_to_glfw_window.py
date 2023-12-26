# from pygraphics.factory_engine import FactoryEngine
from pygraphics.type.render_type import RenderType

def RenderTypeToGLFWwindow(type):
    if type == RenderType.GL1:
        return FactoryEngine.get_render().get_window()
    elif type == RenderType.GL4:
        return FactoryEngine.get_render().get_window()
    else:
        return None