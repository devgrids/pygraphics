from pygraphics.api.type.render_type import RenderType
from pygraphics.api.type.input_type import InputType

class GraphicsResource:

    programs = {}
    textures = {}

    @staticmethod
    def init():
        # Load render program
        GraphicsResource.load_program("sprite2d")  

    @staticmethod
    def load_program(path):
        if path in GraphicsResource.programs:
            return GraphicsResource.programs[path]      
        from pygraphics.api.type.render_program import RenderProgramType
        render_program = GraphicsResource.create_render_program_instance()
        path_elements = path.split('/')
        if len(path_elements) == 1:
            render_program.set_program("pygraphics/resources/shaders/"+path+".vert", RenderProgramType.VERTEX)
            render_program.set_program("pygraphics/resources/shaders/"+path+".frag", RenderProgramType.FRAGMENT)
        else:
            render_program.set_program(path+".vert", RenderProgramType.VERTEX)
            render_program.set_program(path+".frag", RenderProgramType.FRAGMENT)
            filename_with_extension = path_elements[-1]
            path = filename_with_extension.split('.')[0]
        render_program.link_programs()
        GraphicsResource.programs[path] = render_program
        return render_program
    
    @staticmethod
    def load_texture(path):
        if path in GraphicsResource.textures:
            return GraphicsResource.textures[path]
        texture = GraphicsResource.create_texture_instance()
        texture.load(path)
        GraphicsResource.textures[path] = texture
        return texture

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
        
    @staticmethod
    def create_texture_instance():     
        from pygraphics.api.texture.gl_texture import GLTexture
        from pygraphics.graphics_api import GraphicsApi

        type_graphic = GraphicsApi.get_type_graphic()
        
        if type_graphic == RenderType.GL1:
            return None
        elif type_graphic == RenderType.GL4:
            return GLTexture()
        else:
            return None

        
    
    
