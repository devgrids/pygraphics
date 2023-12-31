from pygraphics.api.type.render_type import RenderType
from pygraphics.api.type.input_type import InputType

class GraphicsResource:

    resources = {}

    @staticmethod
    def init():
        # Load render program
        from pygraphics.api.type.render_program import RenderProgramType
        render_program = GraphicsResource.create_render_program_instance()
        render_program.set_program("pygraphics/resources/shaders/model.vert", RenderProgramType.VERTEX)
        render_program.set_program("pygraphics/resources/shaders/model.frag", RenderProgramType.FRAGMENT)
        render_program.link_programs()
        GraphicsResource.resources['program_sprite2d'] = render_program

    @staticmethod
    def get_resource(resource):
        return GraphicsResource.resources[resource]
   
    @staticmethod
    def create_sprite_instance():
        from pygraphics.api.sprite.gl_sprite import GLSprite
        from pygraphics.graphics_api import GraphicsApi

        type_input = GraphicsApi.get_type_input()
        type_graphic = GraphicsApi.get_type_graphic()
        
        if type_input == InputType.GLFW:
            if type_graphic == RenderType.GL1:
                return None
            elif type_graphic == RenderType.GL4:
                return GLSprite()
            else:
                return None
        else:
            return None
        
    @staticmethod
    def create_render_program_instance():
        
        from pygraphics.api.render_program.glsl_shader import GLSLShader
        from pygraphics.graphics_api import GraphicsApi

        type_graphic = GraphicsApi.get_type_graphic()
        
        if type_graphic == RenderType.GL1:
            return None
        elif type_graphic == RenderType.GL4:
            return GLSLShader()
        else:
            return None

        
    
    
