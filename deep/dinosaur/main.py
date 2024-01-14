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

        if self.position.x > _width:
            self.position.x = _width;
            self.velocity.x *= -1;
    
        elif self.position.x < 0:
            self.velocity.x *= -1
            self.position.x = 0

        if self.position.y > _height:
            self.velocity.y *= -1
            self.position.y = _height
    
        elif self.position.y < 1.5:
            self.velocity.y *= 0;
            self.position.y = 1.5;

def main(): 

    System.camera.set_projection_matrix(0, 30, 0, 30)

    cube = System.new_object_2d()
    cube.transform.position.x = 15
    cube.transform.scale.x = 30

    player = System.new_object_2d()
    player.box2d.color = glm.vec3(0.0, 1.0, 0.0)
    
    player.transform.position = glm.vec3(5.0, 25.0, 1.0)
    player.transform.scale = glm.vec3(2.0, 2.0, 1.0)
    


    system = ForceSystem(100, player.transform.position)

    _wind = glm.vec2(0.0, 150.0)
    _gravity = glm.vec2(0.0, -9.81)

    speed = 3.7

    def handle():
        delta_time = System.time_manager.get_delta_time()

        # if System.input_manager.is_pressed('a'):
        #     player.transform.position.x-=speed*delta_time
        # if System.input_manager.is_pressed('d'):
        #     player.transform.position.x+=speed*delta_time
        # if System.input_manager.is_pressed('w'):
        #     player.transform.position.y+=speed*delta_time
        # if System.input_manager.is_pressed('s'):
        #     player.transform.position.y-=speed*delta_time

        if System.input_manager.is_button_mouse_pressed_down(True):
            system.applyForce(_wind);

        system.applyForce(_gravity);
        
        system.update(30,30);
    
        player.transform.position.x = system.position.x
        player.transform.position.y = system.position.y

    System.loop(handle)

if __name__ == "__main__":
    main()

