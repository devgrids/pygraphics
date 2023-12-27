import time

class TimeManager:
    def __init__(self):
        self.new_time = 0.0
        self.delta_time = 0.0
        self.last_time = 0.0

    def init(self):
        self.new_time = self.delta_time = self.last_time = 0.0

    def update(self):
        self.new_time = time.time()
        self.delta_time = self.new_time - self.last_time
        self.last_time = self.new_time

    def get_delta_time(self):
        return self.delta_time
