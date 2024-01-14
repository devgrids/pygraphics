import sys
sys.path.append('C:\\dev\\deep')
from pygraphics.config import *

def main(): 

    player = System.new_game_object_2d(
        "deep/dinosaur/assets/sprites/male/kuro/base/move.png",
        glm.ivec2(6,1))
    
    player.transform.position = glm.vec3(1.0, 2.0, 1.0)
    player.transform.scale = glm.vec3(2.0, 2.0, 1.0)
    System.camera.set_projection_matrix(0, 30, 0, 30)

    # player.sprite_renderer.load_texture("deep/dinosaur/assets/sprites/male/kuro/base/dead.png")

    speed = 3.7

    def handle():
        delta_time = System.time_manager.get_delta_time()

        if System.input_manager.is_pressed('a'):
            player.transform.position.x-=speed*delta_time
        if System.input_manager.is_pressed('d'):
            player.transform.position.x+=speed*delta_time
        if System.input_manager.is_pressed('w'):
            player.transform.position.y+=speed*delta_time
        if System.input_manager.is_pressed('s'):
            player.transform.position.y-=speed*delta_time


    System.loop(handle)

if __name__ == "__main__":
    main()

