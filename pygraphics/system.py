from OpenGL.GL import *
from pygraphics.graphics_api import GraphicsApi
from pygraphics.api.camera.orthographic_camera import OrthographicCamera
from pygraphics.api.camera.camera import Camera
from pygraphics.graphics_resource import GraphicsResource
import glm

class System:

    render = None
    input_manager = None
    time_manager = None
    gui = None
    camera = None

    end = False
    cursor_mouse_enabled = True

    objects = []

    pixel = None
    pixels = []

    @staticmethod
    def init():
        System.render = GraphicsApi.get_new_render()
        System.input_manager = GraphicsApi.get_new_input_manager()
        System.time_manager = GraphicsApi.get_new_time_manager()
        System.gui = GraphicsApi.get_new_gui()
        
        System.camera = OrthographicCamera()
        System.camera.set_projection_matrix(glm.ortho(-10.0, 10.0, -10.0, 10.0, -1.0, 1.0))
        
        System.render.init()
        System.gui.init()

        System.input_manager.link_render(System.render)
        System.gui.link_render(System.render)

        System.input_manager.link_gui(System.gui)
        System.input_manager.init()
        System.time_manager.init()

        GraphicsResource.init()
        program = GraphicsResource.load_program("sprite2d")
        program.use()
        program.set_matrix("u_projection", System.camera.get_projection_matrix())

        System.init_pixel()
       
    @staticmethod
    def init_pixel():
        program = GraphicsResource.load_program("cube2d")
        program.use()
        program.set_matrix("u_projection", System.camera.get_projection_matrix())
        from pygraphics.templates.cube2d import Cube2D
        System.pixel = Cube2D()
        System.pixel.start()

    @staticmethod
    def draw_pixel(x, y, color=glm.vec3(1.0, 1.0, 1.0)):
        System.pixel.transform.position.x = x
        System.pixel.transform.position.y = y
        System.pixel.update(System.camera)
        System.pixel.render(color)
    
    @staticmethod
    def new_character2d(path_sprite):
        from pygraphics.templates.character2d import Character2D
        character2d = Character2D(path_sprite)
        System.objects.append(character2d)
        return character2d
    
    @staticmethod
    def loop(code_source):     
        for object in System.objects:
                object.start()
        while not System.render.is_closed() and not System.end:
            System.time_manager.update()
            System.render.update()
            System.gui.update()
            code_source()
            for object in System.objects:
                object.update(System.camera)
                object.render()
            System.gui.render()
            System.input_manager.buffers_events()
        System.gui.clear()
        System.render.clear()

    @staticmethod
    def exit():
        System.end = True
    
