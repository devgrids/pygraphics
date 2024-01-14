import sys
sys.path.append('C:\\dev\\deep')

from pygraphics.config import *

def main():

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

