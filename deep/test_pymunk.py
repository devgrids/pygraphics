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

    y_suelo = -20

    # Crear un espacio y establecer la gravedad
    space = pymunk.Space()
    space.gravity = (0, -981)
    space.damping = 0.9  # Amortiguamiento para reducir el efecto de rebote

    # Crear un suelo
    suelo_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    suelo_shape = pymunk.Segment(suelo_body, (-40, y_suelo), (40, y_suelo), 5)
    suelo_shape.elasticity = 0.0
    suelo_shape.friction = 0.0
    space.add(suelo_body, suelo_shape)

    # Crear un cuerpo y una forma de ladrillo
    ladrillo_body = pymunk.Body(100, 100)
    ladrillo_body.position = (0, 50)  # Posición inicial del ladrillo
    ladrillo_shape = pymunk.Poly.create_box(ladrillo_body, (10, 10))
    ladrillo_shape.elasticity = 0.0
    ladrillo_shape.friction = 0.0
    space.add(ladrillo_body, ladrillo_shape)

    # Opcional: Limitar la rotación del ladrillo
    ladrillo_body.angular_velocity = 0
    ladrillo_body.angular_velocity_limit = 0

     # Configurar el handler de colisión
    handler = space.add_collision_handler(0, 0)  # 0 es el tipo de colisión por defecto
    handler.begin = colision_ladrillo_suelo


    import time

    # # Simulación durante 10 segundos
    # for i in range(200):
    #     print(f"Tiempo: {i/20:.2f} s, Posición de la bola: {body.position}")
    #     space.step(1/20)  # Avanzar la simulación
    #     time.sleep(1/20)  # Esperar para sincronizar con el tiempo real



    def loop():

        delta_time = System.time_manager.get_delta_time()
        space.step(1/60)
        
        if System.input_manager.is_pressed_down('e'):
            System.exit()
        
        System.draw_pixel(ladrillo_body.position[0],ladrillo_body.position[1], glm.vec3(0.0, 1.0, 0.0))
        System.draw_pixel(1,0)

        

    System.loop(loop)
    return 0

if __name__ == "__main__":
    main()

