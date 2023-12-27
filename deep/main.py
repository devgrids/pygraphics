import sys
sys.path.append('C:\\dev\\deep')

from pygraphics.api.type.render_type import RenderType
from pygraphics.api.type.input_type import InputType
from pygraphics.api.type.render_program import RenderProgramType

from pygraphics.factory_engine import FactoryEngine
from pygraphics.system import System

# from pygraphics.api.render_program.glsl_shader import GLSLShader
# from pygraphics.api.texture.gl_texture import load_texture

def program():
    if System.input_manager.is_pressed_down('e'):
            System.exit()
    if System.input_manager.is_pressed_down('f'):
        print("Hola, Yordy Leonidas MV!")

def main():
    FactoryEngine.set_type_graphic(RenderType.GL4)
    FactoryEngine.set_type_input(InputType.GLFW)

    System.init_system()

    # shader = GLSLShader()
    # shader.set_program("deep/resources/shaders/sprite.vert", RenderProgramType.VERTEX)
    # shader.set_program("deep/resources/shaders/sprite.frag", RenderProgramType.FRAGMENT)

    # shader.link_programs()

    # Uso de la función
    # Asegúrate de llamar a esta función después de haber creado un contexto de OpenGL
    # texture_id = load_texture('deep/resources/sprites/goku/base/icon.png')

    System.main_loop(program)
    return 0

if __name__ == "__main__":
    main()

