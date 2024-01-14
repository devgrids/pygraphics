from pygraphics.engine.components.component import Component

class Animation():
    def __init__(self):
        self.name = ""
        self.loop = False


class Animator(Component):
    def __init__(self):
        self.animations = {}
        self.frame = 0
        self.timer = 0.0
        self.count = 0
        self.sprite = None  
        self.animation_completed = False
        self.loop = True
        self.max_timer = 0.05

    def add_animation(self, animation):
        self.animations[animation.name] = animation

    def set_sprite(self, sprite):
        self.sprite = sprite
        self.count = self.sprite.to.size.x

    def load_animation(self, name):
        pass
   
    def start(self):
        pass

    def update(self, delta_time):
        self.timer += delta_time

        if self.timer > self.max_timer:
            self.timer = 0.0
            if not self.animation_completed:
                self.sprite.to.offset.x = self.sprite.to.offset.x+1
                if self.sprite.to.offset.x >= self.count:
                    if not self.loop:
                        self.animation_completed = True
                    else:
                        self.sprite.to.offset.x = 0

    def render(self):
        pass


