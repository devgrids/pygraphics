from OpenGL.GL import *
from pygraphics.graphics_api import GraphicsApi
from pygraphics.api.camera.orthographic_camera import OrthographicCamera
from pygraphics.api.camera.camera import Camera
from pygraphics.graphics_resource import GraphicsResource

class System:

    render = None
    input_manager = None
    gui = None
    camera = None

    end = False
    cursor_mouse_enabled = True

    objects = []

    @staticmethod
    def init():
        System.render = GraphicsApi.get_new_render()
        System.input_manager = GraphicsApi.get_new_input_manager()
        System.gui = GraphicsApi.get_new_gui()
        
        System.camera = OrthographicCamera()
        
        System.render.init()
        System.gui.init()

        System.input_manager.link_render(System.render)
        System.gui.link_render(System.render)

        System.input_manager.link_gui(System.gui)
        System.input_manager.init()

        GraphicsResource.init()

    @staticmethod
    def exit():
        System.end = True

    @staticmethod
    def new_character2d():
        from pygraphics.templates.character2d import Character2D
        character2d = Character2D()
        System.objects.append(character2d)
        return character2d
    
    @staticmethod
    def loop(code_source):       
        for object in System.objects:
                object.start()
        while not System.render.is_closed() and not System.end:
            System.render.update()
            System.gui.update()
            code_source()
            for object in System.objects:
                object.update()
                object.render()
            System.gui.render()
            System.input_manager.buffers_events()

        System.gui.clear()
        System.render.clear()
