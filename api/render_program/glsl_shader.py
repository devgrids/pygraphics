from OpenGL.GL import *
import glm
import os
from spdlog import ConsoleLogger

from pygraphics.api.type.render_program import RenderProgramType
from pygraphics.api.render_program.render_program import RenderProgram

class GLSLShader(RenderProgram):
    def __init__(self):
        self.program_id = 0
        self.program_var_list = {}
        self.error_msgs = ""
        self.programs = {}
        self.shaders_code = {}
        # self.logger = ConsoleLogger(f"glsl_shader.py", False, True, True)

    def set_program(self, program_src, type):
        self.shaders_code[type] = self.read_file(program_src)
        self.programs[type] = GLuint()

    def read_file(self, file_name):
        content = "src=?"
        if os.path.isfile(file_name):
            with open(file_name, 'r') as file:
                content = file.read()
        else:
            # self.logger.error('File not found: %s' % file_name)
            print("Error")
        return content
    
    def link_programs(self):
        self.compile()
        self.program_id = glCreateProgram()

        for shader_type, shader_id in self.programs.items():
            glAttachShader(self.program_id, shader_id)

        glLinkProgram(self.program_id)

        link_status = glGetProgramiv(self.program_id, GL_LINK_STATUS)
        if not link_status:
            info_log = glGetProgramInfoLog(self.program_id)
            print(f"Error en la vinculación del programa: {info_log}")

        for shader_type, shader_id in self.programs.items():
            glDeleteShader(shader_id)

        self.use() 

    
    def get_shader_to_enum(self, type):
        if type == RenderProgramType.VERTEX:
            type_shader = GL_VERTEX_SHADER
        elif type == RenderProgramType.FRAGMENT:
            type_shader = GL_FRAGMENT_SHADER
        else:
            type_shader = None 
        return type_shader
    
    def compile(self):
        for shader_type, shader_id in self.programs.items():
            type_enum = self.get_shader_to_enum(shader_type)
            self.programs[shader_type] = glCreateShader(type_enum)
            code = self.shaders_code[shader_type]
            glShaderSource(self.programs[shader_type], code)
            glCompileShader(self.programs[shader_type])

            compile_status = glGetShaderiv(self.programs[shader_type], GL_COMPILE_STATUS)
            if not compile_status:
                info_log = glGetShaderInfoLog(self.programs[shader_type])
                print(f"Error en la compilación del shader {shader_type}: {info_log}")

    def use(self):
        if self.program_id != 0:
            glUseProgram(self.program_id)
  
    def get_var_ui(self, name):
        return self.program_var_list[name]

    def set_int(self, location, value):
        glUniform1i(glGetUniformLocation(self.program_id, location), value)

    def set_float(self, location, value):
        glUniform1f(glGetUniformLocation(self.program_id, location), value)

    def set_ivec2(self, location, vec):
        glUniform2iv(glGetUniformLocation(self.program_id, location), 1, glm.value_ptr(vec))

    def set_vec2(self, location, vec):
        glUniform2fv(glGetUniformLocation(self.program_id, location), 1, glm.value_ptr(vec))

    def set_vec3(self, location, vec):
        glUniform3fv(glGetUniformLocation(self.program_id, location), 1, glm.value_ptr(vec))

    def set_vec4(self, location, vec):
        glUniform4fv(glGetUniformLocation(self.program_id, location), 1, glm.value_ptr(vec))

    def set_matrix(self, location, matrix):
        glUniformMatrix4fv(glGetUniformLocation(self.program_id, location), 1, GL_FALSE, glm.value_ptr(matrix))

