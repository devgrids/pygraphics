import glm

class Entity:
    def __init__(self):
        self.position = glm.vec3(0.0, 0.0, 0.0)
        self.rotation = glm.vec3(0.0, 0.0, 0.0)
        self.scale = glm.vec3(1.0, 1.0, 1.0)
        self.model = glm.mat4(1.0)
        self.enabled = True

    def set_position(self, position):
        self.position = position

    def set_rotation(self, rotation):
        self.rotation = rotation

    def set_scale(self, scale):
        self.scale = scale

    def set_model(self, model):
        self.model = model

    def set_enabled(self, enabled):
        self.enabled = enabled

    def get_position(self):
        return self.position

    def get_rotation(self):
        return self.rotation

    def get_scale(self):
        return self.scale

    def get_model(self):
        return self.model

    def get_enabled(self):
        return self.enabled

    def compute_model_matrix(self):
        pass

    def step(self, delta_time):
        pass
