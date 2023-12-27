from pygraphics.engine.core.object import Object

class GameObject(Object):
    def __init__(self):
        self.components = []

    def add_component(self, component_type, *args, **kwargs):
        component = component_type(*args, **kwargs)
        self.components.append(component)
        return component

    def get_component(self, component_type):
        for component in self.components:
            if isinstance(component, component_type):
                return component
        return None

    def remove_component(self, component_type):
        component_to_remove = None
        for component in self.components:
            if isinstance(component, component_type):
                component_to_remove = component
                break

        if component_to_remove:
            self.components.remove(component_to_remove)
            return True
        return False

    def get_components(self, component_type):
        return [c for c in self.components if isinstance(c, component_type)]

    def remove_components(self, component_type):
        original_length = len(self.components)
        self.components = [c for c in self.components if not isinstance(c, component_type)]
        return original_length - len(self.components)

# # Ejemplo de uso
# class Component:
#     pass

# class Transform(Component):
#     pass

# game_object = GameObject()
# transform = game_object.add_component(Transform)
# found_transform = game_object.get_component(Transform)
# print(found_transform == transform)  
