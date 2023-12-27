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
        self.program_id = glCreateProgram()
        self.program_var_list = {}
        self.error_msgs = ""
        self.programs = {}
        self.shaders_code = {}
        self.logger = ConsoleLogger('Logger', False, True, True)

    def set_program(self, program_src, type):
        self.shaders_code[type] = self.read_file(program_src)
        self.programs[type] = GLuint()

    def link_programs(self):
        self.use()
        self.compile()
        for key, shader_id in self.programs.items():
            glAttachShader(self.program_id, shader_id)
        glLinkProgram(self.program_id)
        self.check_shader_error(self.program_id)
        self.setup_shader_var_list()

    def get_error_msg(self):
        return self.error_msgs

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

    def check_shader_error(self, shader_id):
        success = glGetShaderiv(shader_id, GL_COMPILE_STATUS)
        if not success:
            info_log = glGetShaderInfoLog(shader_id)
            self.error_msgs += "\n" + info_log
        return success

    def read_file(self, file_name):
        content = "src=?"
        if os.path.isfile(file_name):
            with open(file_name, 'r') as file:
                content = file.read()
        else:
            self.logger.error('File not found: %s' % file_name)
        return content

    def setup_shader_var_list(self):
        count = ctypes.c_int()

        glGetProgramiv(self.program_id, GL_ACTIVE_ATTRIBUTES, ctypes.byref(count))
        for i in range(count.value):
            name = ctypes.create_string_buffer(100)
            size = ctypes.c_int()
            type = ctypes.c_int()
            glGetActiveAttrib(self.program_id, i, 100, None, ctypes.byref(size), ctypes.byref(type), name)
            attrib_location = glGetAttribLocation(self.program_id, name)
            self.program_var_list[name.value.decode('utf-8')] = attrib_location

        glGetProgramiv(self.program_id, GL_ACTIVE_UNIFORMS, ctypes.byref(count))
        for i in range(count.value):
            name = ctypes.create_string_buffer(100)
            size = ctypes.c_int()
            type = ctypes.c_int()
            glGetActiveUniform(self.program_id, i, 100, None, ctypes.byref(size), ctypes.byref(type), name)
            uniform_location = glGetUniformLocation(self.program_id, name)
            self.program_var_list[name.value.decode('utf-8')] = uniform_location

    def compile(self):
        for key, shader_id in self.programs.items():
            shader_type = self.get_shader_to_enum(key)
            self.programs[key] = glCreateShader(shader_type)
            code = self.shaders_code[key].encode('utf-8')
            glShaderSource(self.programs[key], 1, ctypes.byref(ctypes.c_char_p(code)), None)
            glCompileShader(self.programs[key])
            self.check_shader_error(self.programs[key])

    def get_shader_to_enum(self, type):
        if type == RenderProgramType.VERTEX:
            return GL_VERTEX_SHADER
        elif type == RenderProgramType.FRAGMENT:
            return GL_FRAGMENT_SHADER
        else:
            return 0

