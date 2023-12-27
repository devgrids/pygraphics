from OpenGL.GL import *
from pygraphics.factory_engine import FactoryEngine
from pygraphics.api.render_program.glsl_shader import GLSLShader
from pygraphics.api.type.render_program import RenderProgramType
from pygraphics.api.texture.gl_texture import load_texture
import numpy as np

def compile_shader_program():
    vertex_src = """
    #version 330 core
    layout (location = 0) in vec2 aPos;
    layout (location = 1) in vec2 aTexCoord;

    out vec2 TexCoord;

    void main()
    {
        gl_Position = vec4(aPos.x, aPos.y, 0.0, 1.0);
        TexCoord = aTexCoord;
    }
    """

    fragment_src = """
    #version 330 core
    out vec4 FragColor;

    in vec2 TexCoord;

    uniform sampler2D texture1;

    void main()
    {
        FragColor = texture(texture1, TexCoord);
    }
    """

    vertex_shader = glCreateShader(GL_VERTEX_SHADER)
    glShaderSource(vertex_shader, vertex_src)
    glCompileShader(vertex_shader)

    fragment_shader = glCreateShader(GL_FRAGMENT_SHADER)
    glShaderSource(fragment_shader, fragment_src)
    glCompileShader(fragment_shader)

    shader_program = glCreateProgram()
    glAttachShader(shader_program, vertex_shader)
    glAttachShader(shader_program, fragment_shader)
    glLinkProgram(shader_program)

    glDeleteShader(vertex_shader)
    glDeleteShader(fragment_shader)

    return shader_program


class System:

    render = None
    input_manager = None

    end = False
    cursor_mouse_enabled = True

    @staticmethod
    def init_system():
        System.render = FactoryEngine.get_new_render()
        System.input_manager = FactoryEngine.get_new_input_manager()

        System.render.init()
        System.input_manager.link_render(System.render)
        System.input_manager.init()

    @staticmethod
    def exit():
        System.end = True

    @staticmethod
    def main_loop(program):

        # Configuración de la geometría (cuadrado) y textura
        vertices = [
            -0.5, -0.5, 0.0, 0.0,  # Inferior izquierdo
             0.5, -0.5, 1.0, 0.0,  # Inferior derecho
             0.5,  0.5, 1.0, 1.0,  # Superior derecho
            -0.5,  0.5, 0.0, 1.0   # Superior izquierdo
        ]
        indices = [
            0, 1, 2,  # Primer triángulo
            2, 3, 0   # Segundo triángulo
        ]

        vertices = np.array(vertices, dtype=np.float32)
        indices = np.array(indices, dtype=np.uint32)

        vao = glGenVertexArrays(1)
        glBindVertexArray(vao)

        vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, vbo)
        glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

        ebo = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ebo)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices, GL_STATIC_DRAW)

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 16, ctypes.c_void_p(0))
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 16, ctypes.c_void_p(8))

        shader_program = compile_shader_program()
        # shader = GLSLShader()
        # shader.set_program("deep/resources/shaders/sprite.vert", RenderProgramType.VERTEX)
        # shader.set_program("deep/resources/shaders/sprite.frag", RenderProgramType.FRAGMENT)
        # shader.link_programs()

        glUseProgram(shader_program)

        texture  = load_texture('deep/resources/sprites/goku/base/icon.png')
        glBindTexture(GL_TEXTURE_2D, texture)

        while not System.render.is_closed() and not System.end:
            glClearColor(0.0, 0.0, 0.0, 1.0);
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
            program()
            glBindTexture(GL_TEXTURE_2D, texture)
            glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, None)
            System.input_manager.buffers_events()
        System.render.clear()
