from OpenGL.GL import *
import glm
import os
import spdlog
import unittest
from spdlog import ConsoleLogger, FileLogger, RotatingLogger, DailyLogger, LogLevel

from pygraphics.api.type.render_program import RenderProgramType
from pygraphics.api.render_program.render_program import RenderProgram

class GLSLShader(RenderProgram):
    def __init__(self):
        self.program_id = 0
        self.program_var_list = {}
        self.error_msgs = ""
        self.programs = {}
        self.shaders_code = {}
        self.logger = ConsoleLogger(f"glsl_shader.py", False, True, True)

    def set_program(self, program_src, type):
        self.shaders_code[type] = self.read_file(program_src)
        self.programs[type] = GLuint()

    def read_file(self, file_name):
        content = "src=?"
        if os.path.isfile(file_name):
            with open(file_name, 'r') as file:
                content = file.read()
        else:
            self.logger.error('File not found: %s' % file_name)
        return content
    
    def get_shader_to_enum(self, type):
        if type == RenderProgramType.VERTEX:
            type_shader = GL_VERTEX_SHADER
        elif type == RenderProgramType.FRAGMENT:
            type_shader = GL_FRAGMENT_SHADER
        else:
            type_shader = None  # o algún valor por defecto
        return type_shader
    
    def compile(self):
        for shader_type, shader_id in self.programs.items():
            type_enum = self.get_shader_to_enum(shader_type)
            self.programs[shader_type] = glCreateShader(type_enum)
            code = self.shaders_code[shader_type]
            glShaderSource(self.programs[shader_type], code)
            glCompileShader(self.programs[shader_type])
            # check_shader_error(self.programs[shader_type])

   
    def link_programs(self):
        self.use()
        self.compile()

        self.program_id = glCreateProgram()
             
        for shader_id in self.programs.values():
            glAttachShader(self.program_id, shader_id)

        glDeleteShader(self.programs[RenderProgramType.VERTEX])
        glDeleteShader(self.programs[RenderProgramType.FRAGMENT])  

        glLinkProgram(self.program_id)


    def use(self):
        glUseProgram(self.program_id)
  
    def get_var_ui(self, name):
        return self.program_var_list[name]

    def set_int(self, location, value):
        glUniform1i(glGetUniformLocation(self.program_id, location), value)

    def set_float(self, location, value):
        glUniform1f(glGetUniformLocation(self.program_id, location), value)

    def set_vec3(self, location, vec):
        glUniform3fv(glGetUniformLocation(self.program_id, location), 1, glm.value_ptr(vec))

    def set_vec4(self, location, vec):
        glUniform4fv(glGetUniformLocation(self.program_id, location), 1, glm.value_ptr(vec))

    def set_matrix(self, location, matrix):
        glUniformMatrix4fv(glGetUniformLocation(self.program_id, location), 1, GL_FALSE, glm.value_ptr(matrix))

