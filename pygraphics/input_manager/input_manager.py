class InputManager:
    def __init__(self, render=None):
        self.render = render
        self.key_b_event = ['0'] * 512
        self.mouse_pos = (0, 0)
        self.mouse_old_pos = (0, 0)
        self.scroll_offset = (0.0, 0.0)
        self.button_mouse_right_pressed_manager = False
        self.button_mouse_left_pressed_manager = False
        self.is_key_pressed_flag = False
        self.is_mouse_pressed_flag = False

    def init(self):
        for i in range(512):
            self.key_b_event[i] = '0'
        self.is_key_pressed_flag = False
        self.is_mouse_pressed_flag = False

    def link_render(self, render):
        self.render = render

    def is_pressed(self, key):
        return self.key_b_event[ord(key)] == '1'

    def is_pressed_down(self, key):
        return self.key_b_event[ord(key)] == '1'

    def buffers_events(self):
        pass

    def get_mouse_pos(self):
        return self.mouse_pos

    def get_scroll_offset(self):
        return self.scroll_offset

    def is_button_mouse_pressed(self, right):
        if right:
            return self.button_mouse_right_pressed_manager
        else:
            return self.button_mouse_left_pressed_manager

    def is_button_mouse_pressed_down(self, right):
        if right:
            return self.button_mouse_right_pressed_manager
        else:
            return self.button_mouse_left_pressed_manager

    def set_mouse_cursor(self, enabled):
        pass

