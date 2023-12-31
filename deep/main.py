import sys
sys.path.append('C:\\dev\\deep')

from pygraphics.api.type.render_type import RenderType
from pygraphics.api.type.input_type import InputType
from pygraphics.api.type.gui_type import GuiType

from pygraphics.graphics_api import GraphicsApi
from pygraphics.system import System

from pygraphics.engine.components.animator import Animator

def main():
    GraphicsApi.set_type_graphic(RenderType.GL4)
    GraphicsApi.set_type_input(InputType.GLFW)
    GraphicsApi.set_type_gui(GuiType.IMGUI)
    
    System.init()

    character = System.new_character2d()
    character1 = System.new_character2d()
    
    character1.game_object.remove_component(Animator)
    
    def loop():
        if System.input_manager.is_pressed_down('e'):
            System.exit()
        if System.input_manager.is_pressed_down('f'):
            character.transform.position.x+=1
            print("Hola, Yordy Leonidas MV!")
        # System.gui.demo()
        System.gui.info()
        System.gui.tweak()
        System.gui.object(character.game_object)
        System.gui.object(character1.game_object)

    System.loop(loop)
    return 0

if __name__ == "__main__":
    main()

