import sys
sys.path.append('C:\\dev\\deep')

import glm

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

    character = System.new_character2d("deep/resources/sprites/broly/base/icon.png")
    speed = 1.75

    def loop():
        delta_time = System.time_manager.get_delta_time()
        
        if System.input_manager.is_pressed_down('e'):
            System.exit()
        if System.input_manager.is_pressed('a'):
            character.transform.position.x-=speed*delta_time
        if System.input_manager.is_pressed('d'):
            character.transform.position.x+=speed*delta_time
        if System.input_manager.is_pressed('w'):
            character.transform.position.y+=speed*delta_time
        if System.input_manager.is_pressed('s'):
            character.transform.position.y-=speed*delta_time

        System.draw_pixel(3,0, glm.vec3(0.0, 1.0, 0.0))
        System.draw_pixel(1,0)

        # System.gui.demo()
        System.gui.info()
        System.gui.tweak()

    System.loop(loop)
    return 0

if __name__ == "__main__":
    main()

