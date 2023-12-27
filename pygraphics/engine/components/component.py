from pygraphics.engine.core.object import Object

class Component(Object):
    def __init__(self):
        super().__init__() 
        self.type = id(Component)

    def is_class_type(self, class_type):
        return class_type == self.type


# component = Component()
# print(component.is_class_type(id(Component)))
