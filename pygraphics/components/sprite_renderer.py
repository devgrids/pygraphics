from components.component import Component

class SpriteRenderer(Component):
    def __init__(self):
        # Aquí se asume la existencia de una implementación Python de Renderer y Texture2D
        self.renderer = Renderer(Resources.get_shader("sprite"))
        self.sprite_current = Resources.get_texture("default")

    def set_sprite(self, sprite):
        self.sprite_current = sprite

    def render(self, position, size, rotate):
        self.renderer.draw(self.sprite_current, position, size, rotate)

    def set_flip(self, flip):
        self.renderer.set_flip(flip)
