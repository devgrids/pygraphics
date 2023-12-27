from components.component import Component
import time

class Animator(Component):
    max_timer = 0.05

    def __init__(self):
        self.frame = 0
        self.count = 0
        self.timer = 0.0
        self.loop = False
        self.animation_completed = False
        self.last_frame_time = 0.0
        self.delta_time = 0.0
        self.animation = []

    def set_animation(self, animation):
        self.animation = animation
        self.count = len(self.animation)
        self.animation_completed = False
        self.frame = 0

    def set_loop(self, loop):
        self.loop = loop
        self.frame = 0

    def update(self):
        current_time = time.time()
        self.delta_time = current_time - self.last_frame_time
        self.last_frame_time = current_time

        self.timer += self.delta_time

        if self.timer > self.max_timer:
            self.timer = 0.0
            if not self.animation_completed:
                self.frame += 1
            if self.frame >= self.count:
                if not self.loop:
                    self.animation_completed = True
                else:
                    self.frame = 0

    def is_animation_finished(self):
        return self.animation_completed

    def get_frame(self):
        if self.animation:
            return self.animation[self.frame % self.count]
        return None

# Ejemplo de uso
animator = Animator()
# Aquí deberías agregar las texturas a la animación
animator.set_animation([texture1, texture2, texture3])
animator.set_loop(True)
while True:
    animator.update()
    frame_texture = animator.get_frame()
    # Renderizar frame_texture
