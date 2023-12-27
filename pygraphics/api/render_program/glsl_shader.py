import glm
import os
import spdlog
import unittest
from spdlog import ConsoleLogger, FileLogger, RotatingLogger, DailyLogger, LogLevel
from OpenGL.GL import *

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
    
    def link_programs(self):

        # Creación y compilación del shader de vértices
        vertex_shader = glCreateShader(GL_VERTEX_SHADER)
        glShaderSource(vertex_shader, self.shaders_code[RenderProgramType.VERTEX])
        glCompileShader(vertex_shader)

        # Creación y compilación del shader de fragmentos
        fragment_shader = glCreateShader(GL_FRAGMENT_SHADER)
        glShaderSource(fragment_shader, self.shaders_code[RenderProgramType.FRAGMENT])
        glCompileShader(fragment_shader)

        # Creación del programa y adjuntar shaders
        self.program_id = glCreateProgram()
        glAttachShader(self.program_id, vertex_shader)
        glAttachShader(self.program_id, fragment_shader)
        glLinkProgram(self.program_id)

        # Eliminar los shaders ya que están ahora en el programa
        glDeleteShader(vertex_shader)
        glDeleteShader(fragment_shader)
        

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

