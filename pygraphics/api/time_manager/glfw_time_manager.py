import glfw
from pygraphics.api.time_manager.time_manager import TimeManager

class GLFWTimeManager(TimeManager):
    def __init__(self):
        super().__init__()

    def init(self):
        super().init()

    def update(self):
        self.new_time = float(glfw.get_time())
        self.delta_time = self.new_time - self.last_time
        self.last_time = self.new_time

    def get_delta_time(self):
        return super().get_delta_time()
