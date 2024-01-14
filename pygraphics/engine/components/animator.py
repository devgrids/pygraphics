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
        self.count = 6
        self.sprite = None  
        self.animation_completed = False
        self.loop = True

    def add_animation(self, animation):
        self.animations[animation.name] = animation

    def next_offset(self, deltatime):
        self.timer += deltatime

        if self.timer > 0.05:
            self.timer = 0.0
            self.sprite.to.size.x = 6
            if not self.animation_completed:
                self.sprite.to.offset.x = self.sprite.to.offset.x+1
                if self.sprite.to.offset.x >= self.count:
                    if not self.loop:
                        self.animation_completed = True
                    else:
                        self.sprite.to.offset.x = 0


