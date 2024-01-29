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
        System.camera.set_projection_matrix(0, GraphicsApi.app_width, 0, GraphicsApi.app_height)

        System.render.init()
        System.gui.init()

        System.input_manager.link_render(System.render)
        System.gui.link_render(System.render)

        System.input_manager.link_gui(System.gui)
        System.input_manager.init()
        System.time_manager.init()

        GraphicsResource.init()
        System.init_pixel()
        
    @staticmethod
    def load_programs():
        System.load_projection_programs()

    @staticmethod
    def load_projection_programs():
        projection = System.camera.get_projection_matrix()

        program = GraphicsResource.load_program("sprite2d")
        program.use()
        program.set_matrix("u_projection", projection)   

        program = GraphicsResource.load_program("cube2d")
        program.use()
        program.set_matrix("u_projection", projection)   
   
    @staticmethod
    def init_pixel():       
        from pygraphics.templates.cube2d import Cube2D
        System.pixel = Cube2D()
        System.pixel.start()

    @staticmethod
    def draw_pixel(x, y, color=glm.vec3(1.0, 1.0, 1.0)):
        System.pixel.transform.position.x = x
        System.pixel.transform.position.y = y
        System.pixel.update(System.camera)
        System.pixel.box2d.color = color
        System.pixel.render()

    @staticmethod
    def new_object():
        from pygraphics.templates.object import Object
        object = Object()
        System.objects.append(object)
        return object
    
    @staticmethod
    def new_object_2d(path="", size = glm.ivec2(1, 1), offset = glm.vec2(0.0, 0.0)):
        from pygraphics.templates.object_2d import Object2D
        object = Object2D()
        object.sprite_renderer.load_texture(path)
        object.sprite_renderer.set_size(size)
        object.sprite_renderer.set_offset(offset)
        System.objects.append(object)
        return object
    
    @staticmethod
    def new_cube_2d():
        from pygraphics.templates.cube2d import Cube2D
        object = Cube2D()
        System.objects.append(object)
        return object
    
    @staticmethod
    def new_image_2d():
        from pygraphics.templates.image2d import Image2D
        object = Image2D()
        System.objects.append(object)
        return object
    
    @staticmethod
    def loop(code_source):     
        System.load_programs()
        for object in System.objects:
                object.start()
        while not System.render.is_closed() and not System.end:
            delta_time = System.time_manager.get_delta_time()
            System.time_manager.update()
            System.render.update()
            System.gui.update()
            for object in System.objects:
                object.update(delta_time, System.camera)
                object.render()
            code_source()
            System.gui.info()
            System.gui.tweak()
            System.gui.render()
            System.input_manager.buffers_events()
        System.gui.clear()
        System.render.clear()

    @staticmethod
    def exit():
        System.end = True
    
