class Render:
    def __init__(self):
        self.width = 0
        self.height = 0

    def init(self):
        pass

    def clear(self):
        pass

    def is_closed(self):
        return False

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height
