import sys
sys.path.append('C:\\dev\\deep')

import glm

from pygraphics.api.type.render_type import RenderType
from pygraphics.api.type.input_type import InputType
from pygraphics.api.type.gui_type import GuiType

from pygraphics.graphics_api import GraphicsApi
from pygraphics.system import System

def main():
    GraphicsApi.set_type_graphic(RenderType.GL4)
    GraphicsApi.set_type_input(InputType.GLFW)
    GraphicsApi.set_type_gui(GuiType.IMGUI)
    
    System.init()

    background = System.new_game_object_2d("deep/resources/sprites/world-hardest/Background.jpg")
    background.transform.scale = glm.vec3(40.0, 40.0, 1.0)

    player = System.new_game_object_2d("deep/resources/sprites/world-hardest/Player.png")
    player.transform.position = glm.vec3(-13.0, 9.0, 1.0)

    enemy = System.new_game_object_2d("deep/resources/sprites/world-hardest/Enemy.png")

    speed = 5.0

    def loop():

        delta_time = System.time_manager.get_delta_time()
        
        if System.input_manager.is_pressed('a'):
            player.transform.position.x-=speed*delta_time
        if System.input_manager.is_pressed('d'):
            player.transform.position.x+=speed*delta_time
        if System.input_manager.is_pressed('w'):
            player.transform.position.y+=speed*delta_time
        if System.input_manager.is_pressed('s'):
            player.transform.position.y-=speed*delta_time


    System.loop(loop)
    return 0

if __name__ == "__main__":
    main()

