import sys
sys.path.append('C:\\dev\\deep')

import glm

from pygraphics.api.type.render_type import RenderType
from pygraphics.api.type.input_type import InputType
from pygraphics.api.type.gui_type import GuiType

from pygraphics.graphics_api import GraphicsApi
from pygraphics.system import System

import pymunk

def colision_ladrillo_suelo(arbiter, space, data):
    print("El ladrillo ha colisionado con el suelo")
    # Aquí puedes agregar código adicional para manejar la colisión
    return True  # Continuar procesando esta colisión

def main():
    GraphicsApi.set_type_graphic(RenderType.GL4)
    GraphicsApi.set_type_input(InputType.GLFW)
    GraphicsApi.set_type_gui(GuiType.IMGUI)
    
    System.init()

    y_suelo = -28.25

    # Crear un espacio y establecer la gravedad
    space = pymunk.Space()
    # space.gravity = (0, -981)
    space.damping = 0.9  # Amortiguamiento para reducir el efecto de rebote

    # Crear un suelo
    suelo_body = pymunk.Body(body_type=pymunk.Body.STATIC, moment=float('inf'))
    suelo_shape = pymunk.Segment(suelo_body, (0, y_suelo), (0, y_suelo), 4)
    suelo_shape.elasticity = 0.1
    suelo_shape.friction = 1.0
    space.add(suelo_body, suelo_shape)

    # Crear un suelo
    suelo_body2 = pymunk.Body(body_type=pymunk.Body.STATIC, moment=float('inf'))
    suelo_shape2 = pymunk.Segment(suelo_body2, (0, 28.25), (0, 28.25), 4)
    suelo_shape2.elasticity = 0.1
    suelo_shape2.friction = 1.0
    space.add(suelo_body2, suelo_shape2)


    # Crear un cuerpo y una forma de ladrillo
    # Calcular el momento de inercia para un ladrillo
    dimensiones_ladrillo = (10, 10)
    masa_ladrillo = 10
    momento_ladrillo = pymunk.moment_for_box(masa_ladrillo, dimensiones_ladrillo)
    ladrillo_body = pymunk.Body(masa_ladrillo, momento_ladrillo)
    ladrillo_body.position = (0, 15)  # Posición inicial del ladrillo
    ladrillo_shape = pymunk.Poly.create_box(ladrillo_body, dimensiones_ladrillo)
    ladrillo_shape.elasticity = 0.0
    ladrillo_shape.friction = 0.0
    space.add(ladrillo_body, ladrillo_shape)

    # Opcional: Limitar la rotación del ladrillo
    ladrillo_body.angular_velocity = 0 
    ladrillo_body.angular_velocity_limit = 0

     # Configurar el handler de colisión
    handler = space.add_collision_handler(0, 0)  # 0 es el tipo de colisión por defecto
    handler.begin = colision_ladrillo_suelo


    fuerza = 20
    def loop():

        delta_time = System.time_manager.get_delta_time()
        space.step(1/60)
        

        if System.input_manager.is_pressed('a'):
            ladrillo_body.apply_force_at_local_point((-fuerza, 0), (0, 0))
        
        if System.input_manager.is_pressed('d'):
            ladrillo_body.apply_force_at_local_point((fuerza, 0), (0, 0))

        if System.input_manager.is_pressed('w'):
            ladrillo_body.apply_force_at_local_point((0, fuerza), (0, 0))

        if System.input_manager.is_pressed('s'):
            ladrillo_body.apply_force_at_local_point((0, -fuerza), (0, 0))

        
        System.draw_pixel(ladrillo_body.position[0],ladrillo_body.position[1], glm.vec3(0.0, 1.0, 0.0))
        System.draw_pixel(1,0)

        

    System.loop(loop)
    return 0

if __name__ == "__main__":
    main()

