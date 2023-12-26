import glfw
from pygraphics.input_manager.input_manager import InputManager

class GLFWInputManager(InputManager):
    def __init__(self):
        super().__init__()
        self.key_manager = None
        self.mouse_manager = None
        self.mouse_pressed_manager = None
        self.scroll_manager = None
        self.framebuffer_size = None
        self.window = None

    def init(self):
        super().init()

        def key_callback(window, key, scancode, action, mods):
            if action == glfw.PRESS:
                self.key_b_event[key] = '1'
            elif action == glfw.RELEASE:
                self.key_b_event[key] = '0'
                self.is_key_pressed_flag = False

        # def mouse_callback(window, xpos, ypos):
        #     self.mouse_old_pos = self.mouse_pos
        #     self.mouse_pos = (xpos, ypos)

        # def mouse_button_callback(window, button, action, mods):
        #     if action == glfw.PRESS:
        #         if button == glfw.MOUSE_BUTTON_RIGHT:
        #             self.button_mouse_right_pressed_manager = True
        #         elif button == glfw.MOUSE_BUTTON_LEFT:
        #             self.button_mouse_left_pressed_manager = True
        #     elif action == glfw.RELEASE:
        #         if button == glfw.MOUSE_BUTTON_RIGHT:
        #             self.button_mouse_right_pressed_manager = False
        #         elif button == glfw.MOUSE_BUTTON_LEFT:
        #             self.button_mouse_left_pressed_manager = False
        #         self.is_mouse_pressed_flag = False

        # def scroll_callback(window, xoffset, yoffset):
        #     self.scroll_offset = (xoffset, yoffset)

        # def framebuffer_size_callback(window, width, height):
        #     glViewport(0, 0, width, height)

        glfw.set_key_callback(self.window, key_callback)
        # glfw.set_cursor_pos_callback(self.window, mouse_callback)
        # glfw.set_mouse_button_callback(self.window, mouse_button_callback)
        # glfw.set_scroll_callback(self.window, scroll_callback)
        # glfw.set_framebuffer_size_callback(self.window, framebuffer_size_callback)

    def is_pressed(self, key):
        return super().is_pressed(ord(key) - 32)

    def is_pressed_down(self, key):
        if self.is_key_pressed_flag:
            return False
        is_pressed = super().is_pressed_down(ord(key) - 32)
        if is_pressed and not self.is_key_pressed_flag:
            self.is_key_pressed_flag = True
        return is_pressed

    def link_render(self, render):
        super().link_render(render)
        self.window = render.get_window()

    def set_mouse_cursor(self, enabled):
        mode = glfw.CURSOR_NORMAL if enabled else glfw.CURSOR_DISABLED
        glfw.set_input_mode(self.window, glfw.CURSOR, mode)

    def buffers_events(self):
        glfw.poll_events()
        glfw.swap_buffers(self.window)
