import sys
sys.path.append('C:\\dev\\deep')
from pygraphics.config import *

# Constantes
GRAVITY = glm.vec2(0.0, -9.81)
WIND = glm.vec2(0.0, 120.0)
SPEED = 3.7
CAMERA_BOUNDS = (0, 30, 0, 30)
INITIAL_POSITION = glm.vec3(5.0, 5.0, 1.0)
PLAYER_SCALE = glm.vec3(1.0, 2.0, 1.0)
CACTUS_MIN_X = 1
CACTUS_RESET_X_RANGE = (30, 32)
CACTUS_Y_RANGE = (1, 4)
CACTUS_SCALE_RANGE = (1, 2)
TIMER_RESET = 3
CACTUS_MOVE_SPEED = 15


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

    def checkCollision(self, me, other):
        size_x = other.scale.x/2.0 + me.scale.x/2.0
        size_y = other.scale.y/2.0 + me.scale.y/2.0

        if (me.position.x+size_x >other.position.x and 
            other.position.x> me.position.x-size_x and 
            me.position.y+size_y >other.position.y and
            other.position.y> me.position.y-size_y):
            return True
        return False



timer2 = 0.0
flag = False
description = "Network Neural"


def reset_cactus(cactus):
    s_x = random.randint(*CACTUS_SCALE_RANGE)
    s_y = random.randint(*CACTUS_SCALE_RANGE)
    cactus.transform.position.x = random.randint(*CACTUS_RESET_X_RANGE)
    cactus.transform.position.y = random.randint(*CACTUS_Y_RANGE)
    cactus.transform.scale.x = s_x
    cactus.transform.scale.y = s_y

def setup_objects():
    player = System.new_object_2d()
    player.transform.position = INITIAL_POSITION
    player.transform.scale = PLAYER_SCALE
    player.box2d.color = glm.vec3(0.0, 1.0, 0.0)

    cactus = System.new_object_2d()
    cactus.transform.position = glm.vec3(50.0, 2.0, 1.0)
    cactus.transform.scale = glm.vec3(1.0, 3.0, 1.0)

    cactus2 = System.new_object_2d()
    cactus2.transform.position = glm.vec3(35.0, 1.0, 1.0)
    cactus2.transform.scale = glm.vec3(2.0, 2.0, 1.0)

    cube = System.new_object_2d()
    cube.transform.position.x = 15
    cube.transform.scale.x = 30

    return player, cactus, cactus2, cube

def main(): 

    System.camera.set_projection_matrix(*CAMERA_BOUNDS)

    player, cactus, cactus2, cube = setup_objects()

    

    system = ForceSystem(60, player.transform.position)

    _wind = glm.vec2(0.0, 120.0)
    _gravity = glm.vec2(0.0, -9.81)

    speed = 3.7


    def handle():
        global flag
        global timer2
        global description
        
        delta_time = System.time_manager.get_delta_time()
        # if System.input_manager.is_pressed('a'):
        #     player.transform.position.x-=speed*delta_time
        # if System.input_manager.is_pressed('d'):
        #     player.transform.position.x+=speed*delta_time
        # if System.input_manager.is_pressed('w'):
        #     player.transform.position.y+=speed*delta_time
        # if System.input_manager.is_pressed('s'):
        #     player.transform.position.y-=speed*delta_time

        timer2+=delta_time 

        if System.input_manager.is_button_mouse_pressed_down(True) and not flag:
            system.applyForce(_wind);
            flag=True

        system.applyForce(_gravity);
        
        system.update(30,30);
    
        player.transform.position.x = system.position.x
        player.transform.position.y = system.position.y

        sp = 15

        if timer2 > 3:
            cactus.transform.position.x-=delta_time*sp
            cactus2.transform.position.x-=delta_time*sp

        if cactus.transform.position.x < 1:
           
            if abs(cactus.transform.position.x-cactus2.transform.position.x) < 5:
                cactus2.transform.position.x += 25
            reset_cactus(cactus)

        if cactus2.transform.position.x < 1:
           
            if abs(cactus.transform.position.x-cactus2.transform.position.x) < 5:
                cactus.transform.position.x+= 25
            reset_cactus(cactus2)

        if player.transform.position.y < 2.5:
            flag = False

        if system.checkCollision(player.transform,cactus.transform):
            description="¡Perdiste!"

        if system.checkCollision(player.transform,cactus2.transform):
            description="¡Perdiste!"
            
        System.gui.text("Test", description)

    System.loop(handle)

if __name__ == "__main__":
    main()

