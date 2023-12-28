
from pygraphics.api.type.render_type import RenderType
from pygraphics.api.type.input_type import InputType

class FactoryComponent:
   
    @staticmethod
    def create_sprite_instance():
        from pygraphics.api.sprite.gl_sprite import GLSprite
        from pygraphics.factory_engine import FactoryEngine
        
        if FactoryEngine.get_type_input() == InputType.GLFW:
            if FactoryEngine.get_type_graphic() == RenderType.GL1:
                return GLSprite()
            elif FactoryEngine.get_type_graphic() == RenderType.GL4:
                return GLSprite()
            else:
                return None
        else:
            return None
    
