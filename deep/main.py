import sys
sys.path.append('C:\\dev\\deep')

from pygraphics.api.type.render_type import RenderType
from pygraphics.api.type.input_type import InputType

from pygraphics.factory_engine import FactoryEngine
from pygraphics.system import System

from pygraphics.templates.character2d import Character2D

def test():
     print("Testing")

def main():
    FactoryEngine.set_type_graphic(RenderType.GL4)
    FactoryEngine.set_type_input(InputType.GLFW)

    # System.init()
    System.init(test)

    character = Character2D()
    character.start()

    def loop():
        character.render()
        if System.input_manager.is_pressed_down('e'):
            System.exit()
        if System.input_manager.is_pressed_down('f'):
            print("Hola, Yordy Leonidas MV!")

    System.loop(loop)
    return 0

if __name__ == "__main__":
    main()

