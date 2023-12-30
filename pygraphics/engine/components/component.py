from pygraphics.engine.core.object import Object
from pygraphics.helpers.class_type import ClassType

class Component(Object, ClassType):
    def __init__(self):
        Object.__init__(self) 
        ClassType.set_class(self, Component)
