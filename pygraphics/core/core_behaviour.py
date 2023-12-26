from pygraphics.core.game_object import GameObject
from pygraphics.components.transform import Transform

class CoreBehaviour:
    def __init__(self):
        self.gameObject = GameObject()
        self.gameObject.add_component(Transform)

        self.transform = self.gameObject.get_component(Transform)

    def start(self):
        pass

    def update(self):
        pass

    def render(self):
        pass

# # Ejemplo de uso
# class MyBehaviour(CoreBehaviour):
#     def start(self):
#         print("Starting MyBehaviour")

#     def update(self):
#         print("Updating MyBehaviour")

#     def render(self):
#         print("Rendering MyBehaviour")

# my_behaviour = MyBehaviour()
# my_behaviour.start()
# my_behaviour.update()
# my_behaviour.render()
