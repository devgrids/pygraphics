import sys
sys.path.append('C:\\dev\\deep')

from pygraphics.type.render_type import RenderType
from pygraphics.type.input_type import InputType

from pygraphics.factory_engine import FactoryEngine
from pygraphics.system import System

def program():
    if System.input_manager.is_pressed_down('e'):
            System.exit()
    if System.input_manager.is_pressed_down('f'):
        print("Hola, Yordy Leonidas MV!")

def main():
    FactoryEngine.set_type_graphic(RenderType.GL4)
    FactoryEngine.set_type_input(InputType.GLFW)

    System.init_system()
    System.main_loop(program)
    return 0

if __name__ == "__main__":
    main()

