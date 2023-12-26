from pygraphics.material.material import Material
from pygraphics.type.render_program import RenderProgramType
from pygraphics.render_program.glsl_shader import GLSLShader

class GLSLMaterial(Material):
    def __init__(self):
        super().__init__()
        self.program = GLSLShader()

    def load_programs(self):
        self.program.set_program("resources/shaders/model.vert", RenderProgramType.VERTEX)
        self.program.set_program("resources/shaders/model.frag", RenderProgramType.FRAGMENT)

    def prepare(self):
        self.program.link_programs()
