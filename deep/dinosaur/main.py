import sys
sys.path.append('C:\\dev\\deep')
from pygraphics.config import *

class ForceSystem:
    def __init__(self, mass, position):
        self.position = glm.vec2(position.x, position.y)
        self.velocity = glm.vec2(0, 0)
        self.acceleration = glm.vec2(0, 0)
        self.mass = mass

    def update(self, _width, _height):
        self.velocity = self.velocity + self.acceleration
        self.position = self.position + self.velocity
        self.acceleration = self.acceleration * 0.0

        self.checkEdges(_width, _height);

    def applyForce(self, force):
        self.acceleration = self.acceleration + (force / self.mass);

    def checkEdges(self, _width, _height):

        # if self.position.x > _width:
        #     self.position.x = _width;
        #     self.velocity.x *= -1;
    
        # elif self.position.x < 0:
        #     self.velocity.x *= -1
        #     self.position.x = 0

        if self.position.y > _height:
            self.velocity.y *= -1
            self.position.y = _height
    
        elif self.position.y < 0:
            self.velocity.y *= -1;
            self.position.y = 0;

def main(): 

    cube = System.new_object_2d()
    player = System.new_game_object_2d(
        "deep/dinosaur/assets/sprites/male/kuro/base/move.png",
        glm.ivec2(6,1))
    
    player.transform.position = glm.vec3(15.0, 25.0, 1.0)
    player.transform.scale = glm.vec3(2.0, 2.0, 1.0)
    System.camera.set_projection_matrix(0, 30, 0, 30)


    # player.sprite_renderer.load_texture("deep/dinosaur/assets/sprites/male/kuro/base/dead.png")

    system = ForceSystem(10, player.transform.position)

    _wind = glm.vec2(0.0, 0.5)
    _gravity = glm.vec2(0.0, -0.1)

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

        if System.input_manager.is_pressed_down('f'):
            system.applyForce(_gravity);

        #     system.applyForce(_wind);
        
        system.update(50,50);
    
        player.transform.position.x = system.position.x
        player.transform.position.y = system.position.y



    System.loop(handle)

if __name__ == "__main__":
    main()

